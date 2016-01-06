#! /usr/local/bin/python
import json
import netCDF4 as nc
import os


files_dir = '/Users/michaesm/Downloads/test/'

def read_json(open_file, var_name):
    qp = nc.chartostring((open_file.variables[var_name][:]))

    try:
        parsed_json = json.loads(qp[0])
        return parsed_json
    except:
        parsed_json = 'n/a'
        return parsed_json

# def print_provenance(json_obj, sp_len):
#     # get json dictionary keys
#     # keys = json_obj.keys()
#
#     for key in json_obj.keys():
#         print key + ": " + str(json_obj[key]) + "\n"


def parse_json_response(content):
    for key, value in content.iteritems():
        print str(key) + ": " + str(value)

        if type(value) is dict:
            parse_json_response(value)

for root, dirs, files in os.walk(files_dir):
    for f in files:
        if f.endswith(".nc"):
            nc_file = os.path.join(root,f)
            # print ncFile
            print "Printing provenance information for " + nc_file
            print "key : Value"
            file_load = nc.Dataset(nc_file)
            prov_list = [s for s in file_load.variables if 'provenance' in s]
            prov_list = [s for s in file_load.variables if not 'keys' in s]

            for var in prov_list:
                p_json = read_json(file_load, var)
                outfile = open(nc_file + "-" + var + ".json", "w")
                json.dump(p_json, outfile)
                outfile.close()
                    # if p_json == 'n/a':
                    #     continue
                    # else:
                    #     parse_json_response(p_json)
                    #     json.dump(p_json)



# cp = nc.chartostring(f.variables['computed_provenance'][:])
# cp_parsed_json = json.loads(cp[0])
# cpK = cp_parsed_json.keys()
#
# ip = nc.chartostring(f.variables['instrument_provenance'][:])
# ip_parsed_json = json.loads(ip[0])
# ipK = ip_parsed_json.keys()
