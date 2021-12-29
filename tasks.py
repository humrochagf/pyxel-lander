import itertools
import platform
import shutil
import zipfile
from pathlib import Path

from invoke import task

ROOTDIR = Path(__file__).parent.resolve()
PLATFORM_NAME = platform.system().lower().replace("darwin", "osx")


@task
def clean(c):
    print("Cleaning project...")

    cleaning_generator = itertools.chain(
        ROOTDIR.rglob("*.py[co]"),
        ROOTDIR.rglob("*~"),
        ROOTDIR.rglob("*.egg-info"),
        ROOTDIR.rglob("*.pyxapp"),
        ROOTDIR.rglob(".coverage"),
        ROOTDIR.rglob("__pycache__"),
        ROOTDIR.rglob("dist"),
        ROOTDIR.rglob("build"),
    )

    for path in cleaning_generator:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()

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

    package_name = f"pyxel-lander-{PLATFORM_NAME}"

    code_dir = ROOTDIR / "pyxel_lander"
    dist_dir = ROOTDIR / "dist"
    package_dir = dist_dir / package_name

    c.run(f"pyxel package {code_dir} __main__.py")

    package_dir.mkdir(parents=True, exist_ok=True)

    shutil.move(str(ROOTDIR / "pyxel_lander.pyxapp"), str(package_dir))
    shutil.copy(str(ROOTDIR / "README.md"), str(package_dir))
    shutil.copy(str(ROOTDIR / "LICENSE"), str(package_dir / "LICENSE.txt"))
    shutil.copy(str(ROOTDIR / "images" / "icon.png"), str(package_dir))

    with zipfile.ZipFile(dist_dir / f"{package_name}.zip", "w") as fp:
        for file in package_dir.iterdir():
            fp.write(file, f"pyxel-lander/{file.name}")

    print("Packaging done!")
