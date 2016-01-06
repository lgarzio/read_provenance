#! /usr/local/bin/python
import json
import netCDF4 as nc
import os

# Setup save directory and file
save_dir = '/Users/michaesm/Downloads/provenance/'
ncml_file='/Users/michaesm/Downloads/CE04OSPS-SF01B-2A-CTDPFA107-streamed-ctdpf_sbe43_sample-20150906T000000-20150909T120000.nc'

# grab file name for saving of json file
file_name = os.path.basename(ncml_file)
print "Printing provenance information for " + file_name
print "key : Value"
file_load = nc.Dataset(ncml_file)

# only list the provenance variables in the netcdf files
prov_list = [s for s in file_load.variables if 'provenance' in s]


# grab the provenance
var = 'computed_provenance'
qp = nc.chartostring((file_load.variables[var][:])) # convert character to string using netcdf4 toolbox
parsed_json = json.loads(qp[0]) # load string into json

# save the provenance
save_file = os.path.join(save_dir, file_name) # create save file name
outfile = open(save_file + "-" + var + ".json", "w") #create json file
json.dump(parsed_json, outfile) # dump json data into the .json file
outfile.close() # close the file.


