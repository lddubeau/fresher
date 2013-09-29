- With behave, as of 20130927, try to do something like this in a step
  file:

from . import util

That's because the step files are not imported like modules but
exec'ed. Fresher does not prevent relative imports.
