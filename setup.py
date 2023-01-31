from setuptools import setup
import io
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = "Package for automating metamask workflows"


setup(name='SeleniumMetamaskAutomation',
      version='0.0.3',
      packages=['selenium_metamask_automation'],
      description="Package for automating metamask workflows",
      keywords="SeleniumMetamask blockchain automate-metamask install-metamask-extension-selenium selenium-metamask metamask-automation",
      install_requires=["selenium>=3.141.0"],
      extras_require = {
        'windows':  ["pywin32"]
      },
      python_requires='>=3.8',
      url='https://github.com/povilas1565/MetamaskAutomation.git',
      homepage='https://github.com/povilas1565/MetamaskAutomation.git',
      author='Povilas1565',
      author_email='paul156551@@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown'

)
