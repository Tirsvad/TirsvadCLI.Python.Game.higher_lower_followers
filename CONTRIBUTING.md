# Contributing

If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great way
to learn more about social coding on GitJub, new technologies and their ecosystems and how to make constructive, helpful
bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

The following is a set of guidelines for contributing to TirsvadCLI projects which are hosted in the [TirsvadCLI Organization](https://github.com/TirsvadCLI) on GitHub..

## Code style name convention

We are using pep 8 standard to make sure we follow the same code style and name conventions.

# Development

This document describes the process for running this application on your local computer.

## Getting started

It runs on macOS, Windows, and Linux environments.

You'll need python to run the files. To install Python [download the installer from python.org](https://www.python.org/downloads/)

Once you've installed Python (which includes the `pip` package manager), open Terminal and run the following:

Linux
```shell
git clone https://github.com/TirsvadCLI/Python.Game.higher_lower_x_account_follower
cd Python.Game.higher_lower_x_account_follower
python3 -m venv .venv
source .venv\Scripts\activate
pip3 freeze > unins ; pip3 uninstall -y -r unins ; rm unins
pip3 install -r _requirements.txt
```

Windows command prompt
```shell
git clone https://github.com/TirsvadCLI/Python.Game.higher_lower_x_account_follower
cd Python.Game.higher_lower_x_account_follower
python3 -m venv .venv
.venv\Scripts\activate
pip freeze > unins && pip uninstall -y -r unins && del unins
pip install -r _requirements.txt
```

