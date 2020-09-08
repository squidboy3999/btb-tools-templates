from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ['Jinja2', ]

test_requirements = ['pytest', ]

setup(
    name='btb-tools-templates',
    packages=find_packages(include=['btb_tools_templates']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='0.0.1',
)
