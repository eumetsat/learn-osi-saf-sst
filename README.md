# Learn OSI SAF SST

<hr>

[![Python](https://img.shields.io/badge/python%203.10-anaconda-green)](https://www.anaconda.com/products/distribution)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.txt)
[![EUMETLAB](https://img.shields.io/badge/open-EUMETLAB-E67E22.svg)](https://gitlab.eumetsat.int/eumetlab/oceans/ocean-training/sensors/learn-osi-saf-sst)
[![USER PORTAL](https://img.shields.io/badge/open-USER%20PORTAL-154360.svg)](https://user.eumetsat.int/data/themes/marine)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fgitlab.eumetsat.int%2Feumetlab%2Foceans%2Focean-training%2Fsensors%2Flearn-osi-saf-sst/HEAD?labpath=Index.ipynb)

<hr>

## Overview

The **learn-osi-saf-sst** module consists of a collection of Python-based Jupyter Notebooks  
design to demonstrate the use of the sea surface temperature products within the OSI SAF catalogue, 
and to help users begin to work with them.

For any questions about this repository, please contact ops@eumetsat.int.

## License
 
This code is licensed under an MIT license. See file LICENSE.txt for details on 
the usage and distribution terms. No dependencies are distributed as part of 
this package. Copyright EUMETSAT 2024.

All product names, logos, and brands are property of their respective owners. 
All company, product and service names used in this website are for identification 
purposes only.

## Authors

* [**Olivier Membrive**](mailto://osi-saf.manager@meteo.fr) - [OSI SAF](https://osi-saf.eumetsat.int)
* [**Cécile Hernandez**](mailto://osi-saf.manager@meteo.fr) - [OSI SAF](https://osi-saf.eumetsat.int)
* [**Lou-Anne Quellet**](mailto://osi-saf.manager@meteo.fr) - [OSI SAF](https://osi-saf.eumetsat.int)
* [**Gwenaël Le Bras**](mailto://osi-saf.manager@meteo.fr) - [OSI SAF](https://osi-saf.eumetsat.int)
* [**Stéphane Saux Picart**](mailto://osi-saf.manager@meteo.fr) - [OSI SAF](https://osi-saf.eumetsat.int)
* [**Ben Loveday**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)
* [**Hayley Evers-King**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)

Please see the AUTHORS.txt file for more information on contributors.

## Prerequisites

You will require `Jupyter Notebook` to run this code. We recommend that you install 
the latest [Anaconda Python distribution](https://www.anaconda.com/) for your 
operating system. Anaconda Python distributions include Jupyter Notebook.

## Dependencies

|item|version|licence|package info|
|---|---|---|---|
|python|3.10.13|PSF|https://docs.python.org/3/license.html|
|jupyterlab|4.1.2|BSD-3|https://anaconda.org/conda-forge/jupyterlab|
|ipywidgets|8.1.2|BSD-3|https://anaconda.org/conda-forge/ipywidgets|
|dask|2024.2.1|BSD-3|https://anaconda.org/conda-forge/dask|
|xarray|2024.2.0|Apache-2.0|https://anaconda.org/conda-forge/xarray|
|netcdf4|1.6.5|MIT|https://anaconda.org/conda-forge/netcdf4|
|scipy|1.12.0|BSD-3|https://anaconda.org/conda-forge/scipy|
|matplotlib|3.8.3|PSFL|https://matplotlib.org/stable/users/project/license.html|
|cartopy|0.22.0|LGPL-3|https://scitools.org.uk/cartopy/docs/latest/copyright.html|
|cmocean|3.1.3|MIT|https://anaconda.org/conda-forge/cmocean|
|eumdac|2.2.1|MIT|https://anaconda.org/eumetsat/eumdac|
|cmcrameri|1.8|MIT|https://anaconda.org/conda-forge/cmcrameri|

## Included components

None

## Installation

The simplest and best way to install these packages is via Git. Users can clone this 
repository by running the following commands from either their [terminal](https://tinyurl.com/2s44595a) 
(on Linux/OSx), or from the [Anaconda prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/). 

You can usually find your terminal in the start menu of most Linux distributions 
and in the Applications/Utilities folder  on OSx. Alternatively, you should be 
able to find/open your Anaconda prompt from your start menu (or dock, or via running 
the Anaconda Navigator). Once you have opened a terminal/prompt, you should navigate 
to the directory where you want to put the code. Once you are in the correct directory, 
you should run the following command;

`git clone --recurse-submodules --remote-submodules https://gitlab.eumetsat.int/eumetlab/oceans/ocean-training/sensors/learn-osi-saf-sst.git`

This will make a local copy of all the relevant files.

*Note: If you find that you are missing packages, you should check that you ran 
`git clone` with both the `--recurse-submodules` and `--remote-submodules` options.*

*Note: if you are using an older version of git, you may find that your submodules are empty. 
In this case, you need to remove the folder and re-run the line above with `--recursive` added to the end*

*Note: in some rare Anaconda instances, Git is not installed by default. To correct 
this, you can install Git using `conda install git` from the Anaconda prompt (Windows) 
or in your terminal (OSx/Linux).*

## Usage

This collection supports Python 3.10. Although many options are possible, the 
authors highly recommend that users install the appropriate Anaconda package 
for their operating system. In order to ensure that you have all the required 
dependencies, we recommend that you build a suitable Python environment, as 
discussed below.

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - e.g. those that are not included by default in Anaconda. In this 
directory, users will find a *environment.yaml* file which can be used to 
construct an environment that will install all the required packages.

To construct the environment, you should open either **terminal** (Linux/OSx) 
or an **Anaconda prompt** window and navigate to repository folder you downloaded 
in the **Installation** section above. In this folder there is a file called 
**environment.yml**. This contains all the information we need to install the relevant 
packages.

Older versions of the conda package manager can be very slow, so we will install a new "solver" that 
speeds things up. To do this, from the Anaconda prompt (Windows) or in the terminal (OSx/Linux) 
you can run:

`conda install -n base conda-libmamba-solver`

Once the line above is run, to create out Python environment, we run:

`conda env create -f environment.yml --solver=libmamba`

This will create a Python environment called **cmts_learn_osi_saf_sst**. The environment 
won't be activated by default. To activate it, run:

`conda activate cmts_learn_osi_saf_sst`

Now you are ready to go!

*Note: remember that you may need to reactivate the environment in every 
new window instance*

*Note: if you get a warning that "solver" is not a valid conda argument, you can 
skip the libmamba install and run:* `conda env create -f environment.yml`

*Note: as you need to install libmamba solver in the conda base environment, this may not always be
possible on cloud systems.*

### Running Jupyter Lab

This module is based around a series of [Jupyter Notebooks](https://jupyter.org/), designed to be run in Jupyter Lab. 
Jupyter Notebooks support high-level interactive learning by allowing us to combine code, text description and data 
visualisations. If you have not worked with `Jupyter Notebooks` before, please look at the [Introduction to Python 
and Project Jupyter](./working-with-python/Intro_to_Python_and_Jupyter.ipynb) module to get a short introduction to 
their usage and benefits.

To run Jupyter Notebook, open a terminal or Anaconda prompt and make sure you have activated 
the correct environment. Again, navigate to the repository folder. Now you can run Jupyter using:

`jupyter lab` or `jupyter-lab`, depending on your operating system.

This should open Jupyter Lab in a browser window. On occasion, Jupyter may not
be able to open a window and will give you a URL to past in your browser. Please do
so, if required.

*Note: Jupyter Lab is not able to find antyhing that is 'above' it in a directory 
tree, and you will unable to navigate to these. So make sure you run the line above 
from the correct directory!*

Now you can run the notebooks! We recommend you start with the [Index](./Index.ipynb) module.

### Running on cloud platforms

If you are running on a remote Jupyter Hub (e.g. WEkEO or Insula) you will need to perform some additional steps to 
ensure that you have the right python environment loaded in your notebook. When running locally, as long you have activated 
the correct environment, Jupyter will load it into your the "kernel" which runs your code by default. On cloud systems, we 
have to add the kernel to the system and apply it manually when we run.

To add an environment to a kernel you should first build the environment and activate it as described above. Once you have 
done this, you can add your environment to a kernel from the command line as follows:

`python -m ipykernel install --name cmts_learn_osi_saf_sst --user`

You should now be able to select the kernel from the menu bar in the top right hand side of any notebook you run.

*Note: it sometimes takes a few seconds for the kernel to register in the notebook itself*

*Note: the above does not apply to Binder, which will load the environment supplied with the Git repository*

### Collaborating, contributing and issues

If you would like to collaborate on a part of this code base or contribute to it 
please contact us on training@eumetsat.int. If you are have issues and 
need help, or you have found something that doesn't work, then please contact us 
at ops@eumetsat.int. We welcome your feedback!

<hr>
<hr>