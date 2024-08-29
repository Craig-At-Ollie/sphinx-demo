# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Inject the current path into the sys path for autodoc
import os, sys
sys.path.insert(0, os.path.abspath('./'))


project = 'Sphinx-demo'
copyright = '2024'
author = ''
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.viewcode', 'sphinx.ext.intersphinx', 'sphinx.ext.autosummary']

# -- Intersphinx mapping ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

templates_path = ['_templates']
exclude_patterns = ['venv', '_venv', '.venv', '.git',]

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Sphinx-Demo', 'A Sphinx Demonstration',
     [author], 1)
]


# -- Options for autodoc ----------------------------------------------------
# PEP-604 style literals
python_display_short_literal_types = True


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Sphinx-demo', 'A Sphinx Demonstration',
     author, 'Sphinx-demo', 'Testing some Sphinx shit out in python',
     'Miscellaneous'),
]
