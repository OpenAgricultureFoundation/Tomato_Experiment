# Get the unique variable names from the raw data file

filenames = {"control_pfc": "../raw_data/Hidden-Snow_1-2-2020--3-2-2020.csv",
             "with_basil_pfc": "../raw_data/Aged-Shape_1-2-2020--3-2-2020.csv",
             "blue_night_pfc": "../raw_data/Blue-Water_1-2-2020--3-2-2020.csv"}

# the file has the following columns: 
# device,report_time,var,name,value,values
#  we're interest in splitting out the var into individual files.

# create files for each var/name set.
def genfilename(varname):
    if varname[1] != "URL":
        return varname[0] + "_" + varname[1] + ".csv"
    else:
        return "Camera-Top.csv"

# First pass is we'll get all the var names


for file_key in filenames.keys():
    filename = filenames[file_key]
    print("Getting Unique Vars")

    varnames = []
    with open(filename, "r") as f:
        for line in f.readlines():
            linesplit = line.split(',')
            if [linesplit[2],linesplit[3]] not in varnames and linesplit[2] != 'var':
                varnames.append([linesplit[2],linesplit[3]])
                print("Found var name: " + linesplit[2] + " - " + linesplit[3])

    print ("Done finding vars")

    readings_files = {}
    for vn in varnames:
      readings_files[genfilename(vn)] = open(file_key + "-" + genfilename(vn),'w')
      readings_files[genfilename(vn)].write("variable,sensor_name,timestamp_utc,value,value_json\n")

    # loop through main raw data generating the new datafiles
    with open(filename,'r') as f:
        for line in f.readlines():
            linesplit = line.split(',')
            # ignore device name
            report_time = linesplit[1]
            varname = linesplit[2:4]
            value = linesplit[4]
            values_json = ",".join(linesplit[5:])
            filename = genfilename(varname)
            if filename in readings_files.keys():
                newline = ",".join(varname + [report_time,value,values_json])
                readings_files[filename].write(newline)

    for f in readings_files.keys():
        readings_files[f].close()
