This README will help you develop or deploy the `mitosheet_helper_config` package.

## Background 
The `mitosheet_helper_config` package is developped using setuptools.

## Development 
To get started developing the mitosheet_config_helper package:

### On Linux / Mac
Run this command:

``` 
bash dev/macsetup.sh
```

### On Windows
Run these commands:
```
python3 -m venv venv
venv\Scripts\activate.bat
pip install -e ".[dev]"
```

### Linking this package with the mitosheet package
When developing the `mitosheet_helper_config` package, you'll want to link it with the `mitosheet` package for testing. To do so, 
go to the `mitosheet` pacakge and run the following commands to pip install the `mitosheet_helper_config` package from your local repo. 
```
cd <to the home directory of the mitosheet_helper_config repo>
pip install -e .
```

When you make edits to the `mitosheet_helper_config` pacakge, just restart the kernel launched in the `mitosheet` package, and the changes will take effect. 

## Testing
There are three types of tests that we want to run while developing this package: pytest tests, mypy tests and integration tests.

### Pytest tests
To run the pytest tests, run the command:
```
pytest tests/  mitosheet_helper_config/mito_config.py
```
This executes all of the tests in the `tests/` folder, as well as the test in `mito_config.py` which is used to communicate to the admin not to change the version of MITO_ENTERPRISE_CONFIGURATION.

### MyPY tests
To run MyPy tests, run this command:
```
mypy mitosheet_helper_config/ --ignore-missing-imports --disallow-untyped-calls --disallow-incomplete-def
```

### Integration tests
To run integration tests, link this package with the `mitosheet` package and: 
- test that all configuration options work.
- test that all configuration options work correctly when there is no MITO_ENTERPRISE_CONFIGURATION
- test that old versions of the MITO_ENTERPRISE_CONFIGURATION are handled properly.

## Release
Since we intend for enterprise admins to use this package by cloning it from this repo, releasing this package just entails merging into main. 

### Release to main
Before releasing to main, make sure that all CI tests pass, you've followed the testing procedure listed above, and you've followed the release procedure detailed in by technical process. 

### Release on PyPi
We released this package to PyPi and TestPyPi only as placeholders so someone else does not claim this package name. 

If for some reason you do want to release this package to PyPi or TestPyPi, follow these instructions:

- python3 -m venv venv;
- source venv/bin/activate;
- pip install -e ".[dev]"
- Delete the dist folder, and the .egg-info folder
- Bump the version in setup.cfg and pyproject.toml
- python3 -m build

To release on PyPi:
- twine upload dist/*
To release on TestPyPi:
- python3 -m twine upload --repository testpypi dist/*
