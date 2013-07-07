from setuptools import setup, find_packages


setup(name='django-websettings',
      version='0.0.1',
      description="Django application to provide a web interface "
                  "to set a yet another django's settings",
      classifiers=[
        "Programming Language :: Python",
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
)
