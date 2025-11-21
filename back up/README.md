# Introduction to Python programming

Python is an extremely versatile language and its use is growing more and more nowadays. Despite simplicity and readability are among significant Python strengths, writing a good quality Python code requires some degree of preparation. This course aims to introduce the student to the key topics of the language in order to give a solid basis for further investigations that will be required according to the specific field of application. The exposition of the topics uses several examples and tries as much as possible to highlight good Python programming practices in addition to the simple syntax correctness. To improve understanding, the different modules of the course are immediately put into practice in hands-on sessions in which students and teachers can interact directly on simple but significant concrete problems proposed in the exercise.

By the end of the course each student should be able to:
* understand the key features of Python language
* write a Python program/module using the basic syntax elements
* understand the best practices for programming in Python

### Pre-requisites:

Knowledge of the basic fundamentals of programming is useful but not necessary.
A working python environment already installed if you want to use your own laptop.

### Length: 
3 dd


See also [course presentation](https://eventi.cineca.it/en/hpc/introduction-python-programming) at CINECA HPC Courses website.


## Agenda

1. Introduction
   * Introduction to Python
   * Introduction to Jupyter
1. Environment
1. Basics (second degree example)
   * Types
   * Conditionals (if)
   * Minimal I/O
1. Control flow (integral example)
   * while
   * for
   * break, continue, pass
   * range
1. Functions (previous examples)
   * Basics
   * Passing arguments
   * Passing functions
   * Modules
   * Math module
1. Containers - I part (smoothing function example)
   * basics
   * list, tuple and set
   * for loops and containers
   * functions with containers
   * matplotlib
1. Strings and I/O (Caesar cipher example)
   * string handling
   * file management
   * encoding and decoding
1. Containers - II part (100 meters example)
   * dictionary
   * container management
1. Standard Library, introspection, and environment
   * standard library
     * os
     * argparse
     * datetime
     * logging
     * subprocess
   * basic introspection and docs
1. Decorators
1. Error handling
1. Classes (complex type)
   * short introduction
   * inheritance
1. Iterables, iterators and generators


## Download/Clone repository

```bash
git clone https://gitlab.hpc.cineca.it/scai-training-rome/python-intro-2025.git
```

## Hands-on Sessions

Hands on sessions will be held either locally on your laptop or on CINECA clusters, using Jupyter notebooks.

You can connect to CINECA clusters using a grafical interface (VNC) through the following methods:
1. using [Remote Connection Manager (RCM)](https://wiki.u-gov.it/confluence/pages/viewpage.action?pageId=358200249) (recommended solution)
1. using [MoabXTerm](https://mobaxterm.mobatek.net/)
1. using SSH Port Forwarding aka SSH tunnel 

If you want to run on your laptop, you need a working python environment. See [How to Setup Python Environment](#setup-python-environment) in this document.

### Connect using Remote Connection Manager

[Download](https://wiki.u-gov.it/confluence/pages/viewpage.action?pageId=358200249#RCM(RemoteConnectionManager)-Download) the Remote Connection Manager (RCM) client, choosing the proper binary for you OS (Linux, MaxOs, Windows).

Once installed, just run the client. Insert the HOST name you want to log in (i.e: rcm.leonardo.cineca.it) and your username/password credentials provided for the course. You can leave other options with their default (SSH session, windowmanager, etc. ).
Further [RCM instructions](https://wiki.u-gov.it/confluence/pages/viewpage.action?pageId=358200249#RCM(RemoteConnectionManager)-Gettingstarted) can be found on the RCM manual website.

### Connect using MobaXterm

[Download](https://mobaxterm.mobatek.net/download-home-edition.html) the MobaXTerm Home Edition (free version), choosing the proper binary for you OS (Linux, MaxOs, Windows).

Once installed, you can launch the application and select Session to start a New Remote Session. Select SSH session, choose the HOST name you want to log in (i.e: login01-ext.leonardo.cineca.it) and simply click on the OK button.

The MobaXTerm client is configured to run an X server and all SSH session will forward X session on your local computer. So that when you open a broswer on the remote machine, the window will appear on your local computer.

### Connect using SSH + X forwarding

This (lower level) approach is for brave developers who knows what to do :-)

On `localhost` (your laptop) open an ssh session to one of our cluster login node (i.e: login01-ext.leonardo.cineca.it)
from the shell (for Windows users use [Putty](https://www.putty.org/)) with the command:

```bash
ssh -L 9999:localhost:9999 USERNAME@login01-ext.leonardo.cineca.it
```

On the remote host (`leonardo`) open the jupyter notebook on the selected port with the following command:

```bash
jupyter notebook --port=9999 --no-browser
```

To access the notebook, open a browser on `localhost` and copy and paste the URL.


## Setup Python Environment

You can setup the python environment by your own or using the script `00_build_environment.sh` provided with the repository, simply running from a new shell:
```bash
source 00_build_environment.sh
```
This script will setup a virtual environment in your HOME directory, install all required software, and activate the environment with all necessary setup for the course.

The script will also run a jupyter notebook session, which will wait for a connection on a dedicated port. You just need to copy the link provided by the script into a browser in order to run notebooks.

### Install Python on Windows

For all Windows users, we recommand to install a complete Linux system through the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) package. If you already have Windows 10 or 11, the installation is very easy, just follow the instructions below. Otherwise follow the [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) full instructions from Microsoft WSL website.

1. Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator"
1. Type `wsl --install`
1. Restart the system

After rebooting, you will be able to run a complete Linux system simply opening the PowerShell or the Windows Command Prompt (NOT as administrator) and type `wsl.exe`. After loggin in, you can follow the instruction of the [Setup Python Environment](#setup-python-environment) in this document.

You can find a list of [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands).
