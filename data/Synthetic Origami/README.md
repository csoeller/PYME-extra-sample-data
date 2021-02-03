

# Data Description

## 2D synthetic DNA origami (6 die face) DNA-PAINT data set

This is a region from a DNA-PAINT Origami data set which has 6 sites in the arrangement of the face of a die.

## Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       | `130919_sA(ROI+fiducials).hdf` |
| **Sample (tissue/cell type):**            |  Synthetic origami                          |
| **Sample prep., fixation method:**        |  DNA-PAINT (D1 sequence)      |
| **Primary Ab, concentration/dilution:**   |  N/A    |
| **Secondary Ab, concentration/dilution:** |  N/A            |
| **Fiducial (type/present):**              |   200 nm Red fiducial used               |
| **SR mode, Imager conc, buffer, etc:**    |    600 mM NaCl in PBS (pH=8.0). 2 nM ATTO 655 (P1) imager sequence     |
| **Number of frames:**                     |   150.5k frames, 100ms/frame             |

**Note**: Some further data is available from the metadata in the `h5r` file. Please consult the metadata tab in `visGUI`.

### Notes

Sample was washed approximately halfway through and replaced with the same imaging buffer for the second half of the experiment..
   
### Supplied recipe

We supply a recipe `Recipe to correct and filter series 130919_sA.yaml` that can be loaded in visGUI and does some basic filtering plus drift correction. Events are coalesced and non-specific events (based on a temporal filter) are removed. Select the `ROI` data source to see the drift corrected data. 
