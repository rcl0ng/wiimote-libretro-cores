# Nintendo - SNES / SFC (Snes9x Analog Mouse) — public v1.0.0

Game-specific cursor and paddle position tracking plus optional Doom/Wolfenstein 3-D motion-based FPS controls. Exact ROM revisions required for profiles; other games use general tracking.

For cursor/paddle games choose **SNES Mouse** on the game's mouse port. Core Options: **Mouse Input = Left Analog (Position Tracking)**, **Analog Mouse Game Profiles = Automatic**, **Analog Mouse Select Clutch = Disabled**. B is left click; A is right click. Minus is then available for frontend use.

| Exact profile | CRC32 | Coverage |
|---|---|---|
| Mario Paint Japan/USA | 38c9626c | Hand/cursor reference; Fly Swatter reported successful |
| Arkanoid: Doh It Again USA | b50503a0 | P1 gameplay paddle; reported successful after profile fix |
| Lemmings 2 USA | df7200c8 | Cursor and changing limits; reported successful |
| Super Solitaire USA | c8e80d55 | Cursor; reported successful |
| Vegas Stakes USA | 03a0e935 | Active mouse cursor; developer checks only |
| Might and Magic III USA | 8af25e7e | Active mouse cursor; developer checks only |

Other revisions/games fall back to general relative tracking; they do **not** receive these game-specific fixes. Unsupported Arkanoid P2 modes use general input. Dialogue or gameplay can intentionally stop a cursor. This is not universal absolute-position mouse support.

For **Doom USA (09e85ea6)** or **Wolfenstein 3-D USA (6582a8f5)**, enable **FPS Hybrid Controls = Automatic (Doom / Wolf3D)**. Frontend Port 1 may stay RetroPad; the core handles its internal input routing. Start turning sensitivity at 1x; Ron found Doom more usable at 4x. Turning follows horizontal Wiimote motion and stops when held still, even off-center. Vertical motion is unused. D-pad Up/Down walks, Left/Right strafes; B fires/confirms, A uses doors, 1 changes weapon, 2 runs, Plus invokes the game's menu/map behavior. Minus is reserved for the frontend and is not an FPS command; Doom map access through Minus is not provided. Doom remains less polished than Wolf3D. Disable FPS Hybrid for cursor/paddle games. Legacy development guides record detailed profile research.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/snes9x_analog_mouse/`.
