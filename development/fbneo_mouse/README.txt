FBNeo IR Mouse / Neo Pong - TEST v5 (Windows x64)

INSTALL
Close RetroArch. Replace fbneo_mouse_libretro.dll in cores and its .info in
info. Existing RetroBat fbneo_mouse entries continue to apply. Core
Information should show IR Mouse v5. Keep your previous DLL as a backup.

NEO PONG: TWO WIIMOTES
Use neopong.zip, the arcade Neo Pong homebrew v1.1 (pong_p1.rom CRC 9f35e29d).
The supplied neogeo.zip successfully loaded in native testing. Keep the
matching BIOS beside neopong.zip, or in the normal FBNeo BIOS search location.
Neither ROM nor BIOS is included in this package.

Settings > Input > RetroPad Binds / Port Controls:
  Port 1 Device Index = your first Wiimote's vJoy device.
  Port 2 Device Index = your second Wiimote's separate vJoy device.
Do not select the same vJoy device for both players.
Analog to Digital Type = None, sensitivity 1.0, deadzone 0.0.

Quick Menu > Controls:
  Port 1 Device Type = Wiimote IR Mouse (left analog).
  Port 2 Device Type = Wiimote IR Mouse (left analog).
Keep Port 1 mapped to emulated Port 1 and Port 2 to emulated Port 2.
Save a Neo Pong game remap after configuring both players.

Each Wiimote's vertical aim controls its own paddle directly. Horizontal aim
is unused. Pointer extremes map to the original native paddle limits Y=20..206.
This is direct positioning, not fixed-speed Up/Down movement or flick control.
Minus = coin; Plus = that player's Start. B/A retain native game buttons.
Start Player 1; after the initial Ready sequence, press Player 2's Plus to
join. In the native test, Player 2 Start during the first Ready sequence was
not accepted; pressing it again after play began successfully joined.

HOW THE PATCH WORKS
The core checks the exact game name and movement code signatures. For each
IR player it redirects only that player's manual movement branch to a small
in-memory routine containing the current paddle target. It keeps native ball,
collision, scoring and AI code; movement direction is supplied to the normal
input path for the game's ball-deflection logic.
The ROM archive on disk is never modified. Changing either player's device
back to a normal controller restores that player's original movement branch.
The patch is only for neopong v1.1. neoponga v1.0 and other Neo Geo games are
not patched. A CPU opponent remains AI until Player 2 joins normally.

THE FOUR CONFIRMED GAMES
arkanoid.zip, centiped.zip, milliped.zip, missile.zip retain their earlier
calibrated pointing profiles. Their six-target native regression tests passed.
Arkanoid: Plus = 1P Start, Wiimote 1 / RetroPad X = 2P Start, Minus = coin,
B = launch/fire. Reset an old game remap if it overrides those bindings.
Missile Command: D-pad Left/Down/Right fire left/center/right bases.
Home is still available for your frontend menu; the AHK +/- exit chord is
independent of the core.
Other trial game drivers (Rampart, bowling, horseshoes, Quantum, Arkanoid II,
Marble Madness) are removed from this build, matching the narrowed project.
Neo Geo drivers are included to support Neo Pong, but only Neo Pong has a
custom paddle patch. Do not assume other Neo Geo paddle games are converted.

DIAGNOSTICS
Core Options > Input > IR Mouse Diagnostics remains enabled by default.
The save directory contains fbneo-ir-mouse.log; launching another game
replaces it. Neo Pong has PADDLE rows with player, target_y and actual_y.
A target_y of -1 means that player's normal controller movement is restored.
For IR paddles, target_y and actual_y should match after the next game update.
Logs also work with Player 1 normal and Player 2 IR.

VALIDATION AND LIMITS
Native Linux tests used the supplied game and BIOS:
- Five pairs of independent targets, including opposite edges, matched exactly.
- Both paddles swapped between opposite screen edges in one emulated frame.
- Held targets stayed still during the checks.
- Normal P1 / IR P2 and IR P1 / normal P2 both worked.
- Returning P1 from normal controls to IR restored direct positioning.
- Native gameplay ran for 1500 frames with moving/bouncing ball and scoring.
- Original four pointing profiles passed their regressions.
The Windows x64 DLL is cross-compiled; PE format, libretro exports and imports
were checked. No Windows/Wiimote hardware test was performed here.
Fast-position collision and ball-deflection feel still need real playtesting;
the test is not a claim that every game mode or power-up is verified.

SOURCE AND TESTS
Source.tar.gz contains full modified source; v4-to-v5.patch shows the changes.
Makefile.mouse builds this subset. Tests are provided without ROMs or states.
The probe.py harness uses a native .so and requires numpy/Pillow. Scripts
assume the fbneo-mouse-work folder layout and actual matching ZIPs/BIOS.
Run pong-boot.py then pong-join.py, then test-v5-play.py to generate temporary
fixtures; test-v5-pong.py tests target/hold and device switching. State fixtures
and game RAM dumps are deliberately excluded from the package.
