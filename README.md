# Sphinx ABC Notation

This extension adds an `abc` directive to Sphinx in order to write sheet music
as text.  The content of the directive will be rendered to SVG by
[abcm2ps](https://github.com/leesavide/abcm2ps) and included in the rendered
document.

## Usage

```rst
Here are some inversions of a D-major triad.

.. abc::

    X:1
    L:1/4
    K:C
    "Root position"[D^FA] [DA^f] | "First inversion"[^FAd] [^Fda] | "Second inversion"[Ad^f] [Ad'^f] |
    w: closed open closed open closed open
```

Here are some inversions of a D-major triad.

![](example.svg)

## Install

0. Install [abcm2ps](https://github.com/leesavide/abcm2ps).
1. Install this extension: `pip install sphinx_abcnotation --user`
2. Edit `conf.py` to include `sphinx_abcnotation` in the `extensions` list:

    ```
    extensions = ['sphinx_abcnotation']
    ```

3. Use the `.. abc ::` directive in your reStructuredText documents.

For info on abc notation itself I recommend [this page by Steve
Mansfield](http://www.lesession.co.uk/abc/abc_notation.htm).
