

# DoVado

Advanced Computer Architectures (ACA) Research project 2020.   
A CLI tool for RTL Design Space Exploration on top of Vivado.   
&ldquo;Do&rsquo; vado?&rdquo; is an italian slang expression for &ldquo;Dove vado?&rdquo; which means &ldquo;Where do I go?&rdquo;


# State of the Project

Complete prototype.


# How to inspect the project

This project uses [Poetry](https://python-poetry.org/) for managing dependences and python versions in order to avoid conflicting versions on different machines.
Following instructions are tested on a Linux machine but should work on OSX with minor (or none) modifications.


## Install Poetry

(if you already have poetry installed skip to the next section)   
Execute the following command in a shell to install poetry

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

You will find poetry in $HOME/poetry/.bin where $HOME is usually something like *home/your-user-name* (on Linux).
To check that everything went well run:

    poetry --version

If this does not work add the poetry installation directory to the PATH ([instructions](https://docs.oracle.com/cd/E19062-01/sun.mgmt.ctr36/819-5418/gaznb/index.html) for Linux)


## Run an example

Clone this repository to your local machine:

    git clone  --recurse-submodules -j8 https://github.com/DPaletti/dovado.git

Now position at the project root (from now on all commands assume you are at project root):

    cd dovado

Install all the required dependences:

    poetry install

Run an example:

    poetry run dovado < examples/input_files/input_rtl_vadd.txt

Doing so all the program prompts are automatically answered with each line in input (one line = one answer), open it to see the answers.
After all the vivado output you should see examples&rsquo; WNS (worst negative slack) and LUT (lookup table) percentage utilization


# Testing

In order to run tests:

    poetry run pytest

All tests will be ran and their respective outcome shown.   
Tests are managed through pytest which is used as a testing library and as a test runner. Functions which call Vivado are mocked through monkeypatch (from pytest).   

A recap of test coverage can be read by:

    cd html_cov/
    firefox index.html

if you do not have firefox installed any other browser will do.   


# Report
A full report of the activity conducted in developing Dovado and studying the RTL design space exploration problem can be read ([here](./dovado.pdf)).
