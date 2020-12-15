# Data Description

## MT STORM data set

This is a STORM microtubule data set. We include a recipe (YAML file)
that includes some basic drift correction.

## Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       | `16_1_series_BB_microtubules_STORM.h5r` |
| **Sample (tissue/cell type):**            |  COS-7 cells                           |
| **Sample prep., fixation method:**        |  PFA fixed (duration, conc)?           |
| **Primary Ab, concentration/dilution:**   |  anti-beta-tubulin (manufacturer?)     |
| **Secondary Ab, concentration/dilution:** |  Alexa Fluor 647 anti-mouse            |
| **Fiducial (type/present):**              |   not present                          |
| **SR mode, Imager conc, buffer, etc:**    |    dSTORM, ?mM MEA in 90% glycerol     |
| **Number of frames:**                     |   35.4k frames, 25ms/frame             |

**Note**: Some further data is available from the metadata in the `h5r` file. Please consult the metadata tab in `visGUI`.

### Notes

The drift correction is currently based on one of our non-free
   modules. It should be possible to replace this with a general
   linear (and/or piecewise linear) drift correction module that takes
   pre-determined parameter values that are just statically stored in
   the recipe.
   
### Supplied recipe

We supply a recipe `16_1_series_BB.yaml` that can be loaded in visGUI and does some basic filtering plus drift correction. Select the `drift_corrected` data source to see the drift corrected data. 

