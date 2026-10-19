Beetle PSX IR Gun v1 - Windows x64, software renderer

INSTALL
Close RetroArch. Copy cores/beetle_psx_ir_gun_libretro.dll into RetroArch's cores directory and info/beetle_psx_ir_gun_libretro.info into its info directory. Restart RetroArch. Load this core directly for the first test. Your normal PS1 regional BIOS and game files are required, including the same BIOS filenames expected by stock Beetle PSX. No games or BIOS included.

SETUP
Settings > Input > Port 1 Controls: Device Index vJoy 1.
Settings > Input > Port 2 Controls: Device Index vJoy 2.
Both: Analog to Digital Type None, sensitivity 1.0, deadzone 0.0. Keep Disable Left Analog in Menu enabled.
Quick Menu > Controls:
  Port 1 Mapped Port 1; Device Type Wiimote IR GunCon or Wiimote IR Justifier.
  Port 2 Mapped Port 2; choose the same gun type for a two-player game.
  For one player, leave Port 2 at None or the game's required ordinary controller.
  Remove old remaps that redirect both inputs into one emulated port.
  Save GAME remaps so games retain their appropriate gun type.
The new choices provide absolute left-stick aim without smoothing or integration, independently for each port. They ignore Gun Input Mode. Normal gun/controller types remain available. Beetle's game controller compatibility profiles remain active; an incompatible game profile can replace a requested gun with a supported ordinary controller.

BUTTONS (YOUR EXISTING VJOY PROFILE)
Both gun types:
  Wiimote B / RetroPad B: trigger.
  Wiimote A / RetroPad A: offscreen shot/reload. Game must support this.
GunCon:
  1 / RetroPad X: GunCon A (Time Crisis cover/action).
  2 / RetroPad Y: GunCon B.
  + / RetroPad Start: also GunCon B, for menu/action convenience.
  GunCon hardware has no separate Start or Select button. A is reserved
  for offscreen reload; hold 1 for cover/action in Time Crisis.
Justifier:
  1 / RetroPad X: auxiliary button.
  + / RetroPad Start: Justifier Start.
  2: unused.
Minus and Home are not given gun actions; use your frontend menu/hotkeys.

CROSSHAIR/CALIBRATION
Quick Menu > Core Options > Input: select a visible Gun Cursor if needed.
Use the game's calibration screen when available. Coordinate conversion follows Beetle's native gun screen-space model and honors NTSC/PAL and overscan crop. Changes to display/crop can require recalibration.

FIRST TESTS
Time Crisis: Wiimote IR GunCon. Check calibration, B shooting, 1 cover/action, A offscreen shot.
Lethal Enforcers I & II: Wiimote IR Justifier. Check + Start, both independent aims, B trigger and A reload.
See PSX_Gun_Types.txt for original-game gun types, dual support and regional notes.

PSX PORT ROUTING
Each frontend gun goes to the corresponding physical PSX controller port. Unlike NES/Genesis, these modes do not synthesize a second gamepad device or take over both ports from one Wiimote. Gun buttons supply menu actions where the game supports them. Games requiring an additional ordinary pad can use the other port if their own port layout allows it. No generic hybrid pad routing is claimed in this first build.

RETROBAT
New core basename: beetle_psx_ir_gun. Add <core>beetle_psx_ir_gun</core> inside the PSX system's libretro <cores> list in each active es_systems configuration before selecting it from RetroBat. This package does not modify your NES configuration files or your PSX defaults. Start directly in RetroArch before any launcher integration changes.

VALIDATION
Native Linux and Windows x64 builds passed with software rendering, interpreter CPU (HAVE_LIGHTREC=0), and CHD support. Input integration tests passed both bitmask settings, pre-content native-device normalization, independent GunCon/Justifier inputs, 1000 frames holding player 2 still while moving player 1, reload/auxiliary/Start, NTSC/PAL/overscan endpoints, switching back to native devices and controller compatibility profiles. Native init/pre-load device selection/deinit smoke passed. Windows exports and imports checked: only KERNEL32.dll and msvcrt.dll. ZIP integrity checked.
No BIOS/gameplay test was possible here with the currently available files. In-game calibration, timing, hits and two-player play remain for your Windows test.

SOURCE/BUILD
Complete source and patch included, based on commit in upstream-commit.txt.
Native: make HAVE_LIGHTREC=0 HAVE_CDROM=0 -j4
Windows after clean: make platform=win HAVE_LIGHTREC=0 HAVE_CDROM=0 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ -j4
