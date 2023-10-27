import os
import sys

sys.path.insert(0, os.path.abspath('../src/pns'))

# -- Project information -----------------------------------------------------
project = 'JLDP'
copyright = '2023, JLDP'
author = 'JLDP'
release = '2023.10.25'
version = '2023.10.25.2'

# -- General configuration ---------------------------------------------------
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinxcontrib.mermaid',
  'myst_parser',
  'nbsphinx',
  'sphinx_gallery.load_style',
]

templates_path = ['_templates']
pygments_style = 'lightbulb'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

myst_fence_as_directive = ["mermaid"]

mermaid_output_format = 'svg'
