Genesis Plus GX IR Hybrid v3 - Windows x64

Install: close RetroArch; replace cores/genesis_plus_gx_analog_libretro.dll and info/genesis_plus_gx_analog_libretro.info in the corresponding RetroArch directories. Same core filename as our Analog v2, so existing RetroBat core-list entries still apply. Restart RetroArch.

Settings > Input > Port Controls:
  Frontend Port 1 Device Index = vJoy 1.
  Frontend Port 2 Device Index = vJoy 2.
  Analog to Digital Type None, analog sensitivity 1.0, deadzone 0.0.
  Keep Disable Left Analog in Menu enabled.

Quick Menu > Controls:
  Port 1 Mapped Port 1; Port 2 Mapped Port 2.
  Lethal Enforcers / Lethal Enforcers II (Mega Drive or Sega CD):
    Port 1 Device Type = Wiimote IR Justifier + Gamepad.
    Port 2 Device Type = Wiimote IR Justifier (Player 2).
    For one gun, Port 2 Device Type = Joypad Port Empty.
  Menacer games:
    Port 1 Device Type = Wiimote IR Menacer + Gamepad.
    Port 2 Device Type = Joypad Port Empty.
  Master System Light Phaser games:
    Port 1 Device Type = Wiimote IR Light Phaser.
    Port 2 Device Type = Joypad Port Empty, or Wiimote IR Light Phaser
    for a game supporting a second Phaser.
  Disable old Port 3 gun bindings/remaps. The old three-frontend-port layout
  is replaced by two frontend ports. Save GAME remaps for each controller type.

MD/CD hybrid topology is internal: console port 1 = 3-button gamepad;
console port 2 = Menacer or Justifiers. Wiimote 1 supplies gamepad menu input
and first gun; Wiimote 2 supplies the second Justifier. Do not bind vJoy 1
to both frontend ports or map Port 3 into game Port 2.

New IR Device Type choices always use absolute left-stick coordinates.
Light Gun Input core option now offers native Light Gun / Touchscreen only;
it does not control the Wiimote IR choices. Old left_analog options are ignored.
Analog Gun Reload Button option was removed; IR uses the working v2 A layout.
Show Light Gun Crosshair remains a core option: enable it as desired.

Wiimote controls (existing vJoy profile):
  B: trigger. A: offscreen shot/reload (requires game support).
  1 / RetroPad X: first auxiliary. 2 / RetroPad Y: second auxiliary.
  + / RetroPad Start: gun Start; also gamepad Start in MD/CD hybrid mode.
  - / RetroPad Select: no synthetic gun reload; available for frontend bindings.
  D-pad and normal buttons also feed the hybrid 3-button menu gamepad.
  Home: not consumed by this custom code; available for your frontend hotkey.

Aiming stays direct, with no smoothing or relative-mouse conversion. This
revision changes controller selection and routing; it does not change ROMs,
BIOS requirements or Body Count's previously unresolved gun detection.
The ordinary native input devices remain available. The separate SNES mouse
and gun cores are unchanged.

Validation: Linux and Windows x64 builds passed. Integration harness uses the
actual core input polling and controller configuration code, with assertions
active. Passed both polling paths, menu/gamepad Start plus gun Start,
independent Justifiers, 1000 frames holding gun 2 still while gun 1 moves,
endpoint coordinates, per-player reload/auxiliary, minus without reload,
disabled second gun, Menacer, dual Phaser, disabled first port, switching
back to native joypads and native lightgun input. A generated diagnostic MD
program booted, ran and reset using the native build. DLL exports and imports
checked (KERNEL32.dll, msvcrt.dll only); ZIP integrity verified.
Actual MD/CD/SMS games still need your Windows playtest. Start with two-player
Lethal Enforcers, then Menacer 6-in-1 and a working Master System gun game.

Complete source and v2-to-v3 patch included; no game ROMs or BIOS included.
Upstream base: ekeeke/Genesis-Plus-GX 939ce4f045f981f89965f24780cef045cc5e52d7.
Build native: make -f Makefile.libretro -j4
Cross-build after clean: make -f Makefile.libretro platform=win CC=x86_64-w64-mingw32-gcc HAVE_SYS_PARAM=0 -j4
