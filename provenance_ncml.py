#! /usr/local/bin/python
import json
import netCDF4 as nc
import os

save_dir = '/Users/michaesm/Downloads/'
ncml_file='/Users/michaesm/Downloads/CE04OSPS-SF01B-2A-CTDPFA107-streamed-ctdpf_sbe43_sample-20150906T000000-20150909T120000.nc'
# ncml_file = 'http://opendap-devel.ooi.rutgers.edu:8090/thredds/dodsC/eov-3/Coastal_Endurance/CE04OSPS/2A-CTDPFA107/streamed/CE04OSPS-SF01B-2A-CTDPFA107-ctdpf_sbe43_sample-streamed/CE04OSPS-SF01B-2A-CTDPFA107-ctdpf_sbe43_sample-streamed.ncml'
# ncml_file = 'http://opendap-devel.ooi.rutgers.edu:8090/thredds/dodsC/eov-3/Coastal_Endurance/CE05MOAS/05-CTDGVM000/recovered_host/CE05MOAS-GL311-05-CTDGVM000-ctdgv_m_glider_instrument_recovered-recovered_host/CE05MOAS-GL311-05-CTDGVM000-recovered_host-ctdgv_m_glider_instrument_recovered-20141216T185931-20141216T185952.nc'
# ncml_file = '/Users/michaesm/Downloads/CE05MOAS-GL311-05-CTDGVM000-recovered_host-ctdgv_m_glider_instrument_recovered-20141216T185931-20141216T185952.nc'
# ncml_file = '/Users/michaesm/Downloads/CE04OSPS-SF01B-3A-FLORTD104-streamed-flort_d_data_record-20151005T000000-20151011T235959.nc'
# ncml_file = '/Users/michaesm/Downloads/CE04OSPS-SF01B-2A-CTDPFA107-streamed-ctdpf_sbe43_sample-20150805T120000-20150808T235959.nc'
# ncml_file = '/Users/michaesm/Downloads/CE04OSPS-SF01B-3A-FLORTD104-streamed-flort_d_data_record-20151207T000000-20151207T221815.nc'

def read_json(open_file, var_name):
    qp = nc.chartostring((open_file.variables[var_name][:]))

    try:
        parsed_json = json.loads(qp[0])
        return parsed_json
    except:
        parsed_json = 'n/a'
        return parsed_json

def parse_json_response(content):
    for key, value in content.iteritems():
        print str(key) + ": " + str(value)

        if type(value) is dict:
            parse_json_response(value)

file_name = os.path.basename(ncml_file)
print "Printing provenance information for " + file_name
print "key : Value"
file_load = nc.Dataset(ncml_file)
prov_list = [s for s in file_load.variables if 'provenance' in s]
prov_list = [s for s in prov_list if not 'keys' in s]

for var in prov_list:
    try:
        p_json = read_json(file_load, var)
    except ValueError:
        continue

    save_file = os.path.join(save_dir, file_name)
    outfile = open(save_file + "-" + var + ".json", "w")
    json.dump(p_json, outfile)
    outfile.close()
