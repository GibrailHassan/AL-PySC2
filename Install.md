# Install Guide for PySc2 + AuLearn25 Base (Version 08.05.2025)

This  guide is meant to help you installing the Python StarCraft II environment together with our base repository for the assignments.
You will of course need an installation of StarCraft II!

## The gaming side

![sc2 logo](sc2.png)

On Windows your only way to install StarCraft II is the usual way of installing StarCraft II. You need to download the Battle.Net client via <https://eu.shop.battle.net>, create a Battle.Net account. Afterwards, download and install the free "Starter Edition" of StarCraft II using the Battle.Net client. *(There is also StarCraft (1) available on the BattleNet. PySc2 won't work with that installation.)*

After you have installed StarCraft II, you have to download the minigames package <https://github.com/deepmind/pysc2/releases/download/v1.2/mini_games.zip> of PySc2 and move the mini_games directory in the zip into the folder StarCraftII/Maps. You will need to create the directory "Maps" for this.

Under Linux you can download a "headless" client of StarCraft II with the disadvantage that you will not be able to use the original 3D view of the game on Linux. However, PySc2 offers an alternative 2D view.
Blizzard has provided links and explanations how to install it on the following GitHub repo.
<https://github.com/Blizzard/s2client-proto#downloads>

(First findings of your colleagues suggest that the PySc2 library in fact does not work with visual view under Linux. If you want to make your own experiments, feel free to do so.)

**NOTE:** If you do not install the game at the default location, you have to set the SC2PATH environment variable to your custom install directory.
We have decided to create our own fork of PySc2. If you find bugs, feel free to notify us on Mattermost or create an issue.

## Getting Base aulearn25

You need access to our base repository for our assignments. We have uploaded an intial version into the Moodle that we will not maintain through the semester. As a result, we recommend to use the one that is maintained in our institute's gitlab. Clone the Aulearn25_Assignments base repository from [gitlab](https://git.informatik.uni-kiel.de/ag-ins/teaching/aulearn25_assignments). If you do not have access to it, yet. Message Connor via Mattermost or write an email.
If you do not have an LDAP account, you are not able to access the gitlab. In this case, you have to request one. More about this on the web page of the student council <https://www.fs-informatik.uni-kiel.de/studium/ifi-accounts/>. For the instance that you cannot receive an LDAP account, we will provide starter variants of the repo in our moodle.

However, we strongly recommend to work in the university's gitlab - it also eases the hand-in procedure. If you have finished an assignment, just tag the specific last commit and invite a tutor to your project.
If you do not have access to the gitlab, you should send your assignment code to a tutor per email or upload it in Moodle if your archive is <= 20MB.

## Two Paths for Tooling

We recommend one of two ways to install Python and its dependencies. Either you use the relatively new package and project manager uv or use mamba + Poetry.
The second option is the "more established" one that we also used for Autonomous Learning 2023. The first one was suggested by a colleague of yours and so far works very well.
Please, say something if something breaks.

## Option 1: uv

On the current version of our repository, the pyproject.toml expects you to use uv.

By choosing this option, you install your dependencies using solely uv.
Uv is an open source package and project manager developed in Rust that promises to be a drop-in replacement for pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more. It also promises to run way more efficient and simplifies project setups by just requiring one tool.
You can install uv by choosing one of the options explained on this page <https://docs.astral.sh/uv/getting-started/installation/>.

The easiest option for Windows platforms is winget, the in Windows integrated package manager. Just run the following line in a command prompt.
```winget install --id=astral-sh.uv  -e```

Alternatively, you could download the official standalone setup script which is probably the easiest way to install uv on Linux. Or use cargo, Rust's package manager, to install it, if you have it already installed.
This is about it, to be honest. Uv can now do everything that we want.

One way of easily installing everything is calling `uv run run_basic.py` after moving with `cd` into the aulearn25 repository. It will install a Python version >= 3.13 and its dependencies in a virtual environment for you.

It might be the case that VSCode or your IDE of choice does not automatically recognise the installed dependencies of the venv that uv creates for you. If this is the case run `uv sync` in an terminal in the working directory of your project and reload the editor.

Our current pyproject.toml lets uv install PyTorch solely for CPU support on your system if your are using Windows. In case of MacOS, we are not entirely sure to be honest. Linux users will receive GPU support with CUDA 12.4.

To test whether you have GPU support with PyTorch - just open a python interpreter, first import torch and then prompt `torch.cuda.is_available()`. The response indicates whether your system is using cuda -> whether it can use an Nvidia GPU since CUDA requires one. However, PyTorch also supports AMD and GPUs on Mac.
The PyTorch page describes how to install PyTorch for different operating systems and GPUs <https://pytorch.org/get-started/locally/>.
You can run their pip commands by replacing `pip` or `pip3` with `uv pip`.

Unfortunately, we do not have access to an AMD GPU or a modern MAC to test it there. Feel free to share your experiences if you experiment with such a GPU :). 

Please jump to **"Testing AuLearn25"** for more instructions.

## Option 2: Mamba + Poetry

By choosing this option, you install your dependencies using mamba and poetry. For this, you have to use the pyproject.toml with poetry in its filename and rename it to pyproject.toml.

### Getting Python 3

You will of course need a Python version.
It is important that it is at least Python 3.9 and we recommend to keep your Python version updated to the newest release of your current version.
We recommend using Python 3.13, it's compatible with all packages that we need. It will require a manual hotfix for PySc2, though.

There are two ways in installing Python. We recommend using mambaforge. Mamba is a faster variant of conda which the first exercise introduced to you as (Ana)conda. It's a solid option to manage Python installations, managing virtual environments, can also install dependencies, and prevents conflicts between those.

You can install Mambaforge by downloading an installer for it from its [github page](https://github.com/conda-forge/miniforge#mambaforge) and executing it. You should tick that mambaforge is added to the Path variable. It is not recommended by its developers but without it we cannot access it easily from the terminal. In addition, you should tick the option for registering your mamba as your default Python.

<figure>
  <img src="mambaforge.png" alt="Mambaforge" width="400"/>
  <figcaption>Tick boxes 2 and 3 in this window.</figcaption>
</figure>

Mambaforge will automatically come with a somewhat recent release of Python 3.

If you execute ``mamba create -n aulearn python=3.13`` it will create an empty virtual environment with the name aulearn for you that already has an installed Python interpreter. You can activate it by executing ``mamba activate aulearn``. You can get out of a virtual environment of mamba by prompting ``mamba deactivate``.

#### The alternative (not recommended)

Alternatively, you can install Python as standalone software.
On Windows, you can download it from the official Python website https://www.python.org/downloads/ and install it using the installer.
We strongly discourage to install a global Python on Linux due to the possibility to accidentally damage your OS installation.
The installer will ask you in one Window whether you want to add Python to your PATH. You should tick this option. Otherwise, you won't be able to access your Python on command-line.

After installing python, you should test whether its working. For this prompt ```python --version``` it should respond you with a version $>= 3.13.0$.

### Getting Poetry

Poetry python-poetry.org is a tool for dependency management for Python. It's pretty useful and while not as easy to use and well known as Conda,  it's easier to manage and install a lot of dependencies at once with it.

We recommend to install poetry in a separate virtual environment to again separate it from your global Python installation.
For that purpose, create a virtual environment with ``mamba create -n poetry python=3.13`` and run the following install variants in this environment.

To access Poetry globally, you may add Poetry to your path variable. You can find the installation location of your virtual env's Poetry by prompting `whereis poetry` on Linux or `where poetry` on Windows.
There are again two options for installing poetry.

#### Option 1: Manual download

You can download the python install script either directly from [their website](https://install.python-poetry.org/). Afterwards, you only need to run it with python on the command line. When the installation is finished, you will need to add poetry's binaries to your Path environment variable. If you have no Python >= 3.7 as your system Python, you should use your virtual conda environment for this.

#### Option 2: Purely per command-line

If you are under Windows, you can install it using the Powershell.
Run:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - 
```

in an powershell with admin rights.

Under Linux, MacOS or WSL you can run the simpler command ``curl -sSL https://install.python-poetry.org | python3 -``.

When the installation is finished, you will need to add poetry's binaries to your Path environment variable.

After you have installed Poetry prompt ``poetry --version`` in a shell in order to test whether the installation worked as intended.

### Installing PyTorch

PyTorch is our Deep Learning library.
The new pyproject.toml file of the repository should install pytorch for you :)

If you prompt ``pip freeze`` in your virtual environment it should include torch in the list. Note that this PyTorch version will be CPU only on Windows.
In case of MacOS, we are not entirely sure to be honest. Linux users will receive GPU support with CUDA 12.4  (if they own an Nvidia GPU).

We do not own an AMD GPU or a modern MAC. As a result, we lack experiences in how well the PyTorch setup works there. Feel free to share your experiences if you experiment with such a GPU :). 

### Installing PyTorch manually

If this should fail... you can install it manually for example to gain GPU support.
If you are unsure whether poetry is capable to use your Nvidia GPU, you can just open a python interpreter import torch and prompt
`torch.cuda.is_available()`. If it confirms, then your PyTorch installation is actually using your GPU otherwise it is still CPU bound.

#### For Poetry with Mamba

If you use mamba you can use it to install pytorch quite easily with one of the commands on PyTorch's webpage
<https://pytorch.org/get-started/locally/> They have different options for different operating systems (and even GPUs)
Under Linux `mamba install torch` should give you a version of PyTorch that builds on CUDA 12.4.

#### For Poetry without Mamba

 Run ``bash poetry shell`` it will open a shell in your newly created virtual environment.
Then we would suggest to use one of the commands on <https://pytorch.org/get-started/locally/> that fits to your GPU and operating system.

## Installing the dependencies of aulearn25

Next, you will need our base repository.

First move into the aulearn25 directory. Either using ``cd`` or by directly opening a terminal in the directory.
Then you have two options: If you are using mamba, activate your mamba virtual environment and then prompt ``poetry config virtualenvs.create false`` so that poetry does not create another virtual environment.

Otherwise, run ``poetry config virtualenvs.create true`` so that it creates an own one.

In both cases run, ``poetry install --only main --no-interaction --no-ansi``. The latter will install all dependencies for the project that are specified in the pyproject.toml in the virtual Python environment.

## Testing Aulearn25

Now, everything should work!  Try to run one of the runners. For example, prompt ```python run_basic.py`` or `uv run run_basic.py`.
If you are using Python <= 3.10 or our own fork of PySc2, it should work fine. 

Running it with Python >=3.10 and the current pypi release of the package will result into a bug.

### Manual hotfix for Python 3.13 and PySc2 4.0.0 from PyPi

Your Python Interpreter should already show it to you

``` bash
File "C:\Users\<you>\AppData\Local\pypoetry\Cache\virtualenvs\<yourvenv>1\Lib\site-packages\pysc2\lib\colors.py", line 126, in shuffled_hue
    random.shuffle(palette, lambda: 0.5)  # Return a fixed shuffle
TypeError: Random.shuffle() takes 2 positional arguments but 3 were given
```

We will fix this! Open the file and change the line

```python
random.shuffle(palette, lambda: 0.5)
```

to

```python
random.shuffle(palette)
```

After this fix, everything should run as expected. We sacrifice a bit reproducibility here but that should not be an issue (and would be fixable by fixing the seeds of our experiments).
