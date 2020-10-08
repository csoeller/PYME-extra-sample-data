# MT STORM data set #

This is a STORM microtubule data set. We include a recipe (YAML file)
that includes some basic drift correction.

# Sample and acquisition information: #

1'Ab: Beta tubulin

2'Ab: Alexa Fluor 647

Type: dSTORM

Buffer: mM MEA in 90% glycerol

Camera: Zyla-4.2-CL10 (Andor sCMOS)

Integration time:  25 ms

Total duration (frames): 35.4k  


## ToDo

1. The drift correction is currently based on one of our non-free
   modules . It should be possible to replace this with a general
   linear (and/or piecewise linear) drift correction module that takes
   pre-determined parameter values that are just statically stored in
   the recipe.


