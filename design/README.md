# design/ — vendored from the monorepo

**Do not edit anything in this folder.** It is a verbatim copy of
`polarizetech/audio-projects` → `tools/design/`, which generates `design.css`
from `tokens.json` via `build_css.py` and enforces the rules in its own
`CLAUDE.md` with `dev_check.py`.

polarize.tech is a separate repository, so the folder is **vendored rather than
linked**. To update it, re-copy from the monorepo — never patch it here:

```
cp ~/Sites/audio-projects/tools/design/{design.css,design.js,tokens.json} design/
cp ~/Sites/audio-projects/tools/design/fonts/*.woff2 design/fonts/
cp ~/Sites/audio-projects/tools/design/icons/*.svg design/icons/
```

`scripts/check_design.py` re-checks this copy against the monorepo's type rules
and fails if the site's own `styles.css` has drifted from them.

Project-specific styling lives in `/styles.css`, which layers on the tokens
defined here and adds nothing this folder already provides.
