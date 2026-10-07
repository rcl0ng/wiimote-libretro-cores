# Arcade - FBNeo (IR Shooters) — public v1.0.0

Absolute ship positioning for specific Galaga, Galaxian, Gaplus and Galaga 88 sets. Optional cheats and native extra-ship counts. Alternating players only; Space Invaders is not recommended.

Select **Wiimote IR Ship + Buttons** on Port 1, and on Port 2 for alternating-player turns. B fires, Plus starts, Minus inserts coin. This does not add simultaneous cooperative play.

| Exact set | Position mapping | Additional native ships |
|---|---|---|
| galaga.zip (Namco rev. B) | X | 1 |
| galaxian.zip (Namco set 1) | X | None |
| galaga3.zip (GP3 rev. D / Gaplus) | X/Y | 1–6 escorts |
| galaga88.zip | X | 1–2 |

Core Options → Cheats provides Extra Ships, Infinite Lives and Invincibility; defaults are disabled. Enable Core Option Categories if needed. Extra Ships excludes the main fighter and is offered only where native multi-ship behavior exists. A larger formation naturally has less horizontal travel. Existing partners can persist after disabling the option. Galaga '88: choose single/dual with D-pad, then Fire. Scripted sequences retain native movement.

Galaga and the later shooter work were reported successful; the final Gaplus formation-range and numeric-count revision passed developer tests but its final Windows retest was not explicitly recorded. Include it in RC verification. **Space Invaders is excluded from recommendations** due trail/collision behavior, although its earlier driver code remains. Other clones/revisions do not receive a validated custom mapping. Original ROM files are unchanged.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/fbneo_shooter/`.
