import os
from datetime import datetime

file_path = 'The Path to the folder containig the file'
input_schedule_file = 'CASEXXX_INCLUDE.SCH'
export_vol_file = 'final_vol_file.vol'


Well_names = ['WEL000'] # list of the wells to be extracted and added to the VOL file

# Creating the haeder for the Vol file
final_file = "\n".join(['*FIELD','*DAILY','*IGNORE_MISSING',  
                        '*DAY *MONTH *YEAR *GAS *WATER *BHP']) + '\n'

with open(os.path.join(file_path, input_schedule_file)) as original_sch:
    sch_lines = original_sch.readlines()
    
    #DATES_loc list contains all the dates added to schedule using DATES keyword
    DATES_loc = [index+1 for index, element in enumerate(sch_lines) if element.strip() == 'DATES']
    
    listOfDates_unf  = [sch_lines[item].strip()[:-4] for item in DATES_loc] #I store them as 'they are' in a list
    
    listOfDates_f    = [datetime.strptime(listOfDates_unf[index],'%d   %b   %Y').strftime('%d %m %Y') 
                       for index, element in enumerate(listOfDates_unf)] #format them to match vol file requirements
    
    # logic here needs a rework, currently it works based on user knowning what order the wells have been exported. under WCONHIST
    WCONHIST_loc_WELXXX= [index+1 for index, element in enumerate(sch_lines) if element.strip() == 'WCONHIST'] #WCONHIST location
    
    listOfWLEXXX    =  [sch_lines[item].strip() for item in WCONHIST_loc_WELXXX]
    
for well in Well_names:
    final_file = final_file + '*NAME ' + well + '\n'
        
    for i, e in enumerate (listOfWLEXXX):
        gas_rate   = e.split(" ")[12] 
        water_rate = e.split(" ")[15] 
        bhp        = e.split(" ")[21]
        
        if bhp == '1*':
            bhp = str(0)

        line = listOfDates_f[i] + " " + water_rate + " " + gas_rate + " " + bhp +'\n'
        final_file = final_file + line
        
with open(r'path on where to store the vol file\WLE003.vol', 'w+') as vol_file:
    for item in final_file:
        vol_file.write(item)
        
print('complete')