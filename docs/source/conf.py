# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
if sys.version_info < (3, 7):
    from importlib_metadata import version
else:
    from importlib.metadata import version

# -- Project information -----------------------------------------------------

project = 'illumio'
copyright = '2022, Illumio'
author = 'Illumio'

# The full version, including alpha/beta/rc tags
release = version('illumio')

# Simple x.y.z version number
version = '.'.join(release.split('.')[:3])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'tests'
]

add_module_names = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
    "navigation_with_keys": True,
    "sidebar_hide_name": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "illumio_logo.svg"

html_show_sphinx = False

# -- Autodoc Options ---------------------------------------------------------

autodoc_member_order = 'bysource'

# -- Autosummary Options -----------------------------------------------------

autosummary_generate = True

autosummary_imported_members = False

autosummary_ignore_module_all = False
