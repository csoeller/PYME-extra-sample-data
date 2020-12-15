# Data Description

## 3D Quencher-Exchange-PAINT

3D using biplane mode via inserting a 2m lens into a splitter device to create ~250nm z shift. 

### Sample information

| Details                                   | Sample                    |
| ------------------------------------------|:-------------------------:|
| **File name/date:**                       |                   8.10.19 series C        |
| **Sample (tissue/cell type):**            |     cardiac LV pig tissue                      |
| **Sample prep., fixation method:**        |    2% PFA, 1h, 4°C                    |
| **Primary Ab, concentration/dilution:**   |       RyR (MA3-916) - IP3R2 (HPA059144)  (1:100)           |
| **Secondary Ab, concentration/dilution:** |      goat anti-mouse/goat anti-rabbit conjugated DSs sharing a 9bp overlap                     |
| **Fiducial (type/present):**              |        200nm red bead                   |
| **Imager, concentration:**                |   P5-ATTO55-0.5nM, Quencher-50nM, P1-ATTO655-0.3nM                |
| **Number of frames:**                     |  round 1: IP3R2 t=30-50.6k round 2: RyR t=54.3k-80.7k frames          |


### Notes



### Supplied recipe

Recipe included uses fiducial based drift correction and assignes the correct protein to the respective frames, using the "TimedSpecies" module.

Notebook included merges the single binding events that were localised within a radius of 2.0x the localisation error and were on for a consecutive number of 5 frames. It then plots the "coalesced" events. 