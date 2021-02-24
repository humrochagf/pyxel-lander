ifeq (, $(shell which pyxelpackager))
	package_name =
else
	package_name = pyxel-lander-$(shell python -c 'from pyxel_lander import __version__; print(__version__)')
endif

# system-wide standard python installation
install:
	pip install .

# install development requirements
install.hack:
	pip install -r requirements-dev.txt
	pip install -e .

# build pypi package for distribuition
build:
	python setup.py sdist
	python setup.py bdist_wheel

# make the executable package
package:
ifeq (, $(package_name))
	$(error "Pyxel must be installed on this environment")
else
	pyxelpackager pyxel-lander.py
	mkdir -p dist/$(package_name)
	mv dist/pyxel-lander dist/$(package_name)
	cp README.md dist/$(package_name)
	cp LICENSE dist/$(package_name)/LICENSE.txt
	zip -r dist/$(package_name).zip dist/$(package_name)
endif

# publish package to the pypi
publish:
	twine upload dist/*

# lint code
lint:
	isort --recursive --apply pyxel_lander setup.py
	flake8 pyxel_lander setup.py

# remove temporary files and artifacts
clean:
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
