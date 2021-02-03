# Data Description

## 3D (biplane) surface RyR DNA-PAINT data set

This is a region from a DNA-PAINT RyR 3D data set.  

## Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       | `030320_sF(ROI+fiducial).hdf` |
| **Sample (tissue/cell type):**            |  Isolated cardio myocytes              |
| **Sample prep., fixation method:**        |  2% PFA fixed            |
| **Primary Ab, concentration/dilution:**   |  RyR (MA3-916)     |
| **Secondary Ab, concentration/dilution:** |  goat anti-mouse with 9bp (P5) functionalized docking sequences present            |
| **Fiducial (type/present):**              |   Fiducial present. 200 nm Red.                          |
| **SR mode, Imager conc, buffer, etc:**    |    DNA-PAINT, 1 nM P1 ATTO 655 imager in 500 mM NaCl in PBS (pH=8.0)     |
| **Number of frames:**                     |   76.8k frames, 100ms/frame             |

**Note**: Some further data is available from the metadata in the `h5r` file. Please consult the metadata tab in `visGUI`.

### Notes

Information: 50/50 beam splitter. 3 m len in short path. Shift corrected prior to imaging using a densely populated bead slide and calculated with a shiftfield. PSF obtained from beads in the sample.

   
### Supplied recipe

We include a recipe `recipe to drift correct and filter 030320.yaml` that corrects for drift using the fiducial present in the data. Select the `ROI` data source to see the drift corrected data.

