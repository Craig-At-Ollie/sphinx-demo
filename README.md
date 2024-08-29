# sphinx-demo
This is a demo for sphinx and documentation

## Files:
 - `conf.py`: This is the sphinx configuration file.
 - `index.rst`: This is the file that gets converted into html, it contains the autodoc that reads the py module
 - `docstrings.py`: our documented demo file
 - _sphinx-quickstart_ auto-generated files & directories:
   - make.bat
   - Makefile
   - _build/
   - _static/
   - _templates/

## Building:

### Setup:
 1. Clone repo
 2. Create and enable a virtual environment
 3. Install requirements.txt

### Generating HTML:
Using the virtual environment created and enabled in the setup above, execute the command: `make html`. The generated html can be found in the `_build/html` folder.
