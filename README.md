# macOS 27 Skin for VS Code

macOS-faithful color themes (dark, light, and a translucent dark variant), an
SF-Symbol-style file icon theme, and a matching product icon theme.

---

## 1. Install the extension

Copy this folder into your VS Code extensions directory, then restart VS Code:

- macOS / Linux: `~/.vscode/extensions/macos-27-skin`
- Windows: `%USERPROFILE%\.vscode\extensions\macos-27-skin`

## 2. Activate the three themes

Installing alone changes nothing — each theme has to be selected. Open the
Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run:

| Command | Pick |
|---|---|
| Preferences: Color Theme | **macOS Dark**, **macOS Light**, or **macOS Dark Vibrancy** |
| Preferences: File Icon Theme | **macOS SF-Style Icons** |
| Preferences: Product Icon Theme | **macOS SF-Style Product Icons** |

Or set all three at once in `settings.json`:

```json
"workbench.colorTheme": "macOS Dark",
"workbench.iconTheme": "macos-sf-icons",
"workbench.productIconTheme": "macos-sf-product-icons"
```

---

## Required plugin — translucency only

The **macOS Dark Vibrancy** theme is the only piece that needs an external
extension. VS Code windows are opaque by default, so a color theme cannot show
the desktop through the sidebar on its own.

1. Install **Vibrancy Continued** — `illixion.vscode-vibrancy-continued`
   (Extensions view -> search "Vibrancy Continued", or
   `code --install-extension illixion.vscode-vibrancy-continued`).
2. Add to `settings.json`:

```json
"workbench.colorTheme": "macOS Dark Vibrancy",
"vscode_vibrancy.type": "sidebar",
"vscode_vibrancy.opacity": -1
```

3. Run **Reload Vibrancy** from the Command Palette. VS Code will warn that the
   installation is corrupt — this is expected; Vibrancy patches the app shell.
   Click the gear on the notification and choose "Don't Show Again".
4. Re-run **Reload Vibrancy** after every VS Code update, or the effect is lost.

The Vibrancy theme's title bar, activity bar, sidebar, tabs, and panel use alpha
backgrounds so the blur shows through; editor content stays near-opaque for
readability. Without the extension it simply renders like standard macOS Dark.

macOS only. On Windows/Linux, Vibrancy Continued offers acrylic effects but
results vary — use **macOS Dark** there.

---

## Recommended settings

Optional, but the skin was designed against these:

```json
"window.titleBarStyle": "custom",
"window.commandCenter": false,
"editor.fontFamily": "SF Mono, Menlo, monospace",
"editor.fontSize": 13,
"editor.lineHeight": 20,
"workbench.tree.indent": 12,
"workbench.editor.tabSizing": "shrink",
"breadcrumbs.enabled": false
```

`window.titleBarStyle: "custom"` is what lets the theme color the title bar.
With `"native"` the title bar stays system-gray and Vibrancy will not work.

### Auto light/dark switching

```json
"window.autoDetectColorScheme": true,
"workbench.preferredDarkColorTheme": "macOS Dark",
"workbench.preferredLightColorTheme": "macOS Light"
```

---

## Customizing

- **Syntax colors** — replace the `tokenColors` array in
  `themes/macos-dark.json` / `macos-light.json`.
- **Product icons** — 54 glyphs at `U+E001`–`U+E036` cover 96 VS Code icon ids;
  anything not overridden falls back to the stock set. Source artwork is in
  `producticons/svg/` (24pt grid, 1.5pt stroke) and is outlined into
  `sficons.ttf`. Edit an SVG there to redraw a glyph.
- **File icons** — add or swap SVGs in `fileicons/icons/` and map them in
  `fileicons/icon-theme.json`.

No Apple fonts or assets are redistributed; all glyphs are drawn from scratch.

## Troubleshooting

- **Icons didn't change** — the file and product icon themes are separate
  settings from the color theme. Both must be selected.
- **Title bar is the wrong color** — set `"window.titleBarStyle": "custom"` and
  restart (not just reload).
- **Vibrancy stopped working** — re-run **Reload Vibrancy** after a VS Code
  update.
- **Theme not listed** — the folder must sit directly in `.vscode/extensions/`
  with `package.json` at its root, then VS Code fully restarted.
