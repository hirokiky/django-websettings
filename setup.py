from setuptools import setup, find_packages


setup(name='websettings',
      version='0.0.1',
      description="Django application to provide a web interface "
                  "to set a yet another django's settings",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django>=1.5',
      ],
)
