import os, sys, zipfile

export_path =  'Path to the folder of choice' 
read_path = r'Mepo project\CycleName\SAVE'   # This is the path to SAVE folder in MEPO direcotry

obifilename = 'PROB_FCST.OBI'           # What name is your OBI file, it should be the same as Cycle name
CommonName_MEPOfolder = 'PROB_FCST_4_'  # Which of the studies you want this to be extracted, in this example
                                        # it was iteration 4

Parameter2extract = "Parameter 'M7_[GGPT/GGPTH@ATP606]'"  # what parameter you wish to extract

# time_list contains a list of the abcsecia you wish to extract
time_list = ['1704.0','2432.0']

final_values = []

for i in range (1,100):
    zipfile_name = read_path + '/' + CommonName_MEPOfolder + str(i) + '.zip'
    with zipfile.ZipFile(zipfile_name) as obizip:
        for filename in obizip.namelist():
            if obifilename == filename and not os.path.isdir(filename):
                    # reads the file to a list
                with obizip.open(filename) as obi_file:
                    obi_content = obi_file.readlines()
    
    obi_content = [x.strip() for x in obi_content] # cleaning the list
    obi_content = [obi_content[i].decode('ascii') for i, item in enumerate(obi_content) ] # converting bytes to string

    chopping_start=obi_content.index(Parameter2extract)
    chopping_end_L=[i for i, x in enumerate(obi_content) if x == '' and i > chopping_start] # returns line numbers after chop start
    chopping_end  = chopping_end_L[0]

    obi_content_interest = obi_content[chopping_start:chopping_end] #the portion of interest in original obi file

    for line in obi_content_interest:
        line = line.split('\t')
    
        if len(line) > 6:
            if line[1] in time_list:
                final_values = final_values + [line[3]] # append was returning none, quick fix before I investigate why
    final_values = final_values + ["\n"]
    
with open(os.path.join(export_path, "extracted_vector.txt"), 'w+') as final_vals:  #export and save the extracted data.
    for line in final_values:
        final_vals.write(line + ', ')
print('complete')