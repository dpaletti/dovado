

# DoVado

Advanced Computer Architectures (ACA) Research project 2020.   
A CLI tool for RTL Design Space Exploration on top of Vivado.   
&ldquo;Do&rsquo; vado?&rdquo; is an italian slang expression for &ldquo;Dove vado?&rdquo; which means &ldquo;Where do I go?&rdquo;


# State of the Project

**In active development**   
Given an input RTL file after-synthesis utilization and timing are extracted.


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

    git clone https://github.com/DPaletti/dovado.git

Now position at the project root:

    cd dovado

Install all the required dependences:

    poetry install

Run an example:

    poetry run dovado < examples/fifo_memory/input

Doing so all the program prompts are automatically answered with each line in input (one line = one answer), open it to see the answers.
After all the vivado output you should see examples&rsquo; WNS (worst negative slack) and LUT (lookup table) percentage utilization

