from setuptools import setup, find_packages

setup(
    name = "django-oembed",
    version = "0.1",
    url = 'http://github.com/myles/django-oembed',
    license = 'BSD',
    description = '',
    author = 'Myles Braithwaite',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
