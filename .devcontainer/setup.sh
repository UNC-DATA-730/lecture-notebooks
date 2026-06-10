#!/usr/bin/env bash
set -euxo pipefail

# Install pixi via its official script. The binary lands in ~/.pixi/bin; add it
# to PATH for this non-interactive script (the installer's .bashrc edit only
# affects future interactive shells).
curl -fsSL https://pixi.sh/install.sh | bash
export PATH="$HOME/.pixi/bin:$PATH"

# The universal Codespaces image provides the JupyterLab frontend. pixi provides
# the Python and R kernels (the scientific stack), built from the committed lock.
pixi install --locked

# Register both kernels into the user's Jupyter. The kernelspecs carry absolute
# paths into .pixi/envs/default, so the image's JupyterLab launches them directly
# (no PATH activation or shell-hook needed).
pixi run python -m ipykernel install --user --name python3 --display-name "Python 3 (pixi)"
pixi run R -e 'IRkernel::installspec(user = TRUE, displayname = "R (pixi)")'
