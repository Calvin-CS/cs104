.PHONY: build serve publish-web-build deploy

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve --livereload

publish-web-build: build
	git subtree push --prefix _site origin web-build

deploy: publish-web-build
