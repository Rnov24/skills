#!/usr/bin/env python3
"""Start one or more background servers, wait for ports to open, run a command, and tear down.

Adapted from anthropics/skills (webapp-testing, Apache-2.0 © Anthropic).

Usage:
    # Single server
    python3 scripts/with-server.py --server "npm run dev" --port 5173 -- npm test
    python3 scripts/with-server.py --server "python server.py" --port 3000 -- pytest

    # Multiple servers (e.g. backend + frontend)
    python3 scripts/with-server.py \
      --server "cd backend && python server.py" --port 3000 \
      --server "cd frontend && npm run dev" --port 5173 \
      -- pytest tests/e2e
"""

import argparse
import socket
import subprocess
import sys
import time


def is_server_ready(port: int, timeout: int = 30) -> bool:
    """Wait for server to be ready by polling the port."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(('localhost', port), timeout=1):
                return True
        except (socket.error, ConnectionRefusedError):
            time.sleep(0.5)
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description='Run command with one or more background servers')
    parser.add_argument('--server', action='append', dest='servers', required=True, help='Server command to spawn')
    parser.add_argument('--port', action='append', dest='ports', type=int, required=True, help='Port to wait on (must match --server count)')
    parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds per server (default: 30)')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='Command to run once servers are ready')

    args = parser.parse_args()

    if args.command and args.command[0] == '--':
        args.command = args.command[1:]

    if not args.command:
        print("Error: No command specified to run", file=sys.stderr)
        sys.exit(1)

    if len(args.servers) != len(args.ports):
        print("Error: Number of --server and --port arguments must match", file=sys.stderr)
        sys.exit(1)

    servers = [{'cmd': cmd, 'port': port} for cmd, port in zip(args.servers, args.ports)]
    server_processes = []

    try:
        for i, server in enumerate(servers):
            print(f"[with-server] Starting server {i+1}/{len(servers)}: {server['cmd']}")
            process = subprocess.Popen(
                server['cmd'],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            server_processes.append(process)

            print(f"[with-server] Waiting for port {server['port']}...")
            if not is_server_ready(server['port'], timeout=args.timeout):
                raise RuntimeError(f"Server failed to start on port {server['port']} within {args.timeout}s")

            print(f"[with-server] Port {server['port']} ready")

        print(f"[with-server] All {len(servers)} server(s) ready; executing: {' '.join(args.command)}\n")
        result = subprocess.run(args.command)
        sys.exit(result.returncode)

    finally:
        print(f"\n[with-server] Tearing down {len(server_processes)} server(s)...")
        for i, process in enumerate(server_processes):
            try:
                process.terminate()
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            print(f"[with-server] Server {i+1} stopped")
        print("[with-server] All servers stopped")


if __name__ == '__main__':
    main()
