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
  # 'sphinx.ext.napoleon',
  'sphinx.ext.intersphinx',
  'myst_parser',
  'sphinx_design',
  'sphinx_copybutton',
  'sphinx_togglebutton',
  'sphinx_gallery.load_style',
  'sphinxcontrib.mermaid',
  'nbsphinx',
]

templates_path = ['_templates']
pygments_style = 'lightbulb'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
  'css/custom.css',
]

myst_number_code_blocks = ["python"]
myst_fence_as_directive = ["mermaid"]
myst_enable_extensions = [
  "amsmath",
  'attrs_block',
  "attrs_inline",
  "colon_fence",
  "deflist",
  "dollarmath",
  "fieldlist",
  "html_admonition",
  "html_image",
  # "linkify",
  "replacements",
  "smartquotes",
  "strikethrough",
  "substitution",
  "tasklist",
]

mermaid_output_format = 'svg'

autodoc_default_options = {
  'member-order': 'bysource',
  'undoc-members': True,
}

intersphinx_mapping = {
  'pylang': ('https://docs.python.org/3/', None),
  'pytorch': ('https://pytorch.org/docs/stable/', None),
  'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
