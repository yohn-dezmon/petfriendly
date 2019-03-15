try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Test Project',
    'author': 'John Desmond',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'johndesmond631@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'testproject'
}

setup(**config)
