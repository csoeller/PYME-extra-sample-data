# Formats in this respository #

## PYME native

Natively, PYME uses an HDF5 format for the efficient storage of localisation data. This is plain HDF5 but follows a number of conventions so that both localisation, events and metadata can be stored in the same file. By convention, the files have the extension `.h5r`.

This follows the notion that having everything in one file that follows a scientific data format standard is the best of all worlds. No sets of files that need to stay together to ensure data integrity. I (CS) fully subscribe to this idea.

I am not sure PYME has a real data format spec but certainly PYME provides a reference implentation to read and write `.h5r` files.

## Picasso

We are encountering [picasso](https://github.com/jungmannlab/picasso) generated data files regularly these days. The goal is to add a bunch of example files in this format which also uses HDF5 but metadata is supplied in a yaml format.

**TODO**: I am not certain there is a formal format spec but will aim to link to the documentation part that explains the data format.

## CSV

PYME has a general CSV importer and we will aim to provide a bunch of examples for that, too.

## Others

There are probably more bespoke formats out there. Not sure if manufacturers make their format specs available but most will likely allow export to CSV or similar, which in turn will allow PYME to import as CSV.

### ThunderStorm

Thunderstorm appears to use a number of standard column names in a CSV format (among other formats), see the [info](http://www.neurocytolab.org/tscolumns/) collated by Christophe Leterrier.

More info seems to be on github: <https://zitmen.github.io/thunderstorm/>. I am not sure if the project is still in active development.
