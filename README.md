# Sphinx ABC Notation

This extension adds an `abc` directive to Sphinx. The content of the directive
will be rendered to SVG by [abcm2ps](https://github.com/leesavide/abcm2ps) and
included in the rendered document.

## Usage

```rst
Here are 12 notes on a staff.

.. abc::

    X:1
    L:1/4
    K:C
    A, ^A, B, C ^C D ^D E F ^F G ^G
    w: a a♯ b c c♯ d d♯ e f f♯ g g♯
```

Here are 12 notes on a staff.

![](example.svg)

## Install

1. `pip install sphinx_abcnotation --user`
2. Edit `conf.py` to include `sphinx_abcnotation` in the `extensions` list:

    ```
    extensions = ['sphinx_abcnotation']
    ```

3. Use the `.. abc ::` directive in your reStructuredText documents.
