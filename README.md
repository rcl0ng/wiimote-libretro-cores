Wiimote / vJoy Custom Libretro Cores
Release v1.2.0 — Windows x64
Custom Libretro cores and configuration resources for Wiimote lightgun, analog-pointer, mouse, paddle, and hybrid controller setups using Lichtknarre + vJoy, RetroArch, and RetroBat.
Download the latest GitHub release · All releases
What's new in v1.2.0
SNES9x Analog Mouse v10 adds two-player paddle support for Arkanoid: Doh It Again (Arkanoid 2), building on the prior FPS-hybrid work.
Adds the Flycast Hybrid IR v1 RetroBat package for Dreamcast/Naomi workflows.
Adds the PCSX2 GunCon2 Hybrid v0.9 core for PS2 gun-controller experimentation.
Adds the VICE x64 Analog Gun core for Commodore 64 pointer/lightgun experiments.
Consolidates updated custom cores, optional controller resources, and RetroBat reference configurations into one v1.2.0 distribution.
Backward compatibility: the FBNeo Shooter DLL retains its v1.0.0 name, `fbneo_shooter_libretro.dll`. Existing RetroBat references using `fbneo_shooter` do not need changing.
For changes, limitations, and upgrade guidance, see v1.2.0 release notes.
Download packages
Release asset	Purpose
`Custom_Cores_v1.2.0.zip`	Same 11 core DLLs and associated `.info` files, organized in individual core folders.
`Wiimote_Libretro_v1.2.0_Windows_x64.zip`	Unified RetroArch-style `cores/` and `info/` directories, documentation and optional configuration resources.
`Wiimote_Libretro_v1.2.0_Source.zip`	Development/source materials, patches, historical upstream trees and build references. Some newer cores have partial source/patch sets, not fully reproducible standalone source trees.
GitHub's automatically generated Source code archives are repository snapshots and are not substitutes for the separately uploaded Source ZIP.
Included cores
Core DLL	System / use	Packaged build
`beetle_psx_ir_gun_libretro.dll`	PlayStation pointer / lightgun hybrid	IR Gun v1
`beetle_saturn_ir_gun_libretro.dll`	Sega Saturn pointer / lightgun hybrid	IR Gun v1
`fceumm_ir_gun_libretro.dll`	NES Wiimote lightgun	IR Gun v1
`genesis_plus_gx_analog_libretro.dll`	Master System / Genesis pointer hybrid	IR Hybrid v3
`snes9x_ir_gun_libretro.dll`	SNES lightgun	IR Gun v2 MACS
`snes9x_analog_mouse_libretro.dll`	SNES mouse, paddle and selected hybrid control modes	Analog Mouse v10 Dual Paddle
`fbneo_mouse_libretro.dll`	Arcade mouse / paddle / trackball	IR Mouse v5 NeoPong
`fbneo_shooter_libretro.dll`	FBNeo Galaga-family IR shooter controls	Shooter IR v3 Final (original compatible filename)
`flycast_hybrid_ir_libretro.dll`	Dreamcast / Naomi hybrid IR	v1 RetroBat
`pcee2_analog_gun_libretro.dll`	PS2 GunCon2 hybrid	v0.9
`vice_x64_analog_gun_libretro.dll`	Commodore 64 analog gun	Supplied C64 build
The packages contain 11 core DLLs. Individual game compatibility and player count vary; consult core-specific notes and test on your own configuration. Inclusion is not a guarantee of gameplay verification.
Not included: Midway Zeus, xemu, Opera/3DO, or Chihiro. These remain outside this release; Chihiro has its own repository.
Requirements
64-bit Windows and a compatible RetroArch / RetroBat setup.
Wiimotes connected through the user's preferred Bluetooth arrangement.
Lichtknarre and configured vJoy virtual devices; any necessary HIDHide routing should be configured for the local system.
ROMs/game data and BIOS/firmware obtained separately where required. No commercial game ROMs or proprietary BIOS files are included.
Installation and upgrading
Back up your current RetroArch `cores/`, `info/`, remaps, game-specific settings, and RetroBat configuration files.
Download `Wiimote_Libretro_v1.2.0_Windows_x64.zip` and extract it to a staging folder, not straight over a running installation.
Copy the desired DLLs from `cores/` to the RetroArch core directory used by your RetroBat setup.
Copy their matching `.info` files from `info/` to the RetroArch core-info directory.
Review `retrobat/reference-configs/` and `retrobat/optional-reference/` for examples only. Merge the relevant `<core>` entries into your installed `es_systems_*.cfg` files rather than replacing those files wholesale.
Configure Lichtknarre → vJoy player assignment and the corresponding RetroArch input/remaps. Check that Player 1 and Player 2 use the intended devices.
If installing Flycast extras, inspect `optional/flycast/` first; remaps, crosshairs, and NVRAM import resources may overwrite current game settings if used indiscriminately.
Launch a known working game and test aim, trigger, reload, menu controls, coin/start, and both-player behavior where applicable. Keep your backups until satisfied.
Important FBNeo naming note
`fbneo_shooter_libretro.dll` is the same binary that previously appeared under the alternate name `fbneo_galaga_ir_libretro.dll` in an early v1.2.0 staging package. Its SHA-256 matches the v1.0.0 Shooter DLL. The final release intentionally uses the original v1.0.0 filename and `fbneo_shooter` RetroBat identifier, preserving existing references. Do not install both filenames as separate copies of this same core.
Known limitations and scope
These packages were assembled from supplied development archives, not freshly compiled and gameplay-tested as part of this release packaging pass.
Flycast, PS2, and C64 behavior depends on emulator build, core settings, device ordering and target game.
Some optional RetroBat references are examples of previous working layouts and may not suit your installed version without merging.
The development package collects what was supplied, but not every newer core has a complete standalone, reproducible source checkout.
Core license terms may differ; preserve and review the bundled notices before redistribution or modification.
License and acknowledgments
Credit belongs to the upstream Libretro, emulator and individual core developers, as well as the custom-input contributors and testers. Each core retains its own upstream license and attribution requirements; see the included `licenses/` directory and source package. Distribution of modifications does not supersede upstream licenses.
Project: https://github.com/rcl0ng/wiimote-libretro-cores
