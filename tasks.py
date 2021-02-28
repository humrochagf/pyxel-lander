import shutil
import zipfile
from pathlib import Path

from invoke import task

from pyxel_lander import __version__


@task
def clean(c):
    print("Cleaning project...")

    c.run("rm -rf *.egg-info dist build")
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")
    c.run("find . -name '.coverage' -exec rm -f {} +")
    c.run("find . -name '__pycache__' -exec rmdir {} +")

    print("Cleaning done!")


@task
def lint(c):
    print("Running isort and flake8...")

    c.run("isort .")
    c.run("black -l 79 .")
    c.run("flake8 .")

    print("Linting done!")


@task(pre=[clean])
def package(c):
    print("Packaging the game...")

    package_name = f"pyxel-lander-{__version__}"

    root_folder = Path(__file__).parent.resolve()
    dist_folder = root_folder / Path("dist")
    package_folder = dist_folder / package_name

    c.run(f"pyxelpackager {root_folder}/pyxel-lander.py")

    package_folder.mkdir(parents=True, exist_ok=True)

    shutil.move(
        str(dist_folder / "pyxel-lander"),
        str(package_folder),
    )
    shutil.copy(
        str(root_folder / "README.md"),
        str(package_folder),
    )
    shutil.copy(
        str(root_folder / "LICENSE"),
        str(package_folder / "LICENSE.txt"),
    )
    shutil.copy(
        str(root_folder / "images" / "icon.png"),
        str(package_folder),
    )

    with zipfile.ZipFile(dist_folder / f"{package_name}.zip", "w") as fp:
        for file in package_folder.iterdir():
            fp.write(file, f"pyxel-lander/{file.name}")

    print("Packaging done!")
