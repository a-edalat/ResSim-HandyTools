import os
from datetime import datetime

file_path = 'The Path to the folder containig the file'
file_name = 'ConvertOldObsToVol.csv'
export_file = 'final_vol_file.vol'

# This retruns a list of the line splited based on the given criteria
def split_func(line, sep):
    line = line.strip()
    return line.split(sep)

column = 1 # Column is used to read GRAT, WRAT and THP of each well in each pass
row= 0     # row is used so all the dates are added correctly as it reads through the files
final_file = "\n".join(['*FIELD','*DAILY','*IGNORE_MISSING', '*DAY *MONTH *YEAR *GAS *WATER *BHP *WATER_GAS_RATIO']) + '\n' # Creating the haeder for the Vol file

# The idea here is a loop that reads the file few times, each pass it reads the well name and then 
# it creates *NAME for the well name, plus convert the three column to three values of Gas, Water rate
# and THP    
while column < 85:    
    with open(os.path.join(file_path, file_name), 'r') as olderObs_data:
        for line in olderObs_data:
            del_line = split_func(line, ',')
                        
            if row == 0:
                well_name = del_line[column]
                final_file = final_file + '\n' + '*NAME' + ' ' + well_name + '\n'
            elif row > 1:
                date = datetime.strptime(del_line[0],'%d/%m/%Y').strftime('%d %m %Y')
                grat = del_line[column]
                wrat = del_line[column + 3]
                line_pressure = del_line[column + 1]
                wgr = del_line[column + 2]
                final_file = final_file + date + " " + grat + " " + wrat + " " + line_pressure + " " + wgr + '\n'
                
            row += 1
    
    column += 4
    row = 0

open(export_file,"w+").write(final_file)