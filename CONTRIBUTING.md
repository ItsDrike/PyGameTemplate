# Contributing Guidelines

This project is fully open-sourced and all contributions are welcome.

Do note though that we value the quality of the code we write and distribute, and you will need to adhere to the
repositories standards. Your PR may get rejected on the basis of a contributor failing to follow these guidelines.

## The Golden Rules of Contributing

You should adhere to these rules in pretty much every project, even if it doesn't require you to, it's a good practice
and the maintainers will be a lot less likely to refuse to merge your PR.

1. **Lint before you push.** We have simple but strict style of rules that are enforced through linting. You must
   always lint your code before committing or pushing. Using tools such as `flake8` and `pre-commit` can make this
   easier. Make sure to follow our [style guide](./CONTRIBUTING.md#style-guide) when contributing.
2. **Make great commits.** great commits should be atomic, with a commit message explaining what and why. More on this can be found in [this section](./CONTRIBUTING.md#writing-good-commit-messages).
3. **Do not open a pull request if you aren't assigned to the issue.** If someone is already working on some issue,
   consider offering to collaborate with that person rather than ignoring his work and doing it on your own. If the
   issue doesn't have an author assigned, feel free to ask to be assigned. If you want to work on something completely
   new, make sure to open an issue about it first and ask to be assigned. This helps both you and us because if we
   would decide that the feature doesn't adhere to our vision of the project's future, it could get declined quickly
   without you developing it through only to get denied from the PR.
4. **Use assets licensed for public use.** Whenever a static asset such as images/video files/audio or even code is
   added, they must have a compatible license with our projects.
5. **Use draft pull requests if you aren't done yet.** If your PR isn't ready to be reviewed yet, mark it as draft.
   This is further described in [this section](./CONTRIBUTING.md#work-in-progress-prs)
6. **Follow our [Code of Conduct](./CODE_OF_CONDUCT.md).**

## Writing Good Commit Messages

A well-structured git log is key to a project's maintainability; it provides insight into when and why things were done
for future maintainers of the project.

Commits should be as narrow in scope as possible. Commits that span hundreds of lines across multiple unrelated
functions and/or files are very hard for maintainers to follow. After about a week, they'll probably be hard for you to
follow too.

Please also avoid making minor commits for fixing typos or linting errors. Just lint before you push as described in
[this category](./CONTRIBUTING.md#linting-and-precommit).

We've compiled a few resources on making good commits:

* <https://chris.beams.io/posts/git-commit/>
* <https://thoughtbot.com/blog/5-useful-tips-for-a-better-commit-message>
* <http://ablogaboutcode.com/2011/03/23/proper-git-commit-messages-and-an-elegant-git-history>
* <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>
* <https://dhwthompson.com/2019/my-favourite-git-commit>

## Work in Progress PRs

Whenever you add a pull request that isn't yet ready to be reviewed and merged, you can mark it as a draft. This
provides both visual and functional indicator that the PR isn't yet ready to be reviewed and merged.

This feature should be utilized instead of the traditional method of prepending `[WIP]` to the PR title.

Methods of marking PR as a draft:

1. When creating it

   ![image](https://user-images.githubusercontent.com/20902250/94499351-bc736e80-01fc-11eb-8e99-a7863dd1428a.png)
2. After it was crated

   ![image](https://user-images.githubusercontent.com/20902250/94499276-8930df80-01fc-11eb-9292-7f0c6101b995.png)

For more info, check the GitHub's documentation about this feature
[here](https://github.blog/2019-02-14-introducing-draft-pull-requests/)

## Don't reinvent the wheel

We're an open-sourced project, and like most other open-sourced projects, we depend on other projects that already
implemented things that we're using. It doesn't make sense to implement everything from bottom up when there already
are perfectly reasonable and working implementations made. This usually mostly means using libraries rather than
implementing their code manually, however that's just one way of utilizing other amazing open-sourced projects.

Another way we can make use of the open-sourced community is by utilizing the code written by other people and use
it directly in our source, but **never** use code of others without the appropriate permissions to do so, if this code
comes from an open-sourced project, we always follow the terms of the license that project is licensed under. This
usually means including full-text of that license and the copyright header with description of which files or parts
of the code-base this license applies to. We define these licenses in
[`LICENSE-THIRD-PARTY` file](./LICENSE-THIRD-PARTY). If you will take any code from an open-sourced repository, it is
very important to mention it there.

We all stand on the shoulders of giants even just by using the python language, there were some very smart people
behind implementing this language or the libraries that our project uses and they deserve the credit for their hard
work as their license specifies. We try to be an honorable project and even if a project is released to the public
domain with a license such as the Unlicense, mentioning it the 3rd-party license file gives these people credit for
their work, which we believe is the honorable thing to do, even though their license doesn't specifically require it.

Our project is released under the GPL v3 license and this means we can utilize the code of GPL v3 libraries as well
as the permissive licenses (such as MIT, Apache or BSD licenses), it also means that when you contribute to our
project, you agree that your contributions may appear on other projects accordingly to the GPL license, this is a
"copy-left" license, which ensures that your code will always remain open-sourced and it will never be relicensed
unless you agree to that specifically. If for some reason you don't want to contribute under a copy-left license but
rather under MIT, or other permissive license, you are free to do so, just mention whatever parts you added in the 3rd
party license file with your license's full-text with a copyright notice that includes your name and a link to the
original source (if you just made that code up, instead of a link to the original source, you can just include a link
to your github profile, or just use your git email address.)

## Style Guide

For clarity and readability consistent styling across the project's code base is very important. It is not unusual that
style adjustments will be requested in pull request.

It is always a good practice to adhere to the prevailing code style. Don't change the styling of half of the project
when simply introducing some feature, this often happens with some auto-formatters that aren't compatible with our
existing code style. If you think a code style change is really relevant, open an issue about it and tell us what
exactly should be changed, describe why and feel free to ask us to get assigned to it and you can then open a PR and
work on that specifically. PRs that aren't here to solve styling issues shouldn't attempt to do so, if they do, they
will likely be rejected until the styling is reverted.

We mostly follow `pep8` and `flake8` with certain extensions for our styling. If you aren't familiar, you can check
[pep8 guidelines](https://www.python.org/dev/peps/pep-0008/). These are enforced with the use of `pre-commit` git
hook, more about that in [this section](./CONTRIBUTING.md#linting-and-precommit).

After you've set-up the `pre-commit` hook, make sure to also check the [specific styling
rules](./CONTRIBUTING.md#specific-styling-rules), there are some rules which aren't enforced by flake8 that we follow
to ensure clean and readable code.

## Setting up the virtual environment

This project uses [`poetry`](https://python-poetry.org/) for dependency management and virtual environment. Poetry is a
really nice tool which is very powerful though it can be a bit complicated to get used to it at first, if you're
already familiar with tools such as pipenv or even just pure venv, you'll probably find it quite easy to set up.

We use poetry because it provides a really clean way of managing project-specific dependencies. This means that if this
project would require a specific version of python with a specific set of dependencies at some given versions, we don't
have to clutter the global python installation with these dependencies, but rather we simply use poetry, which will
create per-project virtual python environment that will contain all of these dependencies without interfering with the
global python version. (Note that you'll need to have the actual mainline python version of the project installed, i.e.
if a project requires python 3.8 and you only have 3.9 on your system, you won't be able to run that project until you
also installed 3.9).

Another use of poetry that we're utilizing is it's deployment system. This makes it very easy for us to release the
package to PyPI, however you probably won't need to be touching this unless you are making a complete fork with your
own PyPI release or you're testing things out and are attempting to release the package on Test PyPI.

Setting up the project with poetry:
1. Install poetry (you can use `pip install poetry`, however this is specific to some installed python version, instead
   you should install poetry globally if you intend on switching the versions, which may happen in this project. If
   you're on linux, most package managers will have it packaged as 'poetry', for more info check the
   [docs](https://python-poetry.org/docs/))
2. Create the virtual environment with `poetry install --dev` (notice the `--dev` flag, without it we would only
   install the dependencies needed for our project to run, however our project also includes some additional
   dependencies such as flake8 that provides linting rules for python.)
3. After that, you'll want to run all projects using `poetry run [command]`, alternatively, you can also go into poetry
   shell from which you can run all commands normally and they'll be run from the poetry environment's scope. You can
   get into this shell using `poetry shell`


## Linting and Precommit

It is important that we lint before pushing, to avoid publishing 10 commits just to fix the linting and pass the
workflow checks or additional requested styling. To avoid this, you can use a tool called `pre-commit`. It is a [git
hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) that runs before every commit you make, and is able to
stop that commit if some issues have occurred.

In our [`.pre-commit-config.yaml`](./.pre-commit-config.yaml), we define several checks to be ran before committing,
which are here to enforce our styling guidelines and correct typing. To install pre-commit hook all you need to do is
to run `poetry run task precommit` which will add the git-hook and the pre-commit will run before each new commit you
make and will stop you from committing badly-linted code.

You can also run `pre-commit` on every file in the project by running `poetry run task lint`, this will check the files
you haven't yet decided to commit too.

We also have the [validation workflow](./.github/workflows/validation.yaml) which runs these checks in GitHub itself,
but it is important to run these locally on your own rather than pushing each fixing commit and letting the workflow to
do the job for you because we have limited amount of workflows runs, please don't abuse them.

In our case, the `pre-commit` runs some minor checks, but most notably it runs the `flake8` check, which is here to
enforce our code linting guidelines, this respects our [`tox.ini`](./tox.ini) configuration which defines how flake8
should run.

Setting up pre-commit:

1. Install pre-commit (`pip install pre-commit`, alternatively there will likely be a system-wide version in your
   package manager, however in this case you don't need to install that since pre-commit will always be python version
   agnostic and it'll get installed with our poetry development dependencies automatically)
2. Add pre-commit to your cloned git repository with `pre-commit install`, after this, a git hook will be added and
   pre-commit will run against every modified file before each git commit. If these pre-commit checks fail, you will
   not be allowed to make that commit. (You can bypass it with `git commit --no-verify` if you'd ever need to, however
   you should always try to resolve the pre-commit issues rather than committing failing code)
3. If you'd want to check your code with pre-commit without having to actually make a commit, you can also run
   `pre-commit run --all-files`.

## Specific styling rules

These are the specific styling guidelines our code-base is following. They are here to ensure a smooth and readable
code which will be intuitive for newcomers to this project but also make it easy to work with for common contributors.

Some of these will also be enforced by `flake8`, but some won't so make sure to read through these to know our
code-base style is designed.

### Type Hinting

[PEP 484](https://www.python.org/dev/peps/pep-0484/) formally specifies type hints for Python functions, added to the
Python Standard Library in version 3.5. Type hints are recognized by most modern code editing tools and provide useful
insight into both the input and output types of a function, preventing the user from having to go through the codebase
to determine these types.

For example, a non-annotated function can look like this:

```python
def divide(a, b):
    """Divide the two given arguments."""
    return a / b
```

With annotation, the function looks like this:

```python
def divide(a: int, b: int) -> float:
    """Divide the two given arguments."""
    return a / b
```

Some great resources for learning about python type-hints:

Thankfully python type-hinting is fairly easy to understand, but if you do want to see some rather interesting
resources for a bit more advanced concepts such as type variables or some python specific types like `typing.Callable`,
we've compiled a quick list of really amazing resources about these type hinting practice.

* Python documentation from `typing` library: <https://docs.python.org/3/library/typing.html>
* MyPy documentation (very extensive but quite beginner friendly): <https://mypy.readthedocs.io/en/stable/>
* Typing Generics (advanced): <https://itsdrike.com/posts/typing-generics/>

## Static type checking

All code in this code-base is written to be type-safe with specific static typing rules specified by type-hints, as
shown in the [category above](./CONTRIBUTING.md#Type-Hinting). This enables us to find issues very quickly, for example
if we had code like this:

```python
def merge(a, b):
    return a + b
```

We wouldn't know if the variables `a` and `b` actually have the support for addition (`__add__`) between them, however
with code like this:

```python
def merge(a: list, b: int):
    return a + b
```

We may notice that it makes no sense to add a list to a number, a static type checker would immediately detect this,
and let us know that something is wrong and the types list and int don't support addition like this.

For this project, we use [`pyright`](https://github.com/Microsoft/pyright) as our static type checker (if you use 
VSCode, it is included in the Pylance extension, which is installed along with the Python extension). But it is 
important to know that there are alternatives, such as [`mypy`](https://github.com/python/mypy). We've made sure to
include pyright in the pre-commit checks, which means that pyright will check your code before each commit you make.

### Logging

Instead of using `print` statements for logging, we use the built-in `logging` module. Here is an example usage.

```python
import logging

logger = logging.getLogger(__name__)  # Get logger bound to the module name.  
# ^^ This line is usually placed under the import statements at the top of the file.

logger.debug("This is a DEBUG log, it should be used to make debugging easy, but it won't be shown in production.")
logger.info(
    "This is an INFO log, it shows some normal events occurring that don't need direct attention, but are worth "
    "keeping track of in production.") logger.warning("This is a WARNING log, it indicates that something is out of "
    "the ordinary, this isn't something causes too much problem, but it should be logged"
)
logger.error(
    "This is an ERROR log, it signifies a failure in specific part of the application and requires urgent attention."
)
logger.critical(
    "This is a CRITICAL log, it indicates that something went very wrong and may cause the whole application to fail, "
    "they require immediate intervention."
)
```

This allows us to track which function the error occurred in and at what time, it also allows us to keep all of the
logs from all runs in the `logs/` directory, making it a much more powerful tool compared to simple print statements.

To make our logging output a bit nicer, we also use the `coloredlogs` library, which means requires some extra config,
so instead of the simple example above, what you'll actually see in our code base looks more like this:

```python
from src.util.log import get_logger

log = get_logger()

log.debug("This DEBUG log is colored!")
```

Another non-standard feature which we add is a "TRACE" level log. This is a log level below DEBUG and it's here to make
tracing bugs a lot easier, while debug statements can be useful during development because they describe what's going
on, trace statements can be a lot more verbose and generally only really useful if we're tracing some bugs.

```python
from src.util.log import get_logger

log = get_logger()

log.trace("This is a TRACE level log.")
```

### Quotes

Preference is to use double-quotes (`"`) wherever possible. Single quotes should only be used for cases where it is
logical. Exceptions might include:

* Using a key string within an f-string: f"Today is {data['day']}".
* Using double quotes within a string: 'She said "oh dear" in response'

Docstrings/Multiline strings must always be wrapped in 3 double quotes (`"""my string"""`).

### Docstring Formatting Directive

Many documentation packages provide support for automatic documentation generation from the codebase's docstrings.
These tools utilize special formatting directives to enable richer formatting in the generated documentation.

For example:

```python
from typing import Optional


def foo(bar: int, baz: Optional[dict[str, str]] = None) -> bool:
    """
    Does some things with some stuff.

    :param bar: Some input
    :param baz: Optional, some dictionary with string keys and values

    :return: Some boolean
    """
    ...
```

Since we don't utilize automatic documentation generation, this kind syntax isn't necessary here and it should not be
used in the code contributed here.

The parameter types should instead simply be denoted with type annotations and should the purpose of the variable not
be clear from it's name and annotation, a prose explanation can be used. Explicit references to variables, functions,
classes, etc. should be wrapped with backticks (\`my_variable\`)

For example, the above docstring would become:

```python
from typing import Optional


def foo(bar: int, baz: Optional[dict[str, str]] = None) -> bool:
    """
    Does some things with some stuff.

    This function takes an index, `bar` and checks for its presence in the database `baz`, passed as a dictionary.
    Returns `False` if `baz` is not passed or if `bar` wasn't found in `baz`.
    """
    ...
```

To provide further instruction on our docstring formatting syntax, here are the formatting options

```python
def donut(a: bool, b: str) -> None:
    """Short one-line description of the function."""

def apple(a: bool, b: str) -> None:
    """
    Longer one-line description of a command, which would take up way too much line space if done as shown above.
    """

def bread(a: bool, b: str) -> None:
    """
    Short one-line summary of this function.

    Detailed multi-line description of a command, since it would be too long
    or not relevant enough to clutter the short one-line description.
    """

def pineapple(a: bool, b: str) -> None:
    """
    Short one-line description.

    Detailed multiline description.
    This may include the full explanation of how this command works.

    We can also have multiple sections like this.
    Or when necessary a list of accepted parameters and their explanation.

    Parameters: (detailed parameter description if they are unclear
    from name and annotations, there's usually no need for this)

    * a: bool
        This variable is only a placeholder for this very explanation.
    
    However this parameter description syntax should usually be avoided unless there's
    no better way of doing it.

    We can also include an example usage section like this:
        >>> pineapple(True, "hi")
        "hi"  # Return value with these arguments was the string "hi"
        >>> pineapple(False, "hi")
        None  # Return value with these arguments was None
    """

def banana(a: bool, b: str) -> None:
    """My docstring"""
    print("I like bananas")  # No space between docstring and first line of code for functions/methods

class Orange:
    """My docstring"""

    def __init__(self):  # Extra newline between the class docstring and first method (or class params)
        ...
```


## Changes to this Arrangement

We tried to design our specifications in a really easy and comprehensive way so that they're understandable to
everyone, but of course from a point of someone who already has some established standards, they'll usually always
think that their standards are the best standards, even though there may actually be a better way to do some things.
For this reason, we're always open to reconsidering these standards if there's a good enough reason for it.

Afterall every project will evolve over time, and these guidelines are no different. This document and the standards it
holds are open to pull requests and changes by the contributors, just make sure that this document is always in sync
with the codebase, which means that if you want to propose some syntactic change, you also change it everywhere in the
codebase so that the whole project will actually follow the newly proposed standards.

If you do believe that you have something valuable to add or change, please don't hesitate to do so in a PR (of course,
after you opened an issue, as with every proposed feature by a non-core developer).

## Footnotes

This could be a lot to remember at once, but you can use this document as a resource while writing the code for our
repository and cross-check that your styling is following our guidelines and that you're practicing the rules that
we've set here.

This document was inspired by
[Python Discord's CONTRIBUTING agreement.](https://github.com/python-discord/bot/blob/master/CONTRIBUTING.md).
