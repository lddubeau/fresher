try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name = "fresher",
    version = "0.2-ldd1",
    description = "Clone of the Cucumber BDD framework for Python",
    author = "Roman Lisagor",
    author_email = "rlisagor+fresher@gmail.com",
    url = "http://github.com/rlisagor/fresher",
    license = "GPL",
    packages = ["fresher", "fresher.test"],
    package_data = {'fresher': ['languages.yml']},
    install_requires = ['pyparsing>=1.5.0', 'PyYAML', 'nose>=0.11.1'],
    entry_points = {
        'nose.plugins.0.10': [
            'fresher = fresher.noseplugin:FresherNosePlugin',
            'freshererr = fresher.noseplugin:FresherErrorPlugin'
        ],
        'console_scripts': [
            'fresher-list = fresher.commands:list_steps',
        ],
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ]
)
