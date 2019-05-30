class: middle, center

# Creating and using conda packages

Ryan Dale (ryan.dale@nih.gov)

---

## Conda

- Sort of a cross-platform version of PyPI/CRAN/CPAN/apt/homebrew for Windows,
  macOS, and Linux.

- Creates **reproducible, isolated environments** (similar to virtual environments)

- Not limited to just Python. There are conda packages for C, C++, Java, Perl, R, Go,
  Haskell, Rust, etc etc.


---

## Conda packages

- A conda **package** is a tarball that is unzipped into an isolated directory.

- One or more conda packages unzipped into the same isolated directory creates
  an **environment**.

- An environment must be **activated** to be used, which effectively prepends its
  `bin/` dir to the `$PATH`. Deactivating it removes the directory from the path.

---


---

## Conda recipes

- Specifies the dependencies and installation commands

- Typically a `meta.yaml` file and a `build.sh` script.

- Real-world example: [requests recipe on conda-forge](https://github.com/conda-forge/requests-feedstock/blob/master/recipe/meta.yaml)



## Using conda

- [install miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [conda on biowulf](https://hpc.nih.gov/apps/python.html#envs)

Create an environment, activate, and deactivate when done:

```bash
conda create -n my-env \
    requests \
    ipython \
    pandas \
    matplotlib \
    r-base \
    r-ggplot2

# prepends to path:
conda activate my-env

# when done:
conda deactivate
```
---

## Specifying versions

Install specific versions:

```bash
conda create -n py2 "python=2"
```

Install versions with constraints:

```bash
conda create -n py2 "python<3"
```

On 2019-05-30, this wants to install py27:

```bash
conda create -n pandas "pandas<=0.18.0"
```

In general, it's better to specify as much as you know:

```bash
conda create -n pandas "pandas<=0.18.0" "python=3"
```
---

# Specify versions in requirements file

Use a requirements.txt:

```text
# this is requirements.txt
pandas <=0.18.0
python =3
```

```bash
conda create -n pandas --file requirements.txt
```
---

## Specify version in a YAML environment file (recommended)

A yaml file can specify the channels and their order.

**Note:** use `conda env create` rather than `conda create`:

```bash
conda env create -n pandas --file env.yaml
```
YAML file:

```yaml
# this is env.yaml
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - blas=2.10=openblas
  - bzip2=1.0.6=h14c3975_1002
  - ca-certificates=2019.3.9=hecc5488_0
  - certifi=2018.8.24=py35_1001
  - libblas=3.8.0=10_openblas
  - libcblas=3.8.0=10_openblas
  - libffi=3.2.1=he1b5a44_1006
  - libgcc-ng=8.2.0=hdf63c60_1
  - libgfortran-ng=7.3.0=hdf63c60_0
  - liblapack=3.8.0=10_openblas
  - liblapacke=3.8.0=10_openblas
  - libopenblas=0.3.3=h5a2b251_3
  - libstdcxx-ng=8.2.0=hdf63c60_1
  - ncurses=6.1=hf484d3e_1002
  - numpy=1.11.3=py35h99e49ec_10
  - numpy-base=1.11.3=py35h2f8d375_10
  - openblas=0.3.6=h6e990d7_2
  - openssl=1.0.2r=h14c3975_0
  - pandas=0.17.1=np111py35_0
  - pip=18.0=py35_1001
  - python=3.5.5=h5001a0f_2
  - python-dateutil=2.8.0=py_0
  - pytz=2019.1=py_0
  - readline=7.0=hf8c457e_1001
  - setuptools=40.4.3=py35_0
  - six=1.11.0=py35_1
  - sqlite=3.28.0=h8b20d00_0
  - tk=8.6.9=h84994c4_1001
  - wheel=0.32.0=py35_1000
  - xz=5.2.4=h14c3975_1001
  - zlib=1.2.11=h14c3975_1004
```
---

## Create the YAML file from an existing environment

Get a YAML file from your (possibly-interactively-defined) environment with:

```bash
conda env export -n pandas > env.yaml
```

---

## Be super explicit by specifying URLs

**NOTE:** this is now platform specific! But it's fast since the solver doesn't need to run.

```bash
conda list --explicit > spec-file.txt
```

```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: linux-64
@EXPLICIT
https://conda.anaconda.org/conda-forge/linux-64/ca-certificates-2019.3.9-hecc5488_0.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/libgcc-ng-8.2.0-hdf63c60_1.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/libgfortran-ng-7.3.0-hdf63c60_0.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/libstdcxx-ng-8.2.0-hdf63c60_1.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/bzip2-1.0.6-h14c3975_1002.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/libffi-3.2.1-he1b5a44_1006.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/libopenblas-0.3.3-h5a2b251_3.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/ncurses-6.1-hf484d3e_1002.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/openblas-0.3.6-h6e990d7_2.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/openssl-1.0.2r-h14c3975_0.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/xz-5.2.4-h14c3975_1001.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/zlib-1.2.11-h14c3975_1004.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/libblas-3.8.0-10_openblas.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/readline-7.0-hf8c457e_1001.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/tk-8.6.9-h84994c4_1001.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/libcblas-3.8.0-10_openblas.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/liblapack-3.8.0-10_openblas.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/sqlite-3.28.0-h8b20d00_0.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/liblapacke-3.8.0-10_openblas.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/python-3.5.5-h5001a0f_2.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/blas-2.10-openblas.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/certifi-2018.8.24-py35_1001.tar.bz2
https://conda.anaconda.org/conda-forge/noarch/pytz-2019.1-py_0.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/six-1.11.0-py35_1.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/numpy-base-1.11.3-py35h2f8d375_10.tar.bz2
https://conda.anaconda.org/conda-forge/noarch/python-dateutil-2.8.0-py_0.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/setuptools-40.4.3-py35_0.tar.bz2
https://repo.anaconda.com/pkgs/main/linux-64/numpy-1.11.3-py35h99e49ec_10.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/wheel-0.32.0-py35_1000.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/pandas-0.17.1-np111py35_0.tar.bz2
https://conda.anaconda.org/conda-forge/linux-64/pip-18.0-py35_1001.tar.bz2
```
---


## Shared environments

In a shared directory use `-p` to specify the path (typically in the top-level
working directory of a projects) so others can activate the same environment:

```bash
conda env create -p ./env --file env.yaml
```

```bash
conda activate ./env
```
---


## Channels

A **channel** is a repository of packages.

- [conda-forge docs](http://conda-forge.org/docs/)
- [bioconda](https://bioconda.github.io/)

Bioconda and conda-forge coordinate global pinnings **to ensure ABI
compatibility** across packages in both channels.

This is not guaranteed (or even likely) using other arbitrary channels.

- [setting up bioconda and conda-forge channels](https://bioconda.github.io/index.html#using-bioconda). Order is very important.
- [conda-forge's global pinning](https://github.com/conda-forge/conda-forge-pinning-feedstock/blob/master/recipe/conda_build_config.yaml)

```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

---

# Anatomy of a package

Often contains `bin/`, `lib/` top-level directories that are unpacked into the environment.

Also contains the exact recipe that was used to create the package, which is useful for inspection/debugging.

- [samtools package](https://anaconda.org/bioconda/samtools/0.1.19/download/linux-64/samtools-0.1.19-h94a8ba4_6.tar.bz2), an example C package. Has a corresponding [recipe in bioconda](https://github.com/bioconda/bioconda-recipes/tree/master/recipes/samtools)
- [requests package](https://anaconda.org/conda-forge/requests/2.22.0/download/linux-64/requests-2.22.0-py37_0.tar.bz2), an example Python package. Has a corresponding [recipe in conda-forge](https://github.com/conda-forge/requests-feedstock/tree/master/recipe)
- Overview of the [conda build process](https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html)
- conda-forge's [list of feedstocks](https://github.com/conda-forge/feedstocks/tree/master/feedstocks)

---

# Conda skeleton

If a package is on PyPI, try using the `conda skeleton` tool:

```bash
conda skeleton pypi <packagename>
```

Or a package is on CRAN:

```bash
conda skeleton cran <packagename>
```

---

## pydeface case study

Chosen because John had [forked it at some
point](https://github.com/leej3/pydeface) and Dylan [has a bunch of commits
there](https://github.com/poldracklab/pydeface/commits?author=Shotgunosine).

Packaging is hard. Be prepared to fix subtle issues and get into the weeds of
debugging a project.

---

## conda skeleton

Try skeleton:

```bash
conda skeleton pypi pydeface
# ImportError: Missing dependencies: ['numpy', 'nibabel', 'nipype']

# (not sure why...they're specified in setup.py)
```

Ok, try manually creating a meta.yaml by using an existing Python recipe as a template . . .

---


```yaml
# pydeface/meta.yaml
package:
  name: pydeface
  version: 1.1.0

source:
  url: https://github.com/poldracklab/pydeface/archive/v1.1.0.tar.gz
  sha256: 6ef4044828821e0a7d26242b41220ee8287b8f660a8259e82fb13ee6bb3bd70c

build:
  number: 1
  script: "{{ PYTHON }} -m pip install . --no-deps --ignore-installed -vv "

requirements:
  host:
    - python
  build:
  run:
    - python
    - numpy
    - nibabel
    - nipype

test:
  imports:
    - pydeface

  commands:
    - pydeface

about:
  home: https://github.com/poldracklab/pydeface
  summary: defacing utility for MRI images
  license: MIT
```

---

## Try building with that meta.yaml

```bash
conda build ./pydeface
```

Missing dependency?

```
pkg_resources.DistributionNotFound: The 'pydot>=1.2.3' distribution was not found and is required by nipype
Tests failed for pydeface-1.1.0-py37_1.tar.bz2 - moving package to /home/dalerr/miniconda3/envs/cb/conda-bld/broken
WARNING:conda_build.build:Tests failed for pydeface-1.1.0-py37_1.tar.bz2 - moving package to /home/dalerr/miniconda3/envs/cb/conda-bld/broken
TESTS FAILED: pydeface-1.1.0-py37_1.tar.bz2
```

- Does nipype not list pydot as a dependency? Check its recipe: https://anaconda.org/conda-forge/nipype/files
- It specifies `pydotplus`, but not `pydot`

---

## Modify meta.yaml

- Try adding `pydot` to the `pydeface` recipe dependencies, and re-build:

```yaml
...
  run:
    - python
    - numpy
    - nibabel
    - nipype
    - pydot
...
```

```bash
conda build ./pydeface
```

---

## Another error

```
+ pydeface
usage: pydeface [-h] [--outfile path] [--force] [--applyto  [...]]
                [--cost mutualinfo] [--template path] [--facemask path]
                [--nocleanup] [--verbose]
                path
pydeface: error: the following arguments are required: path
------------
pydeface 2.0
------------
Tests failed for pydeface-1.1.0-py37_1.tar.bz2 - moving package to /home/dalerr/miniconda3/envs/cb/conda-bld/broken
WARNING:conda_build.build:Tests failed for pydeface-1.1.0-py37_1.tar.bz2 - moving package to /home/dalerr/miniconda3/envs/cb/conda-bld/broken
TESTS FAILED: pydeface-1.1.0-py37_1.tar.bz2
```
---

## Modify test

Easily fixed, add `-h` to the `pydeface` call:

```yaml
...
  commands:
    - pydeface -h
```

```bash
conda build ./pydeface
```

Hooray! Sucessful locally-built package, ready for a PR to conda-forge or bioconda.

---

## Better testing

Would be better to more fully test, using the freshly-built package by
specifying the build directory as a channel (might as well add ipython for help with debugging):


```bash
conda create -n pydeface-test pydeface ipython --channel /home/dalerr/miniconda3/envs/cb/conda-bld/
```

Another debugging option:

```bash
conda debug <path-to-built-package>
```

---

## Import and inspect


```bash
conda activate pydeface-test
```

```python
from pydeface import utils
utils.initial_checks()
```

```ipython
~/miniconda3/envs/pydeface/lib/python3.7/site-packages/pydeface/utils.py in initial_checks(template, facemask)
     21
     22     if 'FSLDIR' not in os.environ:
---> 23         raise Exception("FSL must be installed and "
     24                         "FSLDIR environment variable must be defined.")
     25         sys.exit(2)

Exception: FSL must be installed and FSLDIR environment variable must be defined.
```

Can't redistribute FSL according to [the license](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence).

I gave up when I had to register to download FSL...

---

# Being kind to packagers


- **Releases**: If your code is on github, create a tagged release which GitHub will
automatically zip up and provide:

```bash
git tag -a v1.2 -m "version 1.2"
git push --tags
```

`conda-build` allows pointing to git repos at specific commits, but this is
strongly discouraged by conda-forge and bioconda.

- **Semantic versioning:**

    - major versions have breaking changes
    - minor versions have new features
    - point versions are bugfixes

- **Specify all dependencies** e.g., in `setup.py` for Python packages.

- **Include a license**, allow redistribution if possible.

- **Try installing your package on a new machine**, write down all the steps
  required. This can find things like hidden dependencies, hard-coded paths,
  etc
