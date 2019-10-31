import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ymaotest",
    version="0.0.1",
    author="Yixin Mao",
    author_email="yixinmao@uw.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(include=['moduleA', 'moduleA.*']),  # this only installs things under moduleA
#    scripts=['scripts/run_script'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
