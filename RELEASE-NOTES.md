# Wiimote Libretro Custom Cores v1.2.0

**Windows x64 · Wiimote + Lichtknarre/vJoy · RetroArch / RetroBat**

This release consolidates **11 custom Libretro cores** into two binary package layouts and a separate source/development archive. It expands the original v1.0.0 lineup with newer SNES features and additional console/controller experiments while keeping existing FBNeo Shooter filenames compatible.

## Release highlight: two-player SNES Arkanoid 2

**SNES9x Analog Mouse v10** introduces **two-player dual-paddle support for *Arkanoid: Doh It Again* (Arkanoid 2)**, enabling separate Wiimote/vJoy paddle inputs for two players in the supported setup. The v10 series builds on earlier analog-mouse work, including the v9 FPS hybrid developments.

## Newly included / updated

- **SNES9x Analog Mouse v10 Dual Paddle:** new two-player Arkanoid 2 support; supersedes the earlier SNES analog-mouse build.
- **Flycast Hybrid IR v1 (RetroBat):** new hybrid pointer/input core and separately staged optional remaps, crosshair resources and NVRAM tools. Review extras before use.
- **PCSX2 GunCon2 Hybrid v0.9:** new PS2 GunCon2-oriented Libretro core package.
- **VICE x64 Analog Gun:** new Commodore 64 analog-pointer/lightgun development build.
- **FBNeo IR Mouse v5 NeoPong:** updated arcade mouse/paddle/trackball build supplied for the collection.
- **FBNeo Shooter IR v3 Final:** retained under the original `fbneo_shooter_libretro.dll` filename (and matching info file) so previous RetroBat entries continue to resolve.
- Other packaged cores: Beetle PSX IR Gun v1, Beetle Saturn IR Gun v1, FCEUmm IR Gun v1, Genesis Plus GX IR Hybrid v3, and SNES9x IR Gun v2 MACS.

## Downloads

| Asset | Contents |
|---|---|
| `Custom_Cores_v1.2.0.zip` | 11 core DLLs and their `.info` files, grouped by core along with associated material. |
| `Wiimote_Libretro_v1.2.0_Windows_x64.zip` | The same 11 DLLs and info files in installation-oriented `cores/` and `info/` folders, plus documentation, licenses and optional RetroBat/controller resources. |
| `Wiimote_Libretro_v1.2.0_Source.zip` | Historical source material and available patches, supplementary build instructions and development notes. Some v1.2.0 components have partial sources, not full self-contained source trees. |

**Install:** Back up your configuration first. Extract the Windows x64 package to a staging location; copy the needed `cores/*.dll` and matching `info/*.info` files into your active RetroArch installation. **Merge** RetroBat reference entries with your local config rather than overwriting existing `es_systems_*.cfg` files. Review Flycast's optional assets individually.

## Backward compatibility

The finalized release intentionally uses `fbneo_shooter_libretro.dll` / `fbneo_shooter_libretro.info` and the RetroBat identifier **`fbneo_shooter`**, matching **v1.0.0**. The alternative `fbneo_galaga_ir_libretro.dll` filename found in a prior staging build contained an **identical DLL binary**; installing both copies is unnecessary.

## Excluded from v1.2.0

- Midway Zeus — not sufficiently verified for this release.
- xemu / Xbox — not sufficiently verified.
- Opera / 3DO — not sufficiently verified.
- Chihiro — maintained separately in its own repository.

## Testing and known caveats

These files were collated and archive/hash-checked, **not compiled or gameplay-tested during release preparation**. Compatibility depends on RetroArch/RetroBat versions, installed dependencies, Lichtknarre/vJoy configuration, control bindings and game-specific behavior. Especially test the new SNES dual-paddle mode, Flycast, PCSX2 and Commodore 64 locally before describing them as fully verified.

No ROMs or commercial BIOS files are included. Preserve all bundled core licenses and attributions. GitHub's automatic Source code ZIP/TAR archives only snapshot the repository; use the separate **Source** release asset for the provided development materials.

Thanks to the upstream emulator and Libretro teams, contributors, and everyone testing Wiimote-based lightgun and hybrid controller workflows. 💚
