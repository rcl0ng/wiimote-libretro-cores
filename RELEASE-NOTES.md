# v1.0.0 — Windows x64

First public packaging of Ron (rclong)'s tested custom cores. Eight Wiimote/vJoy cores: NES, SNES gun, selected SNES mouse profiles, Genesis/Sega CD/Master System, PSX, Saturn, FBNeo mouse and FBNeo shooters.

Standalone RetroArch is the primary setup; RetroBat integration is optional. The package includes modified source, patches, component licenses, info files, vJoy autoconfig and a consolidated RetroBat reference main config. No commercial games or Chihiro/Xbox BIOS are included.

Wiimote input requires Lichtknarre/vJoy, the supplied button mapping and dinput setup. Enable Disable Left Analog in Menu. Missile Command fires its three silos with D-pad Left/Down/Right. For SNES mouse, set Mouse Input to Left Analog (Position Tracking) in Core Options as well as choosing the SNES Mouse device. Chihiro: Vulkan is strongly recommended; use a fresh process for each game. See the per-core guides for exact titles/revisions and limits, including SNES T2 multiplayer and unsupported mouse profiles.

Ron reported all cores passed testing on 2026-10-07. DLLs are unchanged from the accepted RC2. Packaging/source checks passed; no fresh Windows rebuild or universal compatibility certification is claimed. Historical embedded version names remain. fbneo_galaga_ir is distributed as fbneo_shooter. Mixed upstream licenses remain applicable; noncommercial components are not relicensed.
