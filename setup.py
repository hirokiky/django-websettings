import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='django-websettings',
      version='0.1',
      description="Django application to provide a web interface "
                  "to set a yet another django's settings",
      long_description=README,
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Hiroki KIYOHARA',
      author_email='hirokiky@gmail.com',
      url='https://github.com/hirokiky/django-websettings',
      keywords='web wsgi django',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django>=1.5',
      ],
      test_suite='runtest.main',
)
