import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()


setuptools.setup(
        name='sphinx_abcnotation',
        author='stfwn',
        author_email='hi@stfwn.com',
        description='A abc directive for Sphinx',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/stfwn/sphinx_abcnotation',
        scripts=['sphinx_abcnotation.py'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        version='0.4')
