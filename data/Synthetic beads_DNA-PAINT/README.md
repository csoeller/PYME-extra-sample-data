# Data Description

## Synthetic beads

Streptavidin-coated Polystyrene particles, biotin modified. Conjugated to a P1P3e docking strand for DNA-PAINT, this series utilised a P1 imager. The folder contains a basic recipe for drift correction and coalescing.

## Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       | `12_3_21_series_C.h5r` |
| **Sample (tissue/cell type):**            |  Synthetic beads                           |
| **Sample prep., fixation method:**        |  N/A          |
| **Primary Ab, concentration/dilution:**   |  N/A     |
| **Secondary Ab, concentration/dilution:** |  N/A            |
| **Fiducial (type/present):**              |   present                         |
| **SR mode, Imager conc, buffer, etc:**    |    DNA-PAINT, 0.1nM P1 655, 1x TE + 600mM NaCl     |
| **Number of frames:**                     |   38k frames, 100ms/frame             |

**Note**: Some further data is available from the metadata in the `h5r` file. Please consult the metadata tab in `visGUI`.

### Notes
   
### Supplied recipe

We supply a recipe `recipe for drift correction_coalescing.yaml` that can be loaded in visGUI and does some basic filtering plus drift correction. Select the `fiducialApplied` data source to see the drift corrected data. 

