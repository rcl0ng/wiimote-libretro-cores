FCEUmm IR Gun v1 - NES Wiimote Zapper + Gamepad (Windows x64)

INSTALL
Close RetroArch and EmulationStation/RetroBat. Copy cores/fceumm_ir_gun_libretro.dll into RetroArch's cores directory, and info/fceumm_ir_gun_libretro.info into its info directory. This is a separate core filename; stock FCEUmm remains available.

RETROBAT
The retrobat-configs folder contains updated es_systems_nes.cfg and es_systems main.cfg from your supplied files. Replace the corresponding original files in your EmulationStation configuration directory (use es_systems main.cfg, not the uploaded copy's '(2)' suffix). Both NES/libretro core lists now contain fceumm_ir_gun; other systems and existing custom cores are retained. XML validated. Your es_settings.cfg does not need an edit to list the core; its current Mednafen NES default is retained. Choose libretro + fceumm_ir_gun in the game's advanced emulator settings for the games you want to test. Restart RetroBat after copying.

FIRST TEST: DUCK HUNT
Settings > Input > Port 1 Controls: Device Index vJoy 1, Analog to Digital Type None, sensitivity 1.0, deadzone 0.0. Keep Disable Left Analog in Menu enabled.
Quick Menu > Controls > Port 1 Controls:
  Device Type: Wiimote IR Zapper + Gamepad
  Mapped Port: 1
Port 2 can remain Auto or None; the hybrid choice handles both physical NES ports internally. Remove old remaps which redirect frontend Port 1 into Port 2. Save a GAME remap after setting it up.

INTERNAL ROUTING
Frontend Port 1 supplies a NES gamepad on physical console port 1 and a Zapper on physical console port 2. No duplicate vJoy binding is required. The hybrid mode reserves both console ports and disables Four Score/Famicom expansion adapters. It is intended for ordinary NES Zapper games, not VS arcade-specific gun wiring or Famicom expansion guns.

CONTROLS (YOUR EXISTING VJOY PROFILE)
Left stick = direct absolute aim. No smoothing or accumulated movement.
Wiimote B / RetroPad B = Zapper trigger; also normal NES gamepad B.
Wiimote A / RetroPad A = away/offscreen trigger; also NES gamepad A.
+ / RetroPad Start = gamepad Start.
- / RetroPad Select = gamepad Select; your RetroArch hotkey remains available.
D-pad = normal gamepad D-pad.
Home = not used by this custom code; available for your frontend hotkey.

No Zapper aiming-mode core option is required. Native Zapper Mode options do not select the IR source. The new mode uses normal emulated light detection, independent of native mouse/touchscreen/sequential-target selection. Standard native device types remain available when leaving the hybrid mode.
Aim is mapped to the currently visible NES frame, respecting overscan crops. A sends the Zapper's native away-trigger bit and offscreen coordinates. Start and Select stay gamepad signals; the Zapper has no dedicated Start/Select buttons.

VALIDATION
Linux native and Windows x64 builds passed. Integration harness uses actual emulator controller setup and input polling with assertions enabled. Passed both bitmask and individual-button polling, full-frame and cropped-frame endpoints, 1000 stationary aim frames, trigger/away/release, gamepad Start/Select/A/B, frontend assignment order and restoration of native controller choices. A generated diagnostic NROM program booted, ran and reset with the hybrid selected BEFORE content load. DLL libretro exports and imports checked; dependencies KERNEL32.dll and msvcrt.dll only. ZIP integrity checked.
Actual Duck Hunt, Wild Gunman and hybrid-game gameplay still needs your Windows playtest. Test menu Start/Select, aiming edges, B shots and A away shots first.

SOURCE
Complete source, patch and tests included. No game ROMs or BIOS included.
Build native: make -f Makefile.libretro -j4
Cross-build after clean: make -f Makefile.libretro platform=win CC=x86_64-w64-mingw32-gcc -j4
Upstream commit recorded in upstream-commit.txt.
