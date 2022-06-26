import os
import pandas as pd
from datetime import datetime

file_path = 'The Path to the folder containig the file'
file_name_gas = 'ConvertGasObsToVol.csv'
file_name_wat = 'ConvertWatObsToVol.csv'
export_file = 'final_vol_file.vol'

df_g = pd.read_csv(os.path.join(file_path,file_name_gas))
df_w = pd.read_csv(os.path.join(file_path,file_name_wat))


list_of_wells = list(df_g) # Getting the list of the well names
list_of_wells = list_of_wells[1:]

final_file = "\n".join(['*FIELD','*DAILY','*IGNORE_MISSING','*DAY *MONTH *YEAR *GAS *WATER']) + '\n'

# Combining all values and re-formatting DATE
for wells in list_of_wells:
    final_file = final_file + '\n' + '*NAME' + ' ' + wells + '\n'
    for i in range (len(df_g['DATE'])):
        dates = datetime.strptime(str(df_g['DATE'][i]),'%d/%m/%Y').strftime('%d %m %Y')
        final_file = final_file + dates + " " + str(df_g[wells][i]) + " " + str(df_w[wells][i]) + '\n'

open(export_file,"w+").write(final_file)