# -- Source path setup -------------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'JLJl'
copyright = '2023, JLJl'
author = 'JLJl'
release = '2023.10.24'
version = '2023.10.24.1'

# -- General configuration ---------------------------------------------------
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
]

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
