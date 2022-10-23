# Mitosheet Helper Config

This repository is home to the `mitosheet_helper_config` Python package, which is used to configure enterprise installations of the `mitosheet` package. 
Currently, the package allows you to configure the:
- Support email

In the future, enterprises will have many additional configuration options. If you are an enterprise with a specific configuration request, let us know by [opening an issue](https://github.com/mito-ds/monorepo/issues) in the Mito monorepo or sending us an [email](mailto:founders@sagacollab.com). 

This package should only be used with a valid Mito Enterprise liscence Mito. Learn more about Mito Enterprise [here](https://www.trymito.io/plans).

# How it works 

### Background
The `mitosheet_helper_config` package is designed for admins, like you, to set the Mito configuration settings for your entire organization. This configuration system is designed to work seamlessly with the way you deploy Jupyter and Mito to your end users. 

When the `mitosheet_helper_config` package is present in your users' environment, the `mitosheet` package will read the exported MITO_ENTERPRISE_CONFIGURATION dictionary from this package and update the settings accordingly. 


## Instructions

To set configuration settings, you will need to fork this repo, configure the settings, and finally install your modified package into your user's environment. 

### Fork this repository
- Fork this repository
- Edit the `mito_helper_config/mito_config.py` file to set your enterprise settings
- Push these changes to your Github fork

### Ensure the modified settings package is available 

We are going to install this modified package using `pip install`, which means we need to make this package visible to `pip`. There are two easy ways to accomplish this, without revealing any private data:
1. Distribute package directly from your Github fork
2. Deploy this package to a private PyPi mirror

#### Distribute package directly from your Github fork

In this case, **ensure that the `pip install` will have the correct permissions to access this Github repository when it is being run.** This works well if you deploy enviornemnts to users with docker. 

#### Deploy this package to a private PyPi mirror

If users cannot all be given access to this Git repository, another option is to deploy this package to a private PyPi mirror so users can access it. Follow the instructions in `mitosheet_herlper_config/README.md`, just changing the PyPi deploy location to the internal PyPi mirror.

### Adding this config to user enviornments
To deploy this config to the user enviornment, you now only need to `pip install` this modified package. 
1. If you are distributing the package from Github, run the command: `pip install git+<REPO_URL>#egg=mitosheet_helper_config`, where you replace `<REPO_URL>` with the URL of the forked and updated package you created above. **Ensure that the `pip install` will have the correct permissions to access this Github repository when it is being run.**
2. If you are distributing the package from a PyPi mirror, simply run `pip install mitosheet_helper_config`.

#### requirements.txt file

- Distributing from Github: in `requirements.txt`, add a line `git+<REPO_URL>#egg=mitosheet_helper_config`, where you replace `<REPO_URL>` with the URL of your Github fork.
- Ditributing from PyPi mirror: in `requirements.txt`, add a line `mitosheet_helper_config`.

#### Docker

- Distributing from Github: `RUN pip install git+<REPO_URL>#egg=mitosheet_helper_config`, where you replace `<REPO_URL>` with the URL of your Github fork.
- Ditributing from PyPi mirror: `RUN pip install mitosheet_helper_config`

### Testing
If you followed those instructions successfully, the settings should now be applied to Mito. Make sure it worked by:
- Open a Jupyter instance where you use Mito
- Restart your kernel and refresh your browser 
- Create a mitosheet
- Click on the Get Support button in the top right hand corner of Mito
- Make sure that Mito directs you to the email address you configured in the `mitosheet_helper_config` package. 

### Want help?
If you ran into any issues during that process, we're more than happy to help. Send us an [email](mailto:founders@sagacollab.com) and we'll get you sorted.
