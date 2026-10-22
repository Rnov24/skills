# Audit A-004 — the 18 merged UX laws against two real UIs

Auditor run, 2026-10-22. Method and verdict vocabulary per brief.md in
this folder. Evidence is labelled RENDER (the orchestrator's screenshots
in this folder), DOM/HTML (an element fact in markup), or SOURCE
(file:line in the target's code). Dynamic behaviour is judged from
source handlers where a still render cannot show it, and the entry says
which evidence carried the verdict. Rules are audited in the order they
appear in skills/design/references/ux-heuristics.md: the 8 in "Choice,
grouping, and convention", the 3 bolded in "Forms and input", the 4
bolded in "Feedback and system states", the 3 bolded in "Lists and data
density". Neither target repository was modified.

---

## Target A — NetAcad AI Assistant extension popup

Surface: popup.html (structure + CSS), popup.js (behaviour), with
scraper.js / content.js consulted where the popup's messages land.
Render: target-a-netacad-popup-420.png. The model dropdown is empty in
that render because extension storage APIs are absent outside the
extension host (per the brief); that element is judged from source.

### Choice, grouping, and convention

**1. One purpose per screen (Hick) — PASS.**
RENDER: one 340px surface with a single job, controlling this
extension. Everything on it serves that job, and the work is grouped
behind three headed panels (AI provider, Mercury Decide, Automation)
with the run actions separated below them; the lowest-priority items
(the two exports) are demoted to small ghost buttons rather than
competing as peers. No element on the screen serves a second product
or a second task.

**2. Recommend, don't dump (Hick) — PASS.**
SOURCE: every provider's model list carries an explicit recommendation
— the first preset of each list is labelled "(default)" (popup.js:26-58,
e.g. "gemini-3.6-flash (default)", "gpt-4o-mini (default)"), and when
no model has been saved, updateProviderUI selects the first preset
rather than leaving the choice open (popup.js:98). DOM/HTML: the
provider select itself opens on its first option, Google Gemini
(popup.html:640). The user is never handed an undifferentiated list
with the choosing left entirely to them.

**3. Familiar before novel (Jakob) — PASS.**
RENDER + DOM/HTML: the popup uses the conventional extension-settings
vocabulary throughout — labelled selects for provider and model, a
password field for API keys, round toggle switches for booleans,
a primary action button for the main task, status in the header.
Nothing on the surface invents a pattern whose advantage would need
naming; even the keyboard shortcut shown in the header (Alt+Shift+Q)
is the platform's own convention displayed, not replaced.

**4. Spacing signals grouping (Proximity) — PASS.**
SOURCE (CSS in popup.html): a label sits 5px above its own input
(popup.html, `label { margin-bottom: 5px }`, form groups at
popup.html:210) while unrelated groups are separated by the panels'
14px padding and the 14px column gap of the content area
(popup.html:168). RENDER: in each automation row the icon, label, and
description cluster tightly on the left and the toggle they belong to
sits on the same row's right edge; no control is nearer to another
row's label than to its own.

**5. Chunk, and carry it forward (Miller) — PASS.**
RENDER: the surface is chunked into three headed groups plus a run
area, so no unbroken list of controls exists. SOURCE, for the
carry-forward half: everything the user enters is persisted and
re-presented, so nothing must be remembered or re-typed across
openings — settings load from chrome.storage.sync on open and are
written back into the fields (popup.js:117-133), and each toggle
persists the moment it changes (popup.js:147-152).

**6. Same look, same purpose (Similarity) — PASS.**
DOM/HTML: all five boolean settings use the identical `.switch`
component (popup.html, `.switch` styles and the five switch labels);
all panels share the `.panel` treatment, and the one panel that
differs (Mercury Decide, dark navy) differs because it is a different
kind of thing — a separate provider feature — while keeping the same
switch inside it. Buttons keep one base (`.btn`) with the variant
fixed per role: navy = save, blue primary = solve, secondary =
secondary runs and controls, ghost = exports. No visual treatment is
reused for a different kind of action.

**7. Connect what belongs together (Uniform Connectedness) — PASS.**
RENDER + DOM/HTML: each automation toggle sits inside the same row
container as the label and description it controls
(`.automation-row`, popup.html:355); the Mercury toggle sits in the
Mercury panel's own header row, and the Mercury key field sits inside
that panel under a divider. The Save button directly follows the last
settings panel it saves. No control is visually attached to content
it does not affect.

**8. Essentials first and last (Serial Position) — FAIL.**
Rule's operative words: "the most important item comes first and the
final action or takeaway comes last. Low-priority items sit in the
middle, never in the two positions people remember."
RENDER + DOM/HTML: the first position is honoured (status header,
then the provider configuration everything else depends on, and the
primary action leads the run area). The last position is not: the
final action row of the popup is the pair of low-priority ghost
buttons "Export Markdown (.md)" and "Export JSON (.json)"
(popup.html:810-811, `.btn-ghost-row` after the Pause/Stop row at
popup.html:806-807). The screen's most-remembered closing slot is
spent on its least important actions, and only the empty `#status`
line (popup.html:831) sits below them. (The auditor flags a wording
ambiguity in this rule in report.md: whether "last" scopes to the
last action or the last element.)

### Forms and input (bolded rules)

**9. Defaults are safe (Hick) — PASS.**
SOURCE: the shipped defaults are set in popup.js:126-131. The one
default that would create a real commitment — Auto-Submit Answers,
which hands answers to the graded quiz — ships OFF (it turns on only
when storage holds an explicit true: `res.autoSubmit === true`).
Mercury Decide likewise ships off. The three defaults that ship on
(autoSelect `!== false`, showAnswers `!== false`, processOnSwitch
`!== false`, also `checked` in popup.html:720, 759, 779) execute
nothing by themselves: no answer is selected, submitted, or solved
until the user presses a run button, and every default is a visible
toggle that can be changed in one click at the exact point where it
is shown.

**10. Input is tolerated (Postel) — PASS.**
SOURCE: both API key fields are normalised rather than policed — the
main key is read with `.trim()` on save (popup.js:235) and the Mercury
key with `.trim()` on change (popup.js:158), so pasted keys with
leading or trailing whitespace are accepted and cleaned instead of
rejected. The custom model name is likewise trimmed via the same save
path. No field on this surface states a rigid format that a reasonable
typist would trip over; the model choice that could have been a
free-text format trap is a preset list with a free-text escape hatch
(popup.js:80-98).

**11. Impossible actions are unavailable, risky ones are warned (Postel) — FAIL.**
Rule's operative words: "An action that cannot succeed in the current
state is disabled with its reason reachable, not left clickable to
fail. Before a destructive or irreversible action, the interface names
what will be lost and requires a deliberate confirmation."
Both halves break. Impossible half — DOM/HTML + SOURCE: the Pause and
Stop buttons carry no `disabled` attribute and no handler ever
disables them (popup.html:806-807); they are fully clickable when
nothing is running. Clicking Pause while idle is not rejected:
popup.js:310-312 flips the button to "Resume" and shows "Paused", and
the state machine accepts the fiction — pauseAutonomousLoop sets
`isAutonomousPaused = true` unconditionally (scraper.js:82-86). The
run buttons are likewise never disabled while a run is active
(popup.js contains no `processPageBtn.disabled` assignment; the
already-running guard lives silently in scraper.js:386-390).
Risky half — SOURCE: no confirmation exists anywhere on this surface
(`confirm(` appears zero times in popup.html and popup.js). Pressing
"Auto-Solve Quiz" with Auto-Submit enabled submits answers into a
graded NetAcad quiz, and "Auto-Scroll & Complete Module" marks course
modules complete; neither press names what will happen or asks for a
deliberate confirmation first (handlers at popup.js:288-303 pass
straight to sendToTab).

### Feedback and system states (bolded rules)

**12. Feedback lands within ~400ms (Doherty) — PASS.**
SOURCE (dynamic rule, judged from handlers): acknowledgement is
synchronous in the click handlers themselves. Pressing Auto-Solve
sets the status line to "Starting Quiz Auto-Pilot..." with duration 0
— it stays until the response replaces it — before the message to the
tab is even sent (popup.js:290-292); Auto-Scroll does the same
(popup.js:299-301). Save gives feedback on the control itself: the
button flashes green for 1200ms in its storage callback, alongside
the status text (popup.js, save handler). The header badge then tracks
the run state on a 1-second poll (popup.js:176-200, 225). No action on
this surface leaves the user wondering whether the press registered.
(The auditor notes in report.md that the run buttons acknowledge via
the adjacent status line rather than a state change on the button
itself, and that the badge can lag up to the 1s poll interval.)

**13. Errors preserve the work (Postel) — PASS.**
SOURCE: error paths never touch the user's input. When the tab cannot
be reached, sendToTab only writes the error into the status line —
"Could not reach the NetAcad tab. Reload the page and try again."
(popup.js:219-224) — and every field keeps its content. Save's
validation failures return early after setting a status message
(empty custom model name; no key at all) without clearing or
resetting any field, and toggles persist independently of the save
path (popup.js:147-152), so work already done survives a failed save.
The status line itself is `aria-live="polite"` (popup.html:831), and
each error names the problem and the next step in plain words.

**14. Flows end memorably (Peak-End) — FAIL.**
Rule's operative words: "A completed flow ends on a designed
completion state: what was accomplished, in the user's terms, and
what happens next. No flow ends on an empty screen, a bare spinner
that stops, or a state the user must interpret."
SOURCE: a finished run ends on none of that. The content script only
sends its response after the loop has finished (content.js,
processPage handler), and the popup's success branch answers that
completion with the present-tense text "Quiz Auto-Pilot running"
(popup.js:292) — a state the user must interpret, since the run is in
fact over. That text is set with the default 3500ms duration, after
which setStatus clears the status line entirely (popup.js:208-212),
leaving a blank status area and a header badge back at "Ready". The
engines record completion only to the console ("Quiz Auto-Pilot
finished.", scraper.js:489; "Course Scroller finished.",
scraper.js:612) — nothing anywhere in the popup states what was
accomplished (no questions solved, no sections completed) or what
happens next.

**15. Progress feels like progress (Goal-Gradient, Zeigarnik) — FAIL.**
Rule's operative words: "Multi-step work is divided into named
milestones, progress already made is emphasised over the total, and
remaining work is stated specifically ... rather than as a bare
percentage."
SOURCE: the data for exactly this exists and the popup refuses to
show it. The scroller tracks its position (scraper.js:30,
scrollerCurrentSection, updated at scraper.js:530) and the status
response carries both counters to any asker (content.js:384-386,
`scrollCurrent` and `scrollTotal`). The popup's poll handler reads
that same response every second and renders only three words —
"Auto-Pilot Active", "Auto-Pilot Paused", "Course Scroller Active",
or "Ready" (popup.js:176-200) — never touching res.scrollCurrent or
res.scrollTotal. During a run over many sub-topics, the surface that
started the work shows no milestone reached, no count of sections
done, and no statement of what remains.

### Lists and data density (bolded rules)

**16. One dominant action per section (Von Restorff) — PASS.**
RENDER + SOURCE (CSS in popup.html): the settings panels contain no
call to action at all. In the action area the hierarchy is legible:
Auto-Solve Quiz is the single dominant action — the tallest button
(44px, `.btn-primary`, popup.html:495), the only saturated blue, the
only one with an icon — while Save settings sits above it as a
quieter 38px navy bar (`.btn-navy`, popup.html:479), Auto-Scroll is a
white secondary, Pause/Stop are smaller secondaries, and the exports
are 34px ghost buttons (`.btn-ghost`, popup.html:545). Secondary
actions are visibly quieter at every step down.

**17. Actions sit beside their content (Fitts) — PASS.**
RENDER + DOM/HTML: every toggle sits on the same row as the setting
it switches, at the row's right edge. Save settings directly follows
the last settings panel. The run controls are stacked in one run
area — solve, scroll, pause/stop, exports within a few pixels of each
other — so once the user's attention is on running the tool, every
related action is already there; on a 340px popup no action is ever
a screen-crossing away from its content.

**18. The path stays short (Parkinson) — PASS.**
SOURCE + RENDER: configuration is paid for once and never again —
settings and toggles persist (popup.js:117-152), so reopening the
popup is a one-press path to a run. Toggles take effect on change
with no save step interposed (popup.js:147-152); only the key/model
block uses the single explicit Save. The repeat action has a genuine
shortcut, shown in the header: Alt+Shift+Q triggers the solve from
the page. No step in any path on this surface exists merely to
confirm a reversible action, and nothing asks twice for information
already given.

### Target A tally

PASS 14 · FAIL 4 · NA 0.
FAILs: Serial Position (8), Impossible actions / risky ones warned
(11), Flows end memorably (14), Progress feels like progress (15).

---

## Target B — EXAMIND auth screens (login + register)

Surfaces: src/app/(auth)/login/page.tsx and register/page.tsx, judged
as one target across both screens. Renders:
target-b-examind-login-1280.png, target-b-examind-login-390.png,
target-b-examind-register-1280.png. The served build at
http://localhost:3100/login and /register was also dumped with headless
Chromium during this audit; the served DOM matched the source
(submit labels, role default, and code-section contents all present).
Dynamic verdicts are carried by the source handlers, as the brief
directs; no credentials were submitted anywhere.

### Choice, grouping, and convention

**1. One purpose per screen (Hick) — PASS.**
RENDER: each screen has exactly one job. Login is a single centred
card with one form and one decision. Register, though denser, is one
card serving the single registration decision, its parts grouped as
role, then code authorisation, then identity, and verification is a
separate second screen rather than more choices piled onto the first.
Nothing on either screen serves a purpose outside signing in or
registering.

**2. Recommend, don't dump (Hick) — PASS.**
SOURCE + RENDER: register recommends at both choice points. The role
starts on the most common one — `useState` initialises role to
'student' (register/page.tsx:57), and the render shows Siswa / Murid
selected with its check mark while the other two roles sit unselected.
The school follows the same pattern: when the school list loads, the
first school is selected automatically (register/page.tsx:112).
Login removes a choice instead of dumping it: one identifier field
accepts NISN, NIP, email, or username, so the user is never first
asked to classify themselves.

**3. Familiar before novel (Jakob) — PASS.**
RENDER + DOM/HTML: both screens follow the pattern comparable
products have taught — logo top-left, a small status pill top-right,
a centred card, labelled fields, the forgot-password link sitting at
the password label's right edge on login, the primary submit under
the fields, and the cross-link ("Daftar dengan Kode Sekolah" /
"Sudah punya akun? Masuk") below the card. The OTP screen is the
standard six-digit pattern, with `autoComplete="one-time-code"` so
platform autofill works the familiar way. The one mild novelty, role
cards on register, is built from labelled icon-plus-text options and
asks for no new gesture.

**4. Spacing signals grouping (Proximity) — PASS.**
RENDER: on login each label sits tight above its own input with a
wider gap before the next field group, and the password's helper link
sits on the password label's own row. On register the grouping is
done by spacing first: the role grid is one block, the school select,
code input, verification button, and their feedback share one panel
with its own heading, the identity fields form the next block, and
the password pair sits side by side as a related pair. Related items
are consistently nearer each other than anything unrelated.

**5. Chunk, and carry it forward (Miller) — PASS.**
SOURCE: the long task is chunked into two steps — registration form,
then OTP verification — and the system carries everything forward.
Step 2 repeats the address the code was sent to in its own text
("Kode verifikasi dikirim ke {email}"), so the user never has to
remember it; going back to step 1 loses nothing (the back handler
only changes the step and clears OTP messages, register/page.tsx:919
area); and the strongest instance crosses screens entirely: login's
unverified-email path routes to /register?verify=<email>, and
register's effect consumes that parameter to prefill the email and
land directly on step 2 (register/page.tsx:86-93).

**6. Same look, same purpose (Similarity) — PASS.**
RENDER + DOM/HTML: the two screens share one visual system — same
card, same input treatment, same dark full-width submit button, same
indigo text-link treatment for cross-links, same banner shapes for
error (rose) and success (emerald) on both screens and on the OTP
step. The dark slate full-width button always means "the primary
submit of this form" and never anything else; role options share one
card component whose selected state (indigo border, ring, check) is
identical across the three roles.

**7. Connect what belongs together (Uniform Connectedness) — PASS.**
RENDER + DOM/HTML: on register, the school select, registration-code
input, Verifikasi button, verification result, and error all live
inside one shared bordered container headed "Otorisasi Kode Provider
& Sekolah" — the Verifikasi button is even embedded in the right edge
of the very input it verifies, and its result renders directly under
that input. On login, the forgot-password link is attached to the
password field's label row, not floating elsewhere. No control is
visually joined to content it does not affect.

**8. Essentials first and last (Serial Position) — PASS.**
RENDER: login opens with what the screen is and what to use
(heading, then the instruction naming NISN for students and NIP for
teachers), and its form ends with the submit, with only the
registration cross-link after it. Register puts the essential first
decision first (role), the authorisation it depends on second,
identity next, passwords last before the submit — and the submit is
the form's final action, echoing the chosen role ("Daftar sebagai
Siswa"). The OTP screen likewise ends on its verify action, with
resend beneath it. No low-priority item occupies either remembered
position on any of the three screens.

### Forms and input (bolded rules)

**9. Defaults are safe (Hick) — PASS.**
SOURCE + RENDER: the two preselections are the role (student, the
most common for this product — register/page.tsx:57) and, when the
list loads, the first school (register/page.tsx:112). Neither creates
an unintended commitment: no paid tier, no public anything, nothing
recurring exists on these screens; both defaults are changed in one
tap or one select at the exact point where they are shown; and the
submit button restates the role default in its own label ("Daftar
sebagai Siswa") so the one consequential preselection is read back
to the user before it takes effect. Login preselects nothing.

**10. Input is tolerated (Postel) — PASS.**
SOURCE: normalisation is systematic, not incidental. The
registration code is forced to uppercase as it is typed
(register/page.tsx:541) and trimmed plus uppercased before both
verification (register/page.tsx:124) and submission
(register/page.tsx:194), so lowercase or padded codes are accepted.
Emails are trimmed and lowercased at every boundary
(register/page.tsx:197, and in the OTP send/verify paths). The
identifier is trimmed on both screens (login/page.tsx:91;
register submission). The OTP field strips non-digits as typed, so
spaces or pasted separators never become errors. Login's identifier
field is itself the tolerance: one field, four accepted identity
formats. Format requirements that remain (password length, matching
confirmation) are checked client-side with the requirement stated in
the message.

**11. Impossible actions are unavailable, risky ones are warned (Postel) — PASS.**
SOURCE: the impossible half is implemented as a pattern, not an
accident. The OTP verify button is disabled until the code is
exactly six digits — `disabled={otpCode.length !== 6 || verifyingOtp
|| Boolean(otpSuccess)}` (register/page.tsx:869) — and its handler
re-guards the same condition (register/page.tsx:254). Resend is
disabled during its cooldown and while sending, and the reason is
reachable in the button's own text: "Kirim ulang dalam {cooldown}
dtk" (register/page.tsx:901). The code's Verifikasi button is
disabled while a verification is in flight or the field is empty;
both submit buttons disable while loading (register/page.tsx:747;
login/page.tsx:277). For the risky half: nothing on these screens is
destructive or irreversible — registering creates an account and
loses nothing — so no confirmation is owed, and consistently, none
is demanded for the reversible steps either.

### Feedback and system states (bolded rules)

**12. Feedback lands within ~400ms (Doherty) — PASS.**
SOURCE (dynamic rule, judged from the submit handlers): on both
screens the acknowledgement is the first thing that happens and it
lands on the control itself. Login's handler sets loading as its
first statement (login/page.tsx:83); the button immediately disables
and swaps its label for a spinner plus "Memeriksa…". Register
validates synchronously before the request (register/page.tsx:174-186),
so bad input is answered instantly, then sets loading
(register/page.tsx:188) and the button shows a spinner plus
"Mendaftarkan Akun Institusi..." while disabled. The code's
Verifikasi button shows its own spinner while checking, and the OTP
buttons do the same. No press on either screen waits for a network
round trip to find out it registered.

**13. Errors preserve the work (Postel) — PASS.**
SOURCE: every error path writes a message and nothing else. Register's
submit catch sets only the error banner (register/page.tsx,
handleSubmit catch); its three client-side validation failures return
before any state is touched (register/page.tsx:174-186); all seven
field states survive every failure, and the OTP step keeps the user
in place with the email still displayed above the form. Login's catch
likewise sets only the message — identifier and password are never
reset anywhere in handleLogin; its finally block resets only the
loading flag. Messages name the fix in plain words ("Konfirmasi kata
sandi tidak cocok dengan kata sandi baru.", "Periksa kembali data dan
kode registrasi Anda."), and retry is simply pressing the same
still-populated form again.

**14. Flows end memorably (Peak-End) — PASS.**
SOURCE (the completion states exist in the handlers; the supplied
renders show the pre-submit screens, so this verdict is carried by
source): each flow ends on words that say what was accomplished and
what happens next. Register with immediate login shows "Pendaftaran
sebagai {role} berhasil! Mengalihkan ke dashboard Anda..." under a
check icon, then routes to that role's dashboard. Register with
verification ends step 2 with "Verifikasi berhasil! Sedang masuk ke
akun Anda..." then "Pendaftaran berhasil! Mengalihkan ke dashboard
Anda...", and when automatic login cannot follow, the ending is
still designed: "Verifikasi berhasil, silakan masuk." with a full
"Masuk ke Akun Anda" button. Login ends with its button turning to a
green checked "Berhasil Masuk" for 600ms (login/page.tsx:95) before
routing to the role's dashboard — the user's actual destination,
announced in the user's terms.

**15. Progress feels like progress (Goal-Gradient, Zeigarnik) — FAIL.**
Rule's operative words: "Multi-step work is divided into named
milestones, progress already made is emphasised over the total, and
remaining work is stated specifically ('2 steps left: address,
confirm') rather than as a bare percentage."
SOURCE + RENDER: registration is genuinely two-step work — the code
itself names the steps (`step` state, "1: Registration Form,
2: OTP Verification Panel", register/page.tsx:46-52) — but the user
is never shown any of it. Neither screen carries a step indicator, a
milestone name, or a statement of what remains: the step-1 render
(target-b-examind-register-1280.png) shows the full form with no
indication that a verification step follows it, and the step-2 screen
presents "Verifikasi Alamat Email" as a fresh, unpositioned screen —
nothing says it is step 2 of 2, nothing emphasises that the form
(the larger half of the work) is already done, and the only
countdown anywhere is the resend cooldown, which measures a lock
rather than progress. The division exists; the felt progress does
not.

### Lists and data density (bolded rules)

**16. One dominant action per section (Von Restorff) — PASS.**
RENDER: on the login card the dark "Masuk ke Sistem Ujian" button is
the only dominant action; the forgot-password link and the
registration link are quiet text links. On register the dark submit
("Daftar sebagai Siswa") dominates its card; the role cards are
selections, not competing calls to action; the Verifikasi button is a
small grey utility inside its field; the quick-fill code chips are
small pills; and the header's "Sudah punya akun? Masuk" is a quiet
pill outside the card. The OTP screen repeats the pattern: one dark
verify button, one quiet resend text button. Nothing competes at the
submit's weight anywhere.

**17. Actions sit beside their content (Fitts) — PASS.**
RENDER + DOM/HTML: the Verifikasi button is embedded in the right
edge of the code input it acts on; the resend control sits directly
beneath the OTP input it serves; each submit sits immediately below
its form's final field; the forgot-password link sits beside the
password label; the show/hide password eye sits inside the password
field's right edge. On the 390px login render the same adjacency
holds — no action requires crossing the screen from the content it
affects.

**18. The path stays short (Parkinson) — PASS.**
SOURCE + RENDER: login is two fields and one press, and the merged
identifier field removes the role-picking step other school portals
impose. Register keeps every field on one screen instead of taxing
the user with a wizard, and adds the OTP screen only when
verification is actually required. The repeat path has a real
shortcut: arriving from login's verification link lands the user
directly on step 2 with the email already filled
(register/page.tsx:86-93), and after verifying, the flow reuses the
email and password from step 1 to log the user in automatically
(register/page.tsx:270) instead of asking for them again on a fresh
login screen. Nothing is confirmed redundantly and nothing already
given is asked for twice.

### Target B tally

PASS 17 · FAIL 1 · NA 0.
FAIL: Progress feels like progress (15).

---

## Overall tally

| Target | PASS | FAIL | NA |
|---|---|---|---|
| A — NetAcad popup | 14 | 4 | 0 |
| B — EXAMIND auth | 17 | 1 | 0 |
| Both | 31 | 5 | 0 |

Every one of the 18 rules produced a reproducible verdict on both
targets; no rule had to be skipped on either surface.

## Out-of-scope observations

Real things noticed during the audit that none of the 18 rules
governs. These are not verdicts and were not counted above.

1. Target A: the model select renders empty outside the extension
   host because chrome.storage is unavailable there (brief-flagged
   environment artefact). In the real host it is populated from
   popup.js presets; recorded here only so nobody mistakes the
   render for an empty-state defect.
2. Target A: status and error messages auto-clear after 3500ms
   (popup.js:208-212), including error messages the user may not
   have finished reading. The general feedback rules outside the
   bolded four speak to error recovery; the bolded Doherty rule
   governs acknowledgement speed, not message persistence, so this
   was not counted — but it is the observation most likely to bite
   a real user.
3. Target A: neither API key field offers a show/hide toggle, and
   Target B is inconsistent on the same point — register's password
   field has an eye toggle (with an aria-label), login's password
   field has none. The show/hide rule sits in "Forms and input"
   outside the bolded three, so it is out of scope here.
4. Target B: the register screen ships working quick-fill
   registration codes as clickable chips in the served production
   build ("Kode Uji Coba Cepat", confirmed in the served DOM at
   localhost:3100/register), while login's equivalent demo switcher
   is correctly gated to development builds only
   (`process.env.NODE_ENV === 'development'`, login/page.tsx). The
   inconsistency is a product/security concern; none of the 18 rules
   speaks to test data in production, so it carries no verdict.
5. Target B: form-level errors on both screens appear in a banner
   above the form rather than below the field they belong to. The
   error-placement rule is one of the non-bolded Forms rules, so it
   is out of scope for this audit; the bolded Errors-preserve rule
   was judged on preservation and message quality only.
6. Target B: on register, the school select auto-selects the first
   school in code (register/page.tsx:112) but shows its placeholder
   option until the /auth/schools response lands, so a user whose
   network stalls sees an unselected required field with no loading
   indication on the control. Noted as an observation; the Defaults
   verdict above judges the default that the code establishes.
