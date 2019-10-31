# Example Python Package Template

## Basic steps
### Step 1. Install package

- Go to the root-level directory (where `setup.py` is located):

    `cd ./`

- Install package by:

    `pip install ./` (preferred)
    (`pip install -e ./` for editable package)
    OR
    `python setup install`

**NOTE: The package will be installed under the name `ymaotest`, which is specified in `setup.py`. However, the actual package to import is `mytest`, which is the directory name.**

### Step 2. Test package installation

`python exmaples/run_script.py`

## Some notes

1. The template uses *explicit import* for importing modules (this is recommended by PEP8).

2. In `setup.py`, `packages=setuptools.find_packages(include=['moduleA', 'moduleA.*'])` specifies to *only* install moduleA. Therefore moduleB is not installed. This can be useful when there are multiple subdirectories under the root directory that are not package code.

3. *With* installation, `examples/run_script.py` can be placed and run anywhere. *Without* installation, `examples/run_script.py` has to be moved to the root directory, and must be run from the root directory in order for the importing to work.

