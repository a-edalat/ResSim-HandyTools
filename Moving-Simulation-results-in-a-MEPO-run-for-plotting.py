# this script should be added to mepo post process, move the vectors to a different folder
# under unique name to be plotted in Petrel
from shutil import copyfile
import os

#Your simulation name goes here, this is the common name used by MEPO for all cases (cycle name)
sim_name = 'PROJ'

for i in range (1,1000):
    path = r'Mepo Path\Cycle name\experiment_002_' + str(i).zfill(4) + '_000'
    print(path)
    name = path[-12:]

    try:
        #copyfile(sim_name + '.DATA',   path[:-23] + 'Petrel_Results/' + name + '.DATA' )
        copyfile(sim_name + '.UNSMRY', path[:-23] + 'Petrel_Results/' + name + '.UNSMRY' )
        copyfile(sim_name + '.SMSPEC', path[:-23] + 'Petrel_Results/' + name + '.SMSPEC' )
    except FileNotFoundError:
        print (name)
        continue