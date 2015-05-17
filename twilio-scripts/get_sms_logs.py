#!/usr/bin/env python
# Top line: very important. Must have Twilio python library installed (https://www.twilio.com/docs/python/install)
import os
import sys
import codecs
from datetime import datetime, date
from twilio.rest import TwilioRestClient

ACCOUNT_SID = '$MY_ACCOUNT_SID'
AUTH_TOKEN   = '$MY_AUTH_TOKEN'
LOG_FILE        = 'sms_log.csv'
LAST_ENTRY    = None # "LAST_ENTRY" helps us to read log from the last date we have fetched
RECORDS        =  []

def get_last_entry():
    global LAST_ENTRY
    if LAST_ENTRY:
        tstamp = LAST_ENTRY
    elif os.path.exists(LOG_FILE):
        # let's read "LAST_ENTRY" from the file
        with codecs.open(LOG_FILE) as f:
            line = f.readlines()[-1]
            tstamp = line.split(',')[2]
            LAST_ENTRY = tstamp
    else:
        #no "LAST_ENTRY" in mem or file. Let's create a header and a safe file
        add_header()
        tstamp = 'Mon 03 Jan 2000 00:00:00 +0000'
        LAST_ENTRY = tstamp
        
    ts = ' '.join(tstamp.split()[1:4])
    date_object = datetime.strptime(ts, '%d %b %Y')
    print 'LAST_ENTRY ', date_object
    return date_object

def get_logs(date_object):
    del RECORDS[:]
    i  = 0
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sms_list =  client.messages.list()
    for sms in sms_list:
        record = [sms.body,  sms.status,  ' '.join((sms.date_sent).split(',')),  sms.api_version,  sms.num_segments,  \
                sms.account_sid,  sms.sid,  sms.direction,  sms.from_, sms.to,  sms.price,  sms.price_unit]
        record2 = [x or '' for x in record ]
        final = ','.join(record2)
        RECORDS.append(final)
        if i == 0:
            LAST_ENTRY = ' '.join((sms.date_sent).split(','))
        i+=1
        
    write_records()
    
def write_records():
    # avoid duplicates
    data = []
    if os.path.exists(LOG_FILE):
        with codecs.open(LOG_FILE) as d:
            file_data = d.readlines()
            for line in file_data:
                date = line.split(',')[2]
                #if  date == LAST_ENTRY:
                data.append(date)
                
    with codecs.open(LOG_FILE, 'a') as f:
        for record in reversed(RECORDS):
            if not record.split(',')[2] in data:
                f.write(record)
                f.write('\n')
    
def add_header():
    header = 'Body,Status,SentDate,ApiVersion,NumSegments,AccountSid,Sid,Direction,From,To,Price,PriceUnit'
    if not os.path.exists(LOG_FILE):
        with codecs.open(LOG_FILE, 'w') as f:
            f.write(header)
            f.write('\n')
    
if __name__ == '__main__':
    date_object = get_last_entry()
    get_logs(date_object)
    sys.exit()
