# Mitosheet Helper Config

This repository is home to the `mitosheet_helper_config` Python package, which is used to configure enterprise installations of the `mitosheet` package. 
Currently, the package allows you to configure the:
- Support email

In the future, enterprises will have many additional configuration options. If you are an enterprise with a specific configuration request, let us know by [opening an issue](https://github.com/mito-ds/monorepo/issues) in the Mito monorepo or sending us an [email](mailto:founders@sagacollab.com). 

This package should only be used with a valid Mito Enterprise liscence or written consent from Mito. Learn more about Mito Enterprise [here](https://www.trymito.io/plans).

# How it works 

### Background
The `mitosheet_helper_config` package is designed for admins, like you, to set the Mito configuration settings for your entire organization. This configuration system is designed to work seamlessly with the way you deploy Jupyter and Mito to your end users. 

When the `mitosheet_helper_config` package is present in your users' environment, the `mitosheet` package will read the exported MITO_ENTERPRISE_CONFIGURATION dictionary from this package and update the settings accordingly. 

At a high level, to use the `mitosheet_helper_config` settings you will: clone this repo, configure the settings, upload this repo to your org's GitHub, and finally install this package from that GitHub repo during the creation of your user's environment. 


## Instrucitons
To set the Mito configuration settings for your entire organization, follow these instructions:
- Clone this repository
- Navigate to the `mito_config.py` file and follow the instructions to set your enterprise settings
- Upload the repository to your organization's GitHub

Now that you've set your configuration options, the last step is to make the `mitosheet_helper_config` package accessible to the `mitosheet` pacakge. 

### Docker Deployment
If you're using Docker to deploy mitosheet to your users, follow these instructions:
- Retrieve the git clone URL of the configured `mitosheet_helper_config` package that you just uploaded to your organization's GitHub. 
    - It shoud look something like this: `https://github.com/mito-ds/mitosheet_helper_config.git`. 
- Add this command to your Docker file: `RUN pip install git+<REPO_URL>#egg=mitosheet_helper_config`. 
    - Make sure to fill in the `<REPO_URL>` with the git clone URL you just collected. 
    - The final command should look something like this: `RUN pip install git+https://github.com/mito-ds/mitosheet_helper_config.git#egg=mitosheet_helper_config`
- Rebuild the base Docker image

### GitHub Repository Clone
If your users clone a repository to create their Jupyter / Mito environment, follow these instructions:
[TODO add these instructions]

### Testing
If you followed those instructions successfully, the settings should now be applied to Mito. Make sure it worked by:
- Open a Jupyter instance where you use Mito
- Restart your kernel and refresh your browser 
- Create a mitosheet
- Click on the Get Support button in the top right hand corner of Mito
- Make sure that Mito directs you to the email address you configured in the `mitosheet_helper_config` package. 

### Want help?
If you ran into any issues during that process, we're more than happy to help. Send us an [email](mailto:founders@sagacollab.com) and we'll get you sorted.