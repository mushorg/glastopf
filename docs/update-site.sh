#!/bin/bash
#Script to update gh-pages

set -e

TMP_REPO=`mktemp -d -t glastopf-site.XXX`
TMP_HTML=`mktemp -d -t glastopf-site.XXX`

git show HEAD:glastopf/__init__.py > source/glastopf_version.py

make html
cp -R build/html/* $TMP_HTML

git clone git@github.com:mushorg/glastopf.git $TMP_REPO
cd $TMP_REPO
git checkout gh-pages
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
cp -R $TMP_HTML/* $TMP_REPO
touch $TMP_REPO/.nojekyll
git add .
git commit -a -m "Site update"
git push origin gh-pages
rm -rf $TMP_REPO
rm -rf $TMP_HTML
