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
We're going to use `pipenv` for creating virtual environments, so we'll describe
how to get you up and running with that next.

Note that the command for Python and pip (the Python module installing tool)
can vary. I write `python3` and `pip3` below, but on your machine it may be `python` (and `pip`) or `py`. Best of luck figuring it out if it's not one of those three.

Type in the following commands (the second needs to be in the python_tactics folder).
If you're on Windows, leave out the word `sudo` (but you might need to be running
as the administrator - right click the start menu and run a prompt as admin if needed).

```
$ sudo pip3 install pipenv
$ pipenv shell

```

If the virtual environment (venv) activated properly, your prompt should change:

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
(python_tactics)$ pipenv install pytest-watch
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
