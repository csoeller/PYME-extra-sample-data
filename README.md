# Example data (and a little code) for PYME localisation data handling

This repo aims to collect PYME localisation data examples and some useful
code tidbits.

For details about the PYthon Microscopy Environment (PYME) please
refer to <https://python-microscopy.org>.

## Rationale

We aim to have a largish collection of interesting data examples and
code that explores how to handle this data in notebooks (rather than
the GUI applications that also come with PYME). The term _largish_ will
probably be constrained by the intent to keep the data in one git
repository hosted on github.

The focus is _not_ on providing minimal and as small as possible data
sets, rather _big enough_ and _interesting_ are the guiding
considerations.

The data should also be of utility to check the ability of PYME to
correctly open and interpret this data.

It is possible that a smaller core set of example data sets for PYME will be
assembled into their own repository, but that is up to the core PYME
development team to decide. If created, this may or may not overlap
with the data sets assembled in this _PYME extra data set repository_.

## Required packages to run the code examples

We generally require PYME, see <https://python-microscopy.org>. In
addition, some examples may require the
[PYME-extra](https://github.com/csoeller/PYME-extra) plugin package,
available at github.

We will aim to point out which notebooks require external
code. Initially, as we develop this repository, the code examples may
not all point out dependencies correctly.

## Structure

There is a data subtree with example data from various sources. We
will strive to document a little about the origin of the data in
readme files in the respective directories.

We also intend to maintain some example code how to convert, access
and manipulate the example data. These should also serve as reminders
how to programmatically access SMLM data files outside the VisGUI
graphical application. This is a useful mode for power users and also
has the great advantage to be able to _replay_ an action without the
clicking and selecting functionality in the GUI. 

Needless to say, this will likely remain a _work in progress_.

## Author

[Christian Soeller](https://soellerlab.ex.ac.uk)
