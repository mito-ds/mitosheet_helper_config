# mitosheet_helper_config

This package is used to configure the mitosheet, mitosheet2, and mitosheet3 packages. 
It should only be used with a valid Mito Enterprise liscence. 

# Release to test pypi
Delete the dist folder, and the .egg-info folder
Bump the version in setup.cfg and pyproject.toml
Run `python3 -m build`
Run `python3 -m twine upload --repository testpypi dist/*`