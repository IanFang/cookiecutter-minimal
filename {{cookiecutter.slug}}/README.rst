{{ cookiecutter.name }}
{{ cookiecutter.name|count * "=" }}


{{ cookiecutter.description }}
{{ cookiecutter.repo_url }}

Usage
-----

Installation
------------
git clone {{ cookiecutter.git_url }}
pip install -e .

Requirements
------------

License
-------

Directory
---------

- **src** Source code directory
- **docs** Package documentation (Sphinx)
- **tests** Unit tests

Authors
-------

`{{ cookiecutter.name }}` was written by `{{ cookiecutter.author }} <{{ cookiecutter.email }}>`_.
