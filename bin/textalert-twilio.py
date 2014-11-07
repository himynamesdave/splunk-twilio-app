#!/opt/splunk/bin/python
# - or -
#!C:\progra~1\Splunk\bin\python
# Top line: very important. Should be /opt/splunk/bin/python on *nix or C:\progra~1\Splunk\bin\python on *indows.
# Edit for your Splunk location, but no spaces are allowed (annoyingly.)

#
# textalert-twilio.py: A script to send Splunk alerts via SMS using Twilio.
# Twilio is a cloud-based communications service that can send and receive calls and texts on demand.
#

# Other editable items:
# Please enter in your Twilio account SID and Auth Token below - these are found at the 
# top of your dashboard at https://www.twilio.com/user/account 
twilioID = "AC________________________________"
twilioPW = "________________________________"

# Enter the number to send the SMS to, including international dial code
toNumber = "+___________"

# Enter the number to send the SMS FROM - it must be a Twilio-provided number or short code, not Verified number
fromNumber = "+___________"

# Enter the text to show before the "reason the alert kicked off" - the search name and alert criteria.
alertText = "Splunk Alert:"


#################################################
# Should not need to be edited below this line.
#
import sys, urllib, urllib2
# Parameters passed in from the alert.
# $1-$9 is the positional parameter list.
searchCount = sys.argv[1] # $1 - Number of events returned
searchTerms = sys.argv[2] # $2 - Search terms
searchQuery = sys.argv[3] # $3 - Fully qualified query string
searchName = sys.argv[4] # $4 - Name of saved search
searchReason = sys.argv[5] # $5 - Reason saved search triggered
searchURL = sys.argv[6] # $6 - URL/Permalink of saved search
searchTags = sys.argv[7] # $7 - Always empty as of 4.1
searchPath = sys.argv[8] # $8 - Path to raw saved results in Splunk instance (advanced)

d = urllib.urlencode({"From" : fromNumber, "To" : toNumber, "Body" : alertText + " "+searchReason})
pwm = urllib2.HTTPPasswordMgrWithDefaultRealm()
pwm.add_password("Twilio API", "https://api.twilio.com/2010-04-01/Accounts/", twilioID, twilioPW)
hnd = urllib2.HTTPBasicAuthHandler(pwm)
opn = urllib2.build_opener(hnd)
f = opn.open("https://api.twilio.com/2010-04-01/Accounts/" + twilioID + "/SMS/Messages", d)