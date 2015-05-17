#!/usr/bin/env python
import os
import sys
import codecs
from datetime import datetime, date
from twilio.rest import TwilioRestClient

ACCOUNT_SID = '$MY_ACCOUNT_SID'
AUTH_TOKEN   = '$MY_AUTH_TOKEN'
LOG_FILE        = 'call_log.csv'
LAST_ENTRY    = None # "LAST_ENTRY" helps us to read log from the last date we have fetched
RECORDS        =  []


def get_last_entry():
    global LAST_ENTRY
    print LAST_ENTRY
    if LAST_ENTRY:
        tstamp = LAST_ENTRY
    elif os.path.exists(LOG_FILE):
        # let's read "LAST_ENTRY" from the file
        with codecs.open(LOG_FILE) as f:
            line = f.readlines()[-1]
            tstamp = line.split(',')[1]
            LAST_ENTRY = tstamp
    else:
        #no "LAST_ENTRY" in mem or file. Let's create a header and a safe timestamp
        add_header() 
        tstamp = 'Mon 03 Jan 2000 00:00:00 +0000'
        LAST_ENTRY = tstamp
        
    ts = ' '.join(tstamp.split()[1:4])
    print 'TS: ', ts
    date_object = datetime.strptime(ts, '%d %b %Y')
    print 'LAST_ENTRY ', date_object
    return date_object


def get_logs(date_object):
    del RECORDS[:]
    i  = 0
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call_list =  client.calls.list(status="completed", started_after=date_object)

    for call in call_list:
        record = [call.sid, ' '.join((call.date_created).split(',')), ' '.join((call.date_updated).split(',')), call.parent_call_sid,  call.account_sid, call.to,  call.to_formatted,  call.from_,  \
                call.from_formatted,  call.phone_number_sid, call.status, ' '.join((call.start_time).split(',')),  ' '.join((call.end_time).split(',')),  call.duration,  call.price,  call.price_unit, \
                call.direction,  call.answered_by,  call.annotation,  call.api_version,  call.forwarded_from,  call.group_sid,  call.caller_name,  call.uri]
        record2 = [x or '' for x in record ]
        final = ','.join(record2)
        RECORDS.append(final)
        if i == 0:
            LAST_ENTRY = ' '.join((call.date_created).split(','))
        i+=1
        
    write_records()
        
        
def write_records():
    # avoid duplicates
    data = []
    if os.path.exists(LOG_FILE):
        with codecs.open(LOG_FILE) as d:
            file_data = d.readlines()
            for line in file_data:
                date = line.split(',')[1]
                if  date == LAST_ENTRY:
                    data.append(date)
    with codecs.open(LOG_FILE, 'a') as f:
        for record in reversed(RECORDS):
            if not record.split(',')[1] in data:
                f.write(record)
                f.write('\n')

                
def add_header():
    header = 'Sid,DateCreated,DateUpdated,ParentCallSid,AccountSid,To,ToFormatted,From,FromFormatted,PhoneNumberSid,Status,\
            StartTime,EndTime,Duration,Price,PriceUnit,Direction,AnsweredBy,Annotation,ApiVersion,ForwardedFrom,GroupSid,CallerName,Uri'
    if not os.path.exists(LOG_FILE):
        with codecs.open(LOG_FILE, 'w') as f:
            f.write(header)
            f.write('\n')


if __name__ == '__main__':
    date_object = get_last_entry()
    get_logs(date_object)
    sys.exit()
