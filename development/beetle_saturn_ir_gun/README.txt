BEETLE SATURN IR GUN V1 - WINDOWS X64 TEST BUILD

INSTALL
Copy cores/beetle_saturn_ir_gun_libretro.dll to:
  D:\RetroBatGun\emulators\retroarch\cores\
Copy info/beetle_saturn_ir_gun_libretro.info to RetroArch's configured
Core Info directory (normally emulators/retroarch/info).
Keep your regular Beetle Saturn core installed.

If RetroBat does not list this custom core, its Saturn libretro core list
needs this entry:
  <core>beetle_saturn_ir_gun</core>
This ZIP does not replace your RetroBat XML configuration files.

SETUP FOR VIRTUA COP
1. Load Virtua Cop with this custom core.
2. Settings > Input > RetroPad Binds (or Port Controls):
   frontend Port 1 Device Index = vJoy Device (1).
   frontend Port 2 Device Index = your second vJoy device.
   Choose the actual device names; numbering can differ on your PC.
   Analog to Digital Type = None for both players.
   Keep analog sensitivity 1.0 and deadzone 0.0 for your IR setup.
3. Quick Menu > Controls > Port 1 Controls > Device Type:
   Wiimote IR Gun.
4. For two players, set Port 2 Device Type to Wiimote IR Gun too.
   For one player, Port 2 may be None or an ordinary gamepad.
5. Keep both 6Player Adaptor options disabled for the first test.
6. Quick Menu > Core Options > Gun Crosshair = Cross or Dot.
7. Run the game's gun calibration if offered.
8. Save a Game Remap File once configured.

BUTTONS (USING OUR EXISTING VJOY RETROPAD MAPPING)
Wiimote B / RetroPad B = trigger.
Wiimote A / RetroPad A = offscreen shot/reload.
Wiimote Plus / RetroPad Start = Saturn gun Start.
Left analog X/Y = absolute gun position.
Minus and Home have no gun action assigned by this custom mode.
The core does not assign RetroArch menu/exit hotkeys.

INPUT BEHAVIOR
One frontend device controls one Saturn gun on the corresponding port.
No duplicate vJoy assignment is needed for two-player gun games.
The same Wiimote IR Gun choice works through Saturn's native gun device;
there is no separate Japanese-versus-American gun protocol to select here.
The ordinary Stunner and Virtua Gun choices retain native lightgun input.
Custom IR aiming does not use the native touchscreen/pointer input option,
mouse sensitivity or 3D-pad deadzone settings.
No smoothing or relative-motion accumulation is applied.
The native Saturn reload implementation deliberately generates an offscreen
shot sequence; its short reload behavior is different from aiming latency.
No additional hybrid pad routing has been introduced in this first build.

TEST FIRST
Virtua Cop: aim/calibration, fire, reload and Start.
Then Virtua Cop 2 and two players:
  keep P2 still while moving P1; repeat with players reversed.
Report the exact game and region if it needs different port/menu behavior.

VERIFICATION AND LIMITS
Source-level tests execute both actual input polling paths with mocked
frontend inputs and peripheral binding. They cover per-player independence,
1,000 held-position frames, NTSC/PAL endpoints, trigger/reload/Start,
Minus, native-device restoration and assignments before/after content load.
Full native core init/deinit and pre-content controller assignments passed.
Windows DLL exports and dependencies were checked.
No Saturn BIOS or commercial game was available for local gameplay testing.
Game calibration, hit detection, reload timing and two-player play remain
for your Windows test. This is a first test build, not a gameplay-certified
release.

BUILD/SOURCE
Upstream: https://github.com/libretro/beetle-saturn-libretro
Exact base commit: upstream-commit.txt
Modified source and upstream license: source.tar.gz
Patch: ir-gun.patch
Windows: make platform=win HAVE_CDROM=0
         CC=x86_64-w64-mingw32-gcc-posix
         CXX=x86_64-w64-mingw32-g++-posix
MinGW GCC 13, software renderer, CHD support, statically linked runtimes.
Delete object files before switching between native and Windows builds.
No BIOS or game files are included.
