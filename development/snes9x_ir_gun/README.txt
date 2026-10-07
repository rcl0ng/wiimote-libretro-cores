Snes9x IR Gun v2 - M.A.C.S. Rifle addition (Windows x64)

Replace the existing snes9x_ir_gun_libretro.dll and .info. Core basename is unchanged; no RetroBat system-list edits are needed.
New input choice: Quick Menu > Controls > Port 1 Controls > Device Type > Wiimote IR M.A.C.S. Rifle + Gamepad.
Set frontend Port 1 to vJoy 1 and Mapped Port 1. The core internally places a gamepad on SNES console port 1 and the M.A.C.S. rifle on console port 2. Left analog X/Y provide absolute screen aim; Wiimote B (RetroPad B) is the rifle trigger. The first Wiimote's RetroPad buttons also provide gamepad controls.

Super Scope and Justifier input choices are retained. See README-v1.txt for their controls and independent two-gun setup. The SNES analog mouse custom core remains separate.

Validation: native Linux build passed; input tests passed rifle coordinate endpoints and trigger press/release, plus Scope turbo and independent Justifier input regression checks. Windows x64 DLL verified for libretro exports and dependencies. The supplied M.A.C.S. Basic Rifle Marksmanship ROM booted; trigger advanced through the intro and left-stick inputs moved the crosshair to independent requested positions on the shooting range. Full scoring and calibration behavior still require gameplay testing.

Source.tar.gz contains complete source. v1-to-v2.patch shows the rifle addition. No ROMs or BIOS are included.
