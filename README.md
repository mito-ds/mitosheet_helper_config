# Mitosheet Helper Config

This repository is home to the `mitosheet_helper_config` Python package, which is used to configure enterprise installations of the `mitosheet` package. 
Currently, the package allows you to configure the:
- Support email

In the future, enterprises will have many additional configuration options. If you are an enterprise with a specific configuration request, let us know by [opening an issue](https://github.com/mito-ds/monorepo/issues) in the Mito monorepo or sending us an [email](mailto:founders@sagacollab.com). 

This package should only be used with a valid Mito Enterprise liscence Mito. Learn more about Mito Enterprise [here](https://www.trymito.io/plans).

# How this package works 

The `mitosheet_helper_config` package is designed for admins to set the Mito configuration settings for your entire organization. This configuration system is designed to work seamlessly, no matter how you deliver Jupyter/Mito to your end users. 

When the `mitosheet_helper_config` package is present in your users' environment, the `mitosheet` package will read the exported MITO_ENTERPRISE_CONFIGURATION dictionary from this package and update the settings accordingly. 

# Instructions for Admins

If you wish to deploy a custom Mito configuration to your users, follow the steps below. 

## 1. Fork this repository

- Fork this repository on Github
- Edit the `mito_helper_config/mito_config.py` file to set your enterprise settings
- Push these changes to your Github fork

## 2. Make the modified config available to users 

This package can be made available through a private PyPi mirror, or directly from Github. In either case, this package shoudl be installable as a simple `pip install`. 

### Deploy this package to a private PyPi mirror

If you run a PyPi mirror to distribute packages to your users, follow the deploy instructions in `DEPLOY.md`.

After doing this, the `mitosheet_herlper_config` can be deployed to user enviornments like any other package. Simply add `mitosheet_herlper_config` to `requirements.txt` file, or install it into a docker image like any other pip package.

### Distribute package directly from your Github fork

Another option is just `pip install`ing directly from Github. This works if all users have access to this Github repository, or if you are distributing a docker image that has access to this repository.

If you are distributing the package from Github, run the command: `pip install git+<REPO_URL>#egg=mitosheet_helper_config`, where you replace `<REPO_URL>` with the URL of the forked and updated package you created above. **Ensure that the `pip install` will have the correct permissions to access this Github repository when it is being run.**

## 3. Verify deployment worked
If you followed those instructions successfully, the settings should now be applied to Mito. Make sure it worked by:
- Open a Jupyter instance where you use Mito
- Restart your kernel and refresh your browser 
- Create a mitosheet
- Click on the Get Support button in the top right hand corner of Mito
- Make sure that Mito directs you to the email address you configured in the `mitosheet_helper_config` package. 

# Want help?
If you ran into any issues during that process, we're more than happy to help. If you have a Mito Enterprise license, you're probably talking to us already, so just shoot us an email, and we'll get you sorted.
