# Example of conducting unit test for Python

## Step 1. Install package

- Go to the top-level directory of this repo (where `setup.py` is located):

    `cd ./`

- Install package by:

    `pip install ./` (recommended)
    (`pip install -e ./` for editable package)
    OR
    `python setup install`

**NOTE: The package will be installed under the name `ymaotest`, which is specified in `setup.py`. However, the actual package to import is `mytry`, which is the directory name.**

## Step 2. Run unit tests

### Method 1: Python unittest

You can run individual test files:

    `python -m unittest tests/test_math.py`

    (NOTE: do not add "./" in front of the test path!)

Or you can specify a directory of tests:

    `python -m unittest tests`

    (NOTE: `python -m unittest` is equivalent to `python -m unittest discover`)

### Method 2: pytest

    `pytest ./tests -v`  (`-v` for verbose output)

