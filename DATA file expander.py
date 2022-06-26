import os

file_name = 'DATA file name goes here'
path = r'The path to the folder containing DATA file goes here'

if file_name[-5:] == '.DATA':
    pass
else:
    ext_ind = file_name.find('.')  # Making sure the DATA file has the correct extension

    if ext_ind > 0:
        file_name = file_name[:ext_ind] + '.DATA'
    else:
        file_name = file_name + '.DATA'

file = os.path.join(path, file_name)
final_file = []

def expander(data_file):

    flag = 0      # flags where include files
    grid_flag = 0 # grid info can be excluded here so the final file is smaller and easier to work with
                  # if grid files are needed set this number to any number except 0
    include = os.path.join(path, data_file)
        
    with open(include, 'r') as inc:
        for item in inc:
            
            if item[:7] == 'INCLUDE':
                flag = 1
                continue
                    
            elif flag == 1 and grid_flag != 1 and item[:2] != "--" and item[0] != '\n':
                loc  = item.find('/')     # finding the path to the include
                item = item[:loc].strip() # removing spaces and new lines from the path
                item = item.strip("'")    # removing the qoutations from the path name
                expander(item) # recursive function if there is other includes within this include
                flag = 0       # flag back to zero so the lines can be writtern now
                continue
                        
            elif item[:5] in ['COORD', 'ZCORN'] and grid_flag == 0:
                grid_flag = 1
                continue
                
            elif item.strip() == "/" and grid_flag == 1:
                grid_flag = 0
                continue
            
            elif grid_flag != 1:
                final_file.append(item)
                        
    return final_file

with open(os.path.join(path, file_name[:-5]) + '_EXPANDED.DATA', 'w+') as output:
    output.writelines(expander(file_name))

print('You can check the expanded DATA file in the following path: ')
print(os.path.join(path, file_name[:-5]) + '_EXPANDED.DATA')