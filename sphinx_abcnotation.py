""" ABC Notation for Sphinx

    Extention for Sphinx. Adds an 'abc'-directive where ABC Notation can be
    written, to be rendered and included as SVG files.

    Copyright 2020 by Stefan Wijnja.

    License: MIT (see LICENSE).

"""

import os
import tempfile
from hashlib import sha1
import subprocess
import shutil

import docutils
from docutils.parsers.rst import Directive, directives

from sphinx.errors import SphinxError
from sphinx.util import ensuredir


class abc(docutils.nodes.Element):
    pass

def render_abc(self, abc_source):
    """ Render abc_source with abcm2ps."""

    # Don't try again if we had an error before.
    if hasattr(self.builder, '_abcnotation_warned'):
        return None, None

    # Generate unique base filename
    base_filename = sha1(abc_source.encode('utf-8')).hexdigest()

    # abcm2ps insists on tacking on '001' before .svg because it can export
    # multiple scores from one sourcefile into multiple outfiles
    svg_extension = '001.svg'

    relative_filename = os.path.join(self.builder.imgpath, 'abcnotation', base_filename + svg_extension)
    absolute_filename = os.path.join(self.builder.outdir, '_images', 'abcnotation', base_filename + svg_extension)

    # If we rendered this exact abc snippet already, return that result.
    if os.path.isfile(absolute_filename):
        return relative_filename

    if not hasattr(self.builder, '_abcnotation_tempdir'):
        tempdir = self.builder._abcnotation_tempdir = tempfile.mkdtemp()
    else:
        tempdir = self.builder._abcnotation_tempdir

    abcm2ps_infile = os.path.join(tempdir, base_filename + '.abc')
    with open(abcm2ps_infile, 'w') as fp:
        fp.write(abc_source)

    ensuredir(os.path.dirname(absolute_filename))

    # Prepare command and arguments
    abcm2ps_outfile = os.path.join(tempdir, base_filename)
    args = ['abcm2ps', '-g', '-q', abcm2ps_infile, '-O', abcm2ps_outfile]

    subprocess.run(args, check=True, capture_output=True)

    shutil.copyfile(abcm2ps_outfile + svg_extension, absolute_filename)

    return relative_filename


def visit_abc_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='abc-music'))
    filename = render_abc(self, node['abc_source'])
    self.body.append(f'<img src="{filename}"/>')


def depart_abc_html(self, node):
    self.body.append('</div>')


class AbcDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        node = abc()
        node['abc_source'] = '\n'.join(self.content)
        return [node]


def cleanup_tempdir(app, exception):
    if exception:
        return
    if not hasattr(app.builder, '_abcnotation_tempdir'):
        return
    try:
        shutil.rmtree(app.builder._abcnotation_tempdir)
    except Exception:
        pass


def setup(app):
    app.add_node(abc, html=(visit_abc_html, depart_abc_html))

    app.add_directive('abc', AbcDirective)
    app.connect('build-finished', cleanup_tempdir)
