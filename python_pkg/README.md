# Example Package

## Step 1. Install package

- Go to the top-level directory of this repo (where `setup.py` is located):

    `cd ./`

- Install package by:

    `pip install ./` (recommended)
    (`pip install -e ./` for editable package)
    OR
    `python setup install`

**NOTE: The package will be installed under the name `ymaotest`, which is specified in `setup.py`. However, the actual package to import is `mytest`, which is the directory name.**

## Step 2. Test package installation

`python scripts/run_script.py`

