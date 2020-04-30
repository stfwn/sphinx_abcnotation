# Sphinx ABC Notation

This extension adds an `abc` directive to Sphinx. The content of the directive
will be rendered to `svg` by [abcm2ps](https://github.com/leesavide/abcm2ps)
and included in the rendered document as an image.

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
