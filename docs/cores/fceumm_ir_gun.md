# Nintendo - NES / Famicom (FCEUmm IR Gun) — public v1.0.0

Absolute left-stick Zapper aim with internally routed gamepad controls. Ordinary NES Zapper wiring only; excludes VS and Famicom expansion gun wiring.

Select **Wiimote IR Zapper + Gamepad** on frontend Port 1; mapped port 1. Port 2 may remain Auto or None. Internally the core supplies a gamepad on NES port 1 and Zapper on NES port 2. B shoots, A supplies the away/offscreen trigger, Plus/Minus supply gamepad Start/Select, and D-pad supplies menu movement. Both gun actions also share the corresponding NES gamepad buttons. Native devices remain available. No second independent Zapper or Four Score support is claimed for the hybrid mode. Duck Hunt was reported working by Ron; this is not a complete NES gun game compatibility survey.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/fceumm_ir_gun/`.
