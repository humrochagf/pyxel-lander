ifeq (, $(shell which pyxelpackager))
	PACKAGE_NAME =
else
	PACKAGE_NAME = pyxel-lander-$(shell python -c 'from pyxel_lander import __version__; print(__version__)')
endif

PACKAGE_PARAMS :=
ifeq ($(OS),Windows_NT)
	PACKAGE_PARAMS += -i images/icon.ico
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Darwin)
		PACKAGE_PARAMS += -i images/icon.icns
	endif
endif

# system-wide standard python installation
.PHONY: install
install:
	pip install .

# install development requirements
.PHONY: install.hack
install.hack:
	pip install -r requirements-dev.txt
	pip install -e .

# build pypi package for distribuition
.PHONY: build
build:
	python setup.py sdist
	python setup.py bdist_wheel

# make the executable package
.PHONY: package
package:
ifeq ($(PACKAGE_NAME),)
	$(error "Pyxel must be installed on this environment")
else
	pyxelpackager pyxel-lander.py $(PACKAGE_PARAMS)
	mkdir -p dist/$(PACKAGE_NAME)
	mv dist/pyxel-lander dist/$(PACKAGE_NAME)
	cp README.md dist/$(PACKAGE_NAME)
	cp LICENSE dist/$(PACKAGE_NAME)/LICENSE.txt
	cp images/icon.png dist/$(PACKAGE_NAME)
	cd dist/$(PACKAGE_NAME) && zip ../$(PACKAGE_NAME).zip ./* && cd -
endif

# publish package to the pypi
.PHONY: publish
publish:
	twine upload dist/*

# lint code
.PHONY: lint
lint:
	isort .
	flake8 .

# remove temporary files and artifacts
.PHONY: clean
clean:
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
