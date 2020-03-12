PROJECT = "sobol"

current-version:
	@echo "Current version is `cat ${PROJECT}/__init__.py | awk -F '("|")' '{ print($$2)}'`"

git-release:
	git add ${PROJECT}/__init__.py
	git commit -m "Bumped version to `cat ${PROJECT}/__init__.py | awk -F '("|")' '{ print($$2)}'`"
	git tag `cat ${PROJECT}/__init__.py | awk -F '("|")' '{ print($$2)}'`
	git push
	git push --tags

pypi-build :
	rm -rf build/ dist/
	python3 setup.py sdist bdist_wheel

pypi-upload :
	python3 -m twine upload dist/*