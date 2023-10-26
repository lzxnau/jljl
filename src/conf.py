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
# html_theme_options = {
#  'globaltoc_maxdepth': -1,
#  'globaltoc_includehidden': True
# }
html_static_path = ['_static']
