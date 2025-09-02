import numpy as np

####################################################################
## This class defines the spacecraft for the simulation
## 
## Early version will only be concerned with the Field of View FOV
## for the spacecraft.
##
####################################################################

class spacecraft:
    def __init__(spacecraft):
        ## Default spacecraft position will be 0 latitude and langitude
        spacecraft.lat = 0
        spacecraft.long = 0
        spacecraft.altitude = 1000 ## Altitude in km

        spacecraft.fov = 148.45 ## This is in degrees
                             ## For now do the stupid thing of say spacecraft can see a cone with the
                             ## payload at the apex of the cone. The fov is the opening angle of the cone
                             ## Since a real spacecraft will likely only see CRs at the horizon, this really
                             ## should be a band that goes around the horizon
