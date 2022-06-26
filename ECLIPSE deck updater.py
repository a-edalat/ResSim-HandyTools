
import os

Petrel_Project_SimFolder_Path = "C:"
base_case_name = 'BASE_'       #as an example
includefile_name = '_SOL.INC' #as an example
starting_case_number = 9
final_case_number = 1026
search_keyword = 'RPTRST'
remove_line = False

for i in range (starting_case_number, final_case_number+1):
    case_name =    base_case_name + str(i)
    includefile = case_name + includefile_name
    
    print(i)

    include_file=open(os.path.join(Petrel_Project_SimFolder_Path,case_name,includefile), 'r')
    content = include_file.readlines()
    
    for j in range(0,len(content)):
        current_line = str(content[j])
        if remove_line == True:
            content[j] = "  'BASIC=0'  /" + "\n"
            remove_line = 0
            include_file.close
            break
        
        if current_line[:len(search_keyword)] == search_keyword and remove_line == False:
            remove_line = True
    
    with open(Petrel_Project_SimFolder_Path+"\\"+case_name+"\\"+includefile, 'w+') as file:
        for lines in content:
            file.write(lines)