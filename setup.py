"""Package setup."""
from setuptools import setup
from setuptools import find_packages

version = '2.0.0a0.post2'

setup(
    name='wildcard.lockdown',
    version=version,
    description=(
        'Plone add-on to be able to make your site read-only except for a set '
        'of conditions that can be defined and enabled/disabled.'
    ),
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read() + '\n'
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone :: 6.0',
        'Framework :: Plone :: Addon',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='wildcard security lockdown',
    author='Wildcard Corp',
    author_email='info@wildcardcorp.com',
    url='https://github.com/collective/wildcard.lockdown',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['wildcard'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.11',
    install_requires=[
        'Products.CMFPlone',
        'plone.api',
        'plone.app.registry',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing'
        ]
    },
    entry_points="""
    [plone.autoinclude.plugin]
    target = plone
    """
)
