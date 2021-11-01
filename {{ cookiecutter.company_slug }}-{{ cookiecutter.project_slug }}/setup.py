from re import search

from setuptools import setup, find_packages

with open(
    "src/{{ cookiecutter.company_slug }}/{{ cookiecutter.project_slug }}}}/__init__.py",
    "rt",
    encoding="utf8",
) as f:
    version = search(r"__version__ = \"(.*?)\"", f.read()).group(1)

requires = []

requires_dev = [
    "black~=21.10b0",
    "isort~=5.9.3",
    "pre-commit~=2.15.0",
]

setup(
    name="{{ cookiecutter.company_name }} {{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version=version,
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.repo_url }}",
    packages=[
        "{{ cookiecutter.company_slug }}." + pkg
        for pkg in find_packages(where="src/{{ cookiecutter.company_slug }}")
    ],
    package_dir={"": "src"},
    install_requires=requires,
    extras_require={"dev": requires_dev},
)
