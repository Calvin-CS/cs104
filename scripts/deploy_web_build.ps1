$ErrorActionPreference = "Stop"

Write-Host "Building Jekyll site..."
bundle exec jekyll build

Write-Host "Publishing _site to origin/web-build..."
git subtree push --prefix _site origin web-build

Write-Host "Done. web-build has been updated."
