FROM quay.io/jupyter/minimal-notebook:afe30f0c9ad8

# copy the conda.lock file into the Docker image a build time
COPY conda-linux-64.lock /tmp/conda-linux-64.lock

# install the packages in conda-linux-64.lock in your Docker image
RUN mamba update --quiet --file /tmp/conda-linux-64.lock \
    && mamba clean --all -y -f \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"
