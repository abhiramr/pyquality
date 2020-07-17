# Code Quality - The Practices and the Tools

- This is a repo for the upcoming talk for Bangpypers 18-07-2020 session.

## Code quality - What is it?
- It can mean different things to different people.
- To a data scientist, quality of code = quality of models deployed. 
- To a developer, it's 
    - readability (stylizing)
    - modularity (manual)
    - correctness (tests)
    - performance (profiling)


## What is McCabe complexity?
Also known as cyclomatic complexity, it is the number of paths the code can take. The number goes higher than 1 if the number of control flow statements are higher than 0.

To see what this number is ->

- `pip install mccabe`
- `python -m mccabe --min 1 pyq_mccabe.py`


## For Django Projects

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