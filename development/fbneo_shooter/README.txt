FBNeo Shooter IR v3 Final - Windows x64

INSTALL
Replace fbneo_galaga_ir_libretro.dll in:
  D:\RetroBatGun\emulators\retroarch\cores
Replace fbneo_galaga_ir_libretro.info in:
  D:\RetroBatGun\emulators\retroarch\info
Close RetroArch before replacing the DLL.
The core name/basename is unchanged: FBNeo Galaga IR / fbneo_galaga_ir.
Your existing RetroBat entries work; no es_systems_main.cfg change needed.

INPUT
Quick Menu > Controls > Port 1 Controls > Device Type:
  Wiimote IR Ship + Buttons
For two-player turns, use the same type on Port 2.
Settings > Input: vJoy1 on frontend Port 1; vJoy2 on Port 2.
Keep sensitivity 1.0, deadzone 0.0, Analog to Digital Type = None.
B / RetroPad B: fire. Start: start. Select: coin.
These physical Wiimote names assume your established vJoy mapping.
All games alternate players; this does not add simultaneous co-op.

CUSTOM SUPPORTED ROM SETS
  galaga.zip    Galaga (Namco rev. B)           absolute X
  galaxian.zip  Galaxian (Namco set 1)          absolute X
  galaga3.zip   Galaga 3 (GP3 rev. D / Gaplus)  absolute X and Y
  galaga88.zip  Galaga '88                     absolute X
Keep the ROM archives intact. These are the exact sets you supplied.
The reduced build also includes related stock drivers; they do not get
custom aiming patches. Clones/revisions outside this list are unvalidated.
The original ROM ZIPs remain untouched. ROMs are not included.
Space Invaders is retired from the recommended list following your trail/collision
test. Its v2 code remains in the subset, unchanged and not fixed by this release.

CHEATS SUBMENU
Quick Menu > Core Options > Cheats:
  Extra Ships (only in games with native multiple ships)
  Infinite Lives
  Invincibility
All options default to Disabled. Save a Game Options File if you want
separate defaults for each game.
If options appear flat, enable Core Option Categories in RetroArch.
The core uses the libretro core-options v2 category interface.

Extra Ships (number of additional ships; your main fighter is not counted):
  Galaga: Disabled or 1 (native double fighter).
  Galaga '88: Disabled, 1 or 2 (native dual/triple fighter).
  Galaga 3 / Gaplus: Disabled or 1-6 captured enemy escorts.
  Galaxian: option omitted; no native multiple-ship mode.
Changing the Gaplus count rebuilds the escort formation during active play.
The X mapping uses the game's current formation limits directly; the v2
extra restriction has been removed. Large fleets still occupy more width,
so the native movement span is narrower than with a single fighter.
Existing partners/escorts can remain after disabling the option; their
normal loss rules continue. This is a game upgrade, not player 2's ship.
Infinite Lives retains/restores reserve ships while allowing normal deaths.
Invincibility blocks collision damage via the native collision routine or
invulnerability timer. Capture and other special game sequences remain.
After disabling a timer-based cheat, its native grace period can persist.

GALAGA '88
After coin/start, select single/dual with the D-pad and press Fire to begin.
Scripted intro/capture sequences retain native movement until playable.

FINAL PLAY CHECK
Try Gaplus with 1 and 6 extras, move to both horizontal limits, then switch
back to 1. Check both X and Y, shooting, start/coin and player-two turns.
Classic restores native speed-limited controls.

VALIDATION / LIMITS
The Linux native build was tested against the supplied ROMs with real
emulated frames, plus selected RAM fixtures for active-player routing.
V3 automated runs pass every numeric ship-count choice, including 6-to-1
Gaplus changes and both native X endpoints. Tests also cover the Cheats
category/labels, axis endpoints/intermediate points,
held position, independent player-2 aim, native upgrades and protected play.
Galaga's original movement, firing, death/respawn, capture, double fighter,
cheat toggles and 12,000-frame survival regressions are also retained.
The Windows x64 DLL is cross-compiled from the same source. Architecture,
exports and runtime imports are checked, but live Windows/Wiimote testing
is yours. Later stages/cocktail display flipping need further play testing.

SOURCE / REBUILD
Base: https://github.com/finalburnneo/FBNeo
Commit: 63c4190785cadd5ff84483399375871ed6e98754
Complete modified src is in source/source.tar.gz.
From src/burner/libretro:
  make SUBSET=galaga_ir generate-files
  make SUBSET=galaga_ir -j6
For Windows: use clean objects, platform=win and an x86_64 MinGW compiler.
The subset statically links compiler/thread runtimes.
See source/upstream-to-v2.patch and source/v2-to-v3.patch for the two
sequential patches, and tests/ for implementation/validation.
Retain upstream licensing and attribution; see LICENSE.txt.

REFERENCES FOR PATCH RESEARCH
https://github.com/ScottTunstall/Galaxian
https://computerarcheology.com/Arcade/SpaceInvaders/Code.html
https://github.com/finalburnneo/FBNeo-cheats
Only native game behavior and in-memory emulator patches are used.
