# Nintendo - SNES / SFC (Snes9x IR Gun) — public v1.0.0

Absolute left-stick Super Scope, Justifier and M.A.C.S. rifle aim with internal gamepad routing. Independent second Justifier. T2 multiplayer is not recommended.

Select **Wiimote IR Super Scope + Gamepad**, **Wiimote IR Justifier + Gamepad**, or **Wiimote IR M.A.C.S. Rifle + Gamepad** on frontend Port 1. The core routes pad to console port 1 and gun to console port 2. For two Justifiers, select **Wiimote IR Justifier (Player 2)** on frontend Port 2. Super Scope is a single-gun device.

B = trigger; A = offscreen aim/reload for Justifier; Plus = Start/Pause and gamepad Start; Minus = gamepad Select; Wiimote 1 = Scope Cursor; Wiimote 2 = Scope Turbo toggle. D-pad feeds the hybrid gamepad. Existing crosshair options still apply.

Lethal Enforcers and earlier Scope testing were reported successful. The MACS addition passed range/trigger tests in the development harness; full scoring is not certified. **T2: The Arcade Game multiplayer is not recommended**: axis sticking was reported in the later trial, which was abandoned in favor of the arcade version. This separate gun core does not include the dedicated SNES mouse core's game-specific tracking fixes.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/snes9x_ir_gun/`.
