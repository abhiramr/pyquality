# Code Quality - The Practices and the Tools

- This is a repo for the upcoming talk for Bangpypers 18-07-2020 session.

## Code quality - What is it?
- It can mean different things to different people.
- To a data scientist, quality of code = quality of models deployed. 
- To a developer, it's 
    - modularity (manual)
    - correctness (tests)
    - performance (profiling)
    - readability (stylizing/documentation)

# Modularity
- In a bid to reduce complexity and to avoid ambiguity, each function must do only one task. 
- Separate functionalities as much as possible.

## Question of debate - 1 or many?

- There is really no 1 tool to rule them all. 
- Or is there? ;) 


# Correctness

## What is McCabe complexity?
Also known as cyclomatic complexity, it is the number of paths the code can take. The number goes higher than 1 if the number of control flow statements are higher than 0.

To see what this number is ->

- `pip install mccabe`
- `python -m mccabe --min 1 pyq_mccabe.py`

## How to test?
There are different ways of testing - unit, integration etc.
- The most popular tool is pytest.
- Coverage needs to be ensured. 


# Performance

## Why profile?
Not all operations are equally expensive. In long running scripts that are not very easily discernable with the eye, it is useful to use a line profiler to tell you which operation is the costliest in terms of time so you can try to optimize it better. 

# What about memory usage?
- That is important is some sectors and can be considered a measure of quality.
- How do you handle different data types?
- It can be measured using a simple decorator as well. Illustrated in pyq_mem_profile.py

#### What can you use to profile time?

- `pip install line-profiler`
- `kernprof -l pyq1.py`
- `python -m line_profiler pyq1.py.lprof` 

# Readability

## What can you do for readibility?

- While everyone's tolerance and abilities differ, it's good to have a standard set of practices.
- In the absence of such a standard on a company-wide level, PEP-8 serves as a good reference. 
- There are companies that have their own style guides - Google for e.g.
- To facilitate this, we have pylint, black

## For Django Projects

- Creating a copy of django_sample_project to illustrate what the problem was and what can be after linting. 

#### `pylint-django`

*Installation and usage*

- `pip install pylint-django`
- `pylint --load-plugins pylint_django  .`

Expected output - 

```
------------------------------------
Your code has been rated at 10.00/10
```

### `pre-commit`

*Installation and usage*

- This is a git-hook. It means, you use it within a git repository and "hook" into git's config folders.
- `pip install pre-commit`
- `pre-commit install`
- Set up a .pre-commit-config.yaml file with a config perhaps like - 

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
```
- `pre-commit run --all-files`

- This performs all the operations in the Config file for you. 
- What else can you do with it?


## Coming back to our question of debate - 1 or many?

- Is there really 1 tool to rule them all?
- Prospector comes close. 
- But you will have to run pytest and coverage anyway. 