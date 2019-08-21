# system-wide standard python installation
install:
	pip install .

# install development requirements
install.hack:
	pip install -r requirements-dev.txt
	pip install -e .

# build linux for distribution
build.linux:
	python setup.py linux --clean -b -s
	zip -r dist/pyxel_lander_linux dist/pyxel_lander_linux

# build mac os for distribution
build.macos:
	python setup.py macos --clean -b -s
	zip -r dist/pyxel_lander_macos dist/pyxel_lander_macos

# build mac os for distribution
build.windows:
	python setup.py windows --clean -b -s
	zip -r dist/pyxel_lander_windows dist/pyxel_lander_windows

# build pypi package for distribuition
build:
	python setup.py sdist
	python setup.py bdist_wheel

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
