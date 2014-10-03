Twilio App for Splunk
=================

Welcome to the Splunk app for Twilio
-------------

**Thanks for downloading the Splunk app for Twilio** it's great to see you here. Introductions over, lets get down to business.

**Important:** this app will NOT work unless you follow the setup instructions below - they're super simple to setup, I promise.

__For your convenience, these instructions can also be found in the Splunk GUI once the app has been installed by visiting "help!" > "setup".__

I'm 12, what is this?
-------------

The Splunk app for Twilio comes in two parts.

1) The first part helps you to export your Twilio logs via the Twilio API and ingest them into Splunk. To help you get started this app comes prebuilt with searches powering a number of dashboards and alerts for the ingested log data.

2) The second part provides a SMS alerting functionality via Splunk's scripted alert triggers.

What's in the box?
-------------

*1 x New Index (index=twilio)
*2 x Python collection scripts (get_call_logs.py, get_sms_logs.py)
*2 x File monitor inputs (call_log.csv, sms_log.csv)
*4 x Prebuilt Dashboards (call center, call stats, sms center, billing)
*3 x Prebuilt Alert (billing)
*1 x Important Setup Instructions (you are here)

Twilio Log Input Setup
-------------

**0) Overview**

There are 4 steps you will need to get this app working.

*Get your Twilio account keys
*Edit log collection scripts
*Configure input
*Profit

**1) Get your Twilio account keys**

Get your Twilio Account SID and Auth Token on your [**Twilio Dashboard**](https://www.twilio.com)

**2)Edit log collection scripts**

This app contains two scripts (get_call_logs.py & get_sms_logs.py) that get call and SMS data from Twilio and place the returned information into two CSV files (call_log.csv and sms_log.csv).

You need to configure these scripts with your Twilio account keys:

*Go to "$SPLUNK_HOME/etc/apps/twilio-app/bin"
*Using your favourite text editor open "get_call_logs.py" and "get_sms_logs.py"
*Enter your Twilio Account SID (starting with AC) / Auth token

**Protip:** You might want to test that both scripts work by running them.

$ python get_call_logs.py

$ python get_sms_logs.py

If everything has worked correctly you should see "call_log.csv" and "sms_log.csv" created in "$SPLUNK_HOME/etc/apps/twilio-app/bin"

**3) Configure input**

*Go to "$SPLUNK_HOME/etc/apps/twilio-app/default"
*Copy "inputs.conf" to "$SPLUNK_HOME/etc/apps/twilio-app/local"
*Using your favourite text editor open "$SPLUNK_HOME/etc/apps/twilio-app/local/inputs.conf"
*Replace "$SPLUNK_HOME" with the correct directory of your Splunk installation
*Restart Splunk
*Enable the scripted inputs in the Splunk GUI via: "Settings" > "Data Inputs" > "Scripts"

__Note: The CSV monitors (where log data is written to) are already enabled by default. The scripted inputs do not store any data, they are only used to call the Twilio API.__

**4) Profit**

If everything has worked well, a simple search for "index=twilio" should return some results. You might need to restart Splunk first.

Should some of the dashboards be empty, run a search in Splunk to see if the fields used are in your logs. If you're still suspicious, check the CSV files that should be created exist and have been populated with data.

Splunk SMS Alert Setup
-------------

**0) Overview**

There are 4 steps you will need to get this app working.

*Get your Twilio account keys
*Edit alert scripts
*Configure an alert
*Profit

**1) Get your Twilio account keys**

Get your Twilio Account SID and Auth Token on your [**Twilio Dashboard**](https://www.twilio.com)

**2)Edit alert scripts**

*Go to "$SPLUNK_HOME/etc/apps/twilio-app/bin"
*Using your favourite text editor open "$SPLUNK_HOME/etc/apps/twilio-app/bin/textalert-twilio.py"
*Enter your Twilio Account SID (starting with AC) / Auth token
*Enter "TO phone number" (recipient of SMS Text Message)
*Enter "FROM phone number" (sender of message, must be one of your Twilio Account phone #)

**3) Configure an alert**

*Configure a Splunk alert and select the "Run a Script" option
*Set "textalert-twilio.py" as the script

__Note: Twilio will charge you for every SMS message sent. You can view Twilio pricing @ https://www.twilio.com/sms/pricing__

**4) Profit**

If everything has worked well the "TO phone number" should be recieving alerts. If not, check the alerts are being fired in the alert manager in the Splunk GUI via: "Activity" > "Alert Manager"

[END]

Enjoy!

[**@himynamesdave**](https://twitter.com/himynamesdave)
