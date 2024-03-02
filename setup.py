from distutils.core import setup
setup(
  name = 'ubcaerodesign',         # How you named your package folder (MyLib)
  packages = ['ubcaerodesign'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='GNU Affero General Public License v3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'PyPi package for networking.py and loggingconfig',   # Give a short description about your library
  author = 'Midora',                   # Type in your name
  author_email = 'midorashiu@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ubcaerodesign/ubcaerodesign',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ubcaerodesign/ubcaerodesign/archive/refs/tags/pypi-0.3.tar.gz',    # I explain this later on
  keywords = ['aerodesign'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'zmq'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)