# system-wide standard python installation
install:
	pip install .

# install development requirements
install.hack:
	pip install -r requirements-dev.txt
	pip install -e .

# build linux for distribution
build.linux:
	python setup.py linux -s -b

# build mac os for distribution
build.macos:
	python setup.py macos -s -b

# build mac os for distribution
build.windows:
	python setup.py windows -s -b

# build pypi package for distribuition
build:
	python setup.py sdist
	python setup.py bdist_wheel

# publish package to the pypi
publish:
	twine upload dist/*

# lint code
lint:
	isort --recursive --apply lander pyxel_lander.py setup.py
	flake8 lander pyxel_lander.py setup.py

# remove temporary files and artifacts
clean:
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
