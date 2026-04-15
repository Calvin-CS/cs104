# CS 104 - Introduction to Programming

## Structure

- Markdown pages (`*.md`) for course content
- Shared layout in `_layouts/default.html`
- Styles in `assets/styles.css`

## Deployment (cs106-style)

This repo now uses the same branch pattern as `Calvin-Data-Science/cs106`: the built static site is published to a dedicated branch named `web-build`.

### Automatic publish from `main`

On each push to `main`, GitHub Actions will:

1. install Ruby dependencies,
2. run `bundle exec jekyll build`,
3. publish `_site/` to the `web-build` branch.

Workflow file: `.github/workflows/deploy-web-build.yml`

### Repository settings

1. In GitHub, open **Settings > Actions > General**.
2. Under **Workflow permissions**, choose **Read and write permissions**.
3. Save.

### Hooking into `cs.calvin.edu`

Use the `web-build` branch as the deploy source, matching the cs106 pattern.

- If your `cs.calvin.edu` process pulls from a branch, point it to `web-build`.
- If your process expects a GitHub Pages branch, set Pages to deploy from `web-build` (root).

#### Step 2: switch the `cs.calvin.edu` working copy to `web-build`

Run these on the server where the site is pulled/deployed:

```bash
cd /path/to/cs104/site/repo
git fetch origin
git checkout -B web-build origin/web-build
git branch --set-upstream-to=origin/web-build web-build
git pull
```

After this, your deploy-side repo tracks `origin/web-build`, so future pulls use the built site.

If your deploy script runs a pull command, use:

```bash
git pull origin web-build
```

### Optional: local manual publish to `web-build`

If you need to publish manually from your machine:

```powershell
bundle exec jekyll build
git subtree push --prefix _site origin web-build
```

### Step 3: one-command local deploy target

A `Makefile` is included so you can deploy to `web-build` with one command:

```bash
make deploy
```

Useful targets:

- `make build` -> build `_site/`
- `make serve` -> run local server with live reload
- `make publish-web-build` -> push built `_site/` to `web-build`
- `make deploy` -> alias for `publish-web-build`

If `make` is not installed on Windows, use the manual PowerShell commands above.

For a one-command Windows deploy, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy_web_build.ps1
```

## Preview Locally (Without Deploying)

1. Install Ruby (with DevKit on Windows) so `ruby` and `bundle` are available in your terminal.
2. Install dependencies from this repository root:

	```powershell
	bundle install
	```

3. Start the local site server:

	```powershell
	bundle exec jekyll serve --livereload
	```

4. Open `http://127.0.0.1:4000` in your browser.
