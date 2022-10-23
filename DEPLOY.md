# Deploy `mitosheet_helper_config` to a PyPi mirror

If you are an admin that wants to deploy this package to a private PyPi mirror to distribute to your users, follow these instructions. Run the commands:

```
python3 -m venv venv;
source venv/bin/activate;
pip install -e ".[dev]"
```

Then, bump the version in in setup.cfg and pyproject.toml, and run:
```
python3 -m build
```

Finally, release to PyPi with the command:
```
twine upload dist/ <CUSTOM PYPI FLAGS>
```

You can see the custom flags for uploading to a private PyPI mirror [here](https://twine.readthedocs.io/en/stable/), but generally you need to add the URL of private PyPi mirror, and auth information for this repository.
