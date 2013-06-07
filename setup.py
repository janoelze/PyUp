from setuptools import setup

setup(
    name='PyUp',
    version='1.0',
    packages=['PyUp'],
    url='http://github.com/janoelze/PyUp',
    author='Jan Oelze',
    author_email='jan@codein.is',
    description="PyUp automatically uploads screenshots to imgur.com and adds the image-URL the clipboard.",
    scripts=[
        'PyUp/bin/pyup',
    ],
    install_requires=[
        "manage.py",
    ]
)
