# CS 104 - Introduction to Programming

## Structure

- Markdown pages (`*.md`) for course content
- Shared layout in `_layouts/default.html`
- Styles in `assets/styles.css`

## Deployment (GitHub Pages via `web-build`)

This site deploys only through GitHub Pages using the `web-build` branch.

Published URL:

- https://calvin-cs.github.io/cs104/

### Automatic publish from `main`

On each push to `main`, GitHub Actions will:

1. install Ruby dependencies,
2. run `bundle exec jekyll build`,
3. publish `_site/` to the `web-build` branch.

Workflow file: `.github/workflows/deploy-web-build.yml`

### Required GitHub settings

1. In GitHub, open **Settings > Actions > General**.
2. Under **Workflow permissions**, choose **Read and write permissions**.
3. In **Settings > Pages**, set source to **Deploy from a branch**.
4. Select branch `web-build` and folder `/ (root)`.

### Optional manual publish to `web-build`

If you need to publish manually from your machine:

```powershell
bundle exec jekyll build
git subtree push --prefix _site origin web-build
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
