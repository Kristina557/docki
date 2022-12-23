# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# Additional stuff for the LaTeX preamble.
'preamble': '\\usepackage[utf8]{inputenc}',
'babel': '\\usepackage[russian]{babel}',
'cmappkg': '\\usepackage{cmap}',
'fontenc': '\\usepackage[T1,T2A]{fontenc}',
'utf8extra':'\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
}

project = 'docki'
copyright = '2022, Miri'
author = 'Miri'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'ru'


Options for HTML output
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_favicon = '_static/favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = ['.']
epub_language = 'ru'
# If true, "(C) Copyright ..." is shown in the HTML footer.
# Default is True.

html_show_copyright = False
# How to display URL addresses: 'footnote', 'no', or 'inline'.
epub_show_urls = 'inline'
# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3
    