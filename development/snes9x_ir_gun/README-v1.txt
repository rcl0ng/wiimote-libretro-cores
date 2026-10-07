Snes9x IR Gun - Test v1, Windows x64

Separate from Snes9x Analog Mouse. New core basename: snes9x_ir_gun.
Copy the DLL into RetroArch cores and the .info into info. Load directly through RetroArch for the first test. Frontend registration in RetroBat is a separate installation step.

IMPORTANT: use a new game remap for this core. Avoid the old hybrid duplicate input-port layout. Settings > Input > Port 1 Controls: select the first Wiimote vJoy device. For a second gun, Port 2 Controls: select the second Wiimote vJoy device. Keep Analog to Digital Type None, sensitivity 1.0, deadzone 0.

Quick Menu > Controls > Port 1 Controls > Device Type:
- Wiimote IR Super Scope + Gamepad (Battle Clash, Metal Combat, etc.)
- Wiimote IR Justifier + Gamepad (Lethal Enforcers, etc.)
Both choices read frontend Port 1's left stick for absolute aim and its RetroPad buttons. Internally the SNES has a gamepad in console port 1 and the gun in console port 2.

For two Justifiers: choose Wiimote IR Justifier (Player 2) in Quick Menu > Controls > Port 2 Controls. Leave Mapped Port at 1 for frontend Port 1, and 2 for frontend Port 2. Additional frontend ports should use their own destinations. Save Game Remap File after testing.
Super Scope is a single gun. The Player 2 choice applies only with the first Justifier hybrid choice.

Controls using Ron's existing vJoy mapping:
Left stick: absolute aim, with no velocity integration.
Wiimote B / RetroPad B: trigger.
Wiimote A / RetroPad A: aim offscreen; also fires a reload shot for Justifier.
Wiimote + / RetroPad Start: gun Start/Pause and console gamepad Start.
Wiimote - / RetroPad Select: console gamepad Select.
Wiimote 1 / RetroPad X: Super Scope Cursor.
Wiimote 2 / RetroPad Y: Super Scope Turbo toggle.
D-pad and other RetroPad buttons also feed the console gamepad from the first Wiimote.
Home is not consumed by the custom gun code and can remain your RetroArch hotkey.
Native lightgun and joypad device choices remain available. Gun Input core option is ignored by the new IR choices. Existing cursor appearance options still apply.

Validation: Linux core compiled; Battle Clash booted and ran with IR gun input; isolated routing tests passed endpoints, per-player reload, 1000 held-P2 frames while P1 moved, and turbo rising-edge behavior. Windows x64 cross-build validated. Full gameplay, in-game calibration, and two-player Justifier play require user testing.

Source.tar.gz contains full source; ir-gun.patch contains the changes from the upstream commit recorded in upstream-commit.txt. No game ROMs or BIOS are included.
