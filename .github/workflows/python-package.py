# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python package

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.11", ]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        # python -m pip install black
        # python -m pip install mypy
        python -m pip install pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
   
    # - name: Lint with black
    #   run: |
    #     # stop the build if there are Python syntax errors or undefined names
    #     black . --check
    # - name: check type annotations with mypy
    #   run: |
    #     # stop the build type annotation errors
    #     mypy --strict $(git ls-files 'epconversions/*.py')
    - name: Test with pytest
      run: |
        pytest
