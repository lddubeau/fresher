Possible mechanism for loading steps:

* ``runpy.run_modules()`` requires a ``__main__.py`` and does not
  handle two modules with the same name.

* ``runpy.run_path()`` is even more problematic.
