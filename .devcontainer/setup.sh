#!/usr/bin/env bash
set -euxo pipefail

# mamba is much faster than conda for solving r-base + tidymodels
conda install -n base -c conda-forge -y mamba
mamba env update -y -n base -f environment.yml

# Register both kernels with Jupyter
mamba run -n base python -m ipykernel install --user --name python3 --display-name "Python 3"
mamba run -n base R -e 'IRkernel::installspec(user = TRUE, displayname = "R")'

