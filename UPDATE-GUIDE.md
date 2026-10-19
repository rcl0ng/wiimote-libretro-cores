# Repository maintenance update for v1.2.0

## What this overlay changes

Updates `docs/`, `info/`, `licenses/`, `development/`, `retrobat/`, and root documentation (`RELEASE-NOTES.md`, `SOURCES.md`, `SOURCE-LICENSE-INDEX.md`, `INSTALL-RETROARCH.md`, `CREDITS-LICENSES.md`). Also includes the existing `autoconfig/dinput/vJoy Device.cfg` for reference.

**`README.md` is intentionally excluded**, because the maintainer already updated it online. This ZIP contains **no DLLs** and does not change the published release downloads.

## Applying to GitHub

1. Download this ZIP and extract it locally.
2. Review changed files before uploading, especially any license and RetroBat material.
3. Open the repository's **Code** tab, select **Add file → Upload files**, and drag the *contents* of the extracted overlay, keeping relative folder paths. GitHub's web interface may require uploading folders via drag-and-drop; if it flattens the paths, use Git or GitHub Desktop instead.
4. Review the changed-file listing: do not replace your updated root `README.md`.
5. Commit directly to `main` with a message such as `docs: sync v1.2.0 repository support files`.
6. Check the rendered `docs/cores/snes9x_analog_mouse.md`, `info/`, `licenses/`, `development/`, `retrobat/INSTALL.md` and `SOURCE-LICENSE-INDEX.md` in GitHub.
7. Keep the existing v1.2.0 tag and three published ZIP assets untouched; this update is documentation, metadata and reference material, not a new binary release.

## Important caveats

- The repository's current `main` branch could not be downloaded as a whole during preparation; this package is based on the **previously assembled v1.2.0 release assets** and the public repository listing. Review the GitHub diff before committing, and do not overwrite more recent manual edits.
- `retrobat/reference-configs/es_systems_main.cfg` is a *historical, machine-specific example* with potentially unrelated custom entries; **do not copy it over a live RetroBat file**. New system registration lines are supplied as isolated optional snippets instead.
- XML parse result for packaged main reference: `True`.
- Full upstream source trees are not duplicated here: use the separately published Source ZIP.
