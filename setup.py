from setuptools import setup, find_packages

version = '0.1'

setup(
    name='upiqsite.opip',
    version=version,
    description='Policy product for Teamspace for projects.oregon-pip.org',
    long_description=(
        open("README.rst").read(),
        ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Sean Upton',
    author_email='sean.upton@hsc.utah.edu',
    url='https://github.com/upiq',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['upiqsite'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'uu.projectsite',
        'Products.CMFPlone',
        'plone.browserlayer',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )

