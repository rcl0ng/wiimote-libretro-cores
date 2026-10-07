# Wiimote / vJoy custom libretro cores — v1.0.0

Windows x64 community builds maintained/tested by Ron (rclong), with AI-assisted development. Eight separate custom cores provide left-stick gun inputs, selected SNES mouse profiles, arcade pointing and game-specific ship/paddle patches. Use the Lichtknarre → vJoy pipeline documented in `docs/INPUT-SETUP.md`; the exact matching RetroArch autoconfig is included. Chihiro and its converter are distributed as a separate project.

## Install

**Start with [INSTALL-RETROARCH.md](INSTALL-RETROARCH.md). Standalone RetroArch is the primary setup; RetroBat integration is entirely optional.**

Close RetroArch. Copy `cores` contents into the configured Core directory and `info` contents into the configured Core Info directory. Back up existing custom files. Install the shared `autoconfig/dinput/vJoy Device.cfg`, configure Lichtknarre buttons to match, and **enable Disable Left Analog in Menu**. Read the per-core guide in `docs/cores` before selecting device types. For RetroBat follow `retrobat/INSTALL.md`; reference XML files are optional, version-specific examples, not an automatic installer.

All DLL names are retained except `fbneo_galaga_ir`, now renamed to `fbneo_shooter`. Existing shooter users must select the new core and update per-game core assignments; old filename-based options/remaps may need migration. Keep backups. Its embedded development core name can still say Galaga IR because the binary was not rebuilt. Public version is 1.0.0 v1.0.0; internal DLL build strings retain the original tested revisions. All ROMs, BIOS and save data must be supplied by the user. Stock cores remain available. Exact supported sets/revisions and known limitations are in the per-core guides.

## Core guides

- [Nintendo - NES / Famicom (FCEUmm IR Gun)](docs/cores/fceumm_ir_gun.md)
- [Nintendo - SNES / SFC (Snes9x IR Gun)](docs/cores/snes9x_ir_gun.md)
- [Nintendo - SNES / SFC (Snes9x Analog Mouse)](docs/cores/snes9x_analog_mouse.md)
- [Sega - MS/GG/MD/CD (Genesis Plus GX IR Gun)](docs/cores/genesis_plus_gx_analog.md)
- [Sony - PlayStation (Beetle PSX IR Gun)](docs/cores/beetle_psx_ir_gun.md)
- [Sega - Saturn (Beetle Saturn IR Gun)](docs/cores/beetle_saturn_ir_gun.md)
- [Arcade - FBNeo (IR Mouse)](docs/cores/fbneo_mouse.md)
- [Arcade - FBNeo (IR Shooters)](docs/cores/fbneo_shooter.md)

## Source, licenses and validation

`development/<core>` preserves full modified source archives, upstream notices, patches and historical tests/build instructions. Those historical documents retain old version labels; current docs take precedence for installation and compatibility status. This bundle has mixed upstream licenses, including non-commercial restrictions: retain each component's license and do not apply one blanket license. It is a free community release, not an official Libretro/RetroBat product. See `docs/RELEASE-VERIFICATION.md` for verification scope.

## Downloads and setup

Get the complete Windows package, including modified source and licenses, from [Releases](../../releases/latest). For SNES mouse, select SNES Mouse in Quick Menu Controls and **Mouse Input = Left Analog (Position Tracking)** in Core Options. Chihiro users: **Vulkan is the recommended backend**. RetroBat remains optional.
