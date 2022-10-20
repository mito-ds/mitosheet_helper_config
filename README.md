# Mitosheet Helper Config

This repository is home to the `mitosheet_helper_config` Python package, which is used to configure enterprise installations of the `mitosheet` package. 
Currently, the package allows you to configure the:
- Support email

In the future, enterprises will have many additional configuration options. If you are an enterprise with a specific configuration request, let us know by [opening an issue](https://github.com/mito-ds/monorepo/issues) in the Mito monorepo or sending us an [email](mailto:founders@sagacollab.com). 

This package should only be used with a valid Mito Enterprise liscence or written consent from Mito. Learn more about Mito Enterprise [here](https://www.trymito.io/plans).

# How it works 
The `mitosheet_helper_config` package is designed for admins to set the Mito configuration settings for their entire organization. To do so: 
- Clone this repository
- Navigate to the `mito_config.py` file and follow the instructions to set your enterprise settings
- Upload the repository to your organization's GitHub

Now that you've chosen your configuration options, the last step is to make the `mitosheet_helper_config` package accessible to the `mitosheet` pacakge. 

### Docker Deployment
If you're using Docker to deploy mitosheet to your users, follow these instructions:
- Retrieve the git clone URL of the configured `mitosheet_helper_config` package that you just uploaded to your organization's GitHub. 
    - It shoud look something like this: `https://github.com/mito-ds/mitosheet_helper_config.git`. 
- Add this command to your Docker file: `RUN pip install git+<REPO_URL>#egg=mitosheet_helper_config`. 
    - Make sure to fill in the `<REPO_URL>` with the git clone URL you just collected. 
    - The final command should look something like this: `RUN pip install git+https://github.com/mito-ds/mitosheet_helper_config.git#egg=mitosheet_helper_config`
- Rebuild the base Docker image

### Repository clone
If your users clone a repository to create their Jupyter / Mito environment, follow these instructions:
[TODO] add these instructions 

# For development 
This package is only uploaded to pypi and testpypi as a placeholder. 

### Development 
To get started developing the mitosheet_config_helper package, follow these instructions:
- python3 -m venv venv;
- source venv/bin/activate;
- pip install -e ".[dev]"

### Release to PyPi
- python3 -m venv venv;
- source venv/bin/activate;
- Delete the dist folder, and the .egg-info folder
- Bump the version in setup.cfg and pyproject.toml
- python3 -m build
- twine upload dist/*


###  Release to Test PyPi
- python3 -m venv venv;
- source venv/bin/activate;
- Delete the dist folder, and the .egg-info folder
- Bump the version in setup.cfg and pyproject.toml
- pip install build twine
- python3 -m build
- python3 -m twine upload --repository testpypi dist/*



