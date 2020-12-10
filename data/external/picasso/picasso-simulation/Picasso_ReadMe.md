# Data Description

## Picasso generated simulation data

Here we supply some synthetic data generated with picasso and how to manipulate it to read it with PYME.

### Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       |   origami-simul3_locs.hdf     |
| **Sample (tissue/cell type):**            |   simulated data                        |
| **Sample prep., fixation method:**        |     simulated DNA origami data                      |
| **Primary Ab, concentration/dilution:**   |       N/A                    |
| **Secondary Ab, concentration/dilution:** |        N/A                   |
| **Fiducial (type/present):**              |      simulated data is drift free                    |
| **Imager, concentration:**                |          3.0 nM? (see picasso yaml file)                 |
| **Number of frames:**                     |          7500 (see picasso yaml file)                 |


### Notes

This is purely simulated data. Picasso was used to simulate a 6 spot DNA origami that contains docking strands in the pattern of a 6 on a dice. All the simulations settings can be gleaned from the accompanying picasso yaml file.

**Note** that the `.hdf` file is **not** a PYME readable hdf, rather it is the output from picasso and we need to convert it to become readbale by PYME.

The accompanying Jupyer notebook shows how to process the picasso hdf file to generate a PYME redable file in csv format. That file of localisations is then rendered and the yaml file also processed to generate a histogram of the number of intact spots on the simulated origami (with between 1 and 6 spots).

### Supplied recipe [optional]

We do not supply a VisGUI recipe for this data set as no major corrections need to be carried out. Note that there is a YAML file in the folder, however, this YAML file is the metadata from the Picasso simulation, **not** a VisGUI recipe.

Running the notebook will generate a file `origami-simul3_locs.csv` in the `build` subfolder. You can open this file with VisGUI and see the detected events in the usual way. To import just ok the offered dialogue.

