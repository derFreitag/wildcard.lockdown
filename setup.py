"""Package setup."""

from pathlib import Path
from setuptools import setup

version = "2.0.0a0.post3.dev0"

setup(
    name="wildcard.lockdown",
    version=version,
    description=(
        "Plone add-on to be able to make your site read-only except for a set "
        "of conditions that can be defined and enabled/disabled."
    ),
    long_description=f"{Path('README.md').read_text()}\n{Path('CHANGES.md').read_text()}",
    long_description_content_type="text/markdown",
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    keywords="wildcard security lockdown",
    author="Wildcard Corp",
    author_email="info@wildcardcorp.com",
    url="https://github.com/collective/wildcard.lockdown",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "plone.api",
        "plone.app.registry",
        "plone.registry",
        "Products.CMFPlone",
        "Products.CMFCore",
        "Zope",
        "z3c.form",
    ],
    extras_require={
        "test": ["plone.app.contenttypes", "plone.app.testing", "plone.testing"]
    },
    entry_points="""
    [plone.autoinclude.plugin]
    target = plone
    """,
)
