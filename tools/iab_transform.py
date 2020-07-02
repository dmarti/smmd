import json
import datetime
import csv
import sys
import os
from urllib.parse import urlparse

# input files - directory
inputfile = 'iab.json' #this should be a json file - use to specify an individual file
output_path = '' # specify location for output - this needs to exist/will not be automatically created
output_name = 'iab_cleanup_'
rows_processed = 0

outputfile = output_path + output_name + str(datetime.datetime.now()).replace(' ', '_').split('.')[0] + '.csv'

# Create csv file, add header
with open(outputfile, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    header = ['iab_id', 'name', 'policy', 'domain', 'homepage', 'purps', 'legids', 'featids', 'flag'] # update header values as needed
    writer.writerow(header)

# add data to csv file
def write_csv(row_data, outputfile):
    with open(outputfile, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row_data)

# Read in the json: 
with open(inputfile) as json_file:
    data = json.load(json_file)
    companies = data['vendors']
    for c in companies:
# housekeeping
        rows_processed += 1
        purpose_ids = []
        purps = []
        legit_ids = []
        legids = []
        feat_ids = []
        featids = []
        flag = 0
# getting to work
        iab_id = c['id']
        name = c['name']
        policy = c['policyUrl']
        url_object = urlparse(policy)
        domain = url_object.netloc
        homepage = url_object.scheme + '://' + url_object.netloc
# Convert purpose ids
        purpose_ids = c['purposeIds']
        for pids in purpose_ids:
            if pids == 1:
                purps.append('Information storage and access')
            elif pids == 2:
                purps.append('Personalisation')
            elif pids == 3:
                purps.append('Ad selection, delivery, reporting')
            elif pids == 4:
                purps.append('Content selection, delivery, reporting')
            elif pids == 5:
                purps.append('Measurement')
# Convert legit ids
        legit_ids = c['legIntPurposeIds']
        for lids in legit_ids:
            if lids == 1:
                legids.append('Information storage and access')
            elif lids == 2:
                legids.append('Personalisation')
            elif lids == 3:
                legids.append('Ad selection, delivery, reporting')
                flag += 1 # trap for GDPR
            elif lids == 4:
                legids.append('Content selection, delivery, reporting')
            elif lids == 5:
                legids.append('Measurement')            
# Convert feature ids
        feat_ids = c['featureIds']
        for fids in feat_ids:
            if fids == 1:
                featids.append('Matching Data to Offline Sources')
            elif fids == 2:
                featids.append('Linking Devices')
            elif fids == 3:
                featids.append('Precise Geographic Location Data')
        print(iab_id)
        print(name)
        print(' --- ')
        write_csv([iab_id, name, policy, domain, homepage, purps, legids, featids, flag], outputfile)
    print ("{0} rows processed.".format(rows_processed))
    print('Done.')