# Python Tactics

### Learn Python By Writing Functions

This is a series of exercises, largely based on [Nik Frank](github.com/nikfrank)'s
[JS Tactics](github.com/nikfrank/js-tactics). The exercises are all in the
`exercises.py` script in the following form:

```
# this function should print something to the screen
def printer():
    pass
```

The goal is to write all the functions in all of the exercises.

The tests in `exercise_test.py` check to see if the function behaves properly.
Right now I've been trying to move quickly, so they're pretty basic. If there's a
need, I'll try to improve them.

My suggestion is to use a module called `pytest-watch` with this. It can run the tester
again anytime `exercises.py` is changed, which makes for a much better workflow,
as you can fire it up, start coding, and see in real time if it works. We'll
provide a guide for getting started including this. The `$` just represents your
command prompt, you shouldn't be typing the `$` in.

## Getting Started

#### Cloning the repo

```
$ git clone https://github.com/wschwab/python_tactics.git
$ cd python_tactics
```
It's important to be in the `python_tactics` folder for some of the steps ahead.

#### Setting up a virtual environment

The suggestion in Python is to set up a new virtual environment for each project.
We'll work on getting you up and running with that next. Note that the command for Python
can vary. I write `python3` below, but on your machine it may be `python` or `py`. Best
of luck figuring it out if it's not one of those three. I'm going to split this into
Windows and Mac/Linux, just because they're a little different:

##### Mac/Linux

```
$ python3 -m venv /your/path/to/python_tactics
$ source /your/path/to/python_tactics/bin/activate

```

###### Windows (PowerShell)

```
$ python3 -m venv c:\path\to\python_tactics
$ c:\path\to\python_tactics\Scripts\activate.bat
```
'Your path to python_tactics' means the full path in your file system to the folder
for Python Tactics. In most file explorers you can get in from the menu or by right-clicking
when you're in the folder.

If the venv activated properly, your prompt should change:

```
(python_tactics)$
```

Great!

#### Setting up Pytest-Watch

Pytest-Watch gives us the ability to turn on a tool that will check your functions
to make sure that they're running right. It will also install any other tools that
we need for it to work, so this should be the only install you need, and you also
won't need special permissions (`sudo` or admin) to install it, since it should
only install to the venv.

```
(python_tactics)$ pip3 install pytest-watch
```

#### Running Pytest-Watch

If everything has gone well up until now, this should be simple enough:

```
(python_tactics)$ pytest-watch
```

The Pytest-Watch repo says you can start it by just typing `ptw`, but I've had trouble
with it, so I just gave the whole command.

#### Get Going!

Fire up your code editor from inside the venv. I'll do Atom and Visual Studio Code,
but the idea should be the same for any editor:

##### Atom

```
(python_tactics)$ atom .
```

##### Visual Studio Code

```
(python_tactics)$ code .
```

Enjoy, and happy learning!
