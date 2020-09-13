from distutils.core import setup
setup(
    name='aybapi',   # Chose the same as "name"
    version='1.0.5',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='The official Python AYB API wrapper',
    author='Matthew Stead',                   # Type in your name
    author_email='matievisthekat@iplync.org',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/AdvertiseYourBot/ayb-api.py',
    # I explain this later on
    download_url='https://github.com/AdvertiseYourBot/ayb-api.py/archive/v1.0.5.tar.gz',
    # Keywords that define your package best
    keywords=['ayb', 'api', 'advertiseyourbot'],
    packages=["aybapi", "aybapi.impl", "aybapi.base", "aybapi.utils"],
    install_requires=["requests", "typing"],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
