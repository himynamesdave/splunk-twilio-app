Twilio App for Splunk
====

Thankyou for downloading the Twilio App v0.01.

A Twilio App for Splunk. Includes detailed views of call and SMS logs. Also includes SMS alert functionality.

NOTE: This app does NOTHING by default! Please follow setup instructions below.

Requirements
--

- Splunk installed. Download for free @ http://www.splunk.com/download?r=header
- A Twilio account. Get an account and phone number for free @ https://www.twilio.com

Installing the App
--

- 1. Copy: "/twilio-app" to "$SPLUNK_HOME/etc/apps"
- 2. Restart Splunk
- 3. Congratulations! The Twilio app is now installed.

Data Import
--

This app contains two scripts (get_call_logs.py & get_sms_logs.py) that get call and SMS data from Twilio and place the returned information into two CSV files (call_log.csv and sms_log.csv).

Twilio Call and SMS logs in CSV format downloaded directly imported from Twilio (https://www.twilio.com/help/faq/twilio-basics/how-do-i-export-my-smscall-logs) are also supported.

SETUP:

Note: Your Twilio Account SID and Auth Token can be found under "Dashboard" @ https://www.twilio.com

*nix Users

- 1. Go to "$SPLUNK_HOME/etc/apps/twilio-app/bin".
- 2. Using your favourite text editor open "get_call_logs.py" and "get_sms_logs.py"
- 3a. Replace “YOUR_ACCOUNT_SID” with your Twilio Account SID (starting with AC)
- 3b. Replace “YOUR_AUTH_TOKEN” with your Twilio Auth Token
- 4. Run both scripts to test they work. You should see "call_log.csv" and "sms_log.csv" created in "$SPLUNK_HOME/etc/apps/twilio-app/bin"
- 5. Go to "$SPLUNK_HOME/etc/apps/twilio-app/default".
- 6. Move "inputs.conf" to "$SPLUNK_HOME/etc/apps/twilio-app/local"
- 7. Using your favourite text editor open "$SPLUNK_HOME/etc/apps/twilio-app/local/inputs.conf"
- 8. Replace "<$SPLUNK_HOME>" with the correct directory of your Splunk installation. Stanzas beginning with [script:///... run hourly calls to Twilio to collect new data. Stanzas beginning with [monitor:///... watch for any newly generated logs from the scripts.

Note: Windows users will need to change the inputs.conf stanzas to the following: "[monitor://" and "script://"

Installing SMS Alerts
--

Note: Your Twilio Account SID and Auth Token can be found under "Dashboard" @ https://www.twilio.com

SETUP:

- 1. Copy "$SPLUNK_HOME/etc/apps/twilio-app/bin/textalert-twilio.py" to "$SPLUNK_HOME/bin/scripts"
- 2. Edit "$SPLUNK_HOME/bin/scripts/textalert-twilio.py" with your favourite text editor and input:
- 2a. Your Twilio Account SID (starting with AC)
- 2b. Your Twilio Auth Token
- 2c. TO phone number (recipient of SMS Text Message)
- 2d. FROM phone number (sender of message, must be one of your Twilio Account phone nos.)
- 3. In Splunk set up an alert and use textalert-twilio.py as the "Run a Script" option
- 4. Congratulations! You have set up an SMS alert

Please note: Twilio will charge you for every SMS message sent. You can view Twilio pricing @ https://www.twilio.com/sms/pricing

Change log
---

v1 - Added support for automatic log import
v0.1 - Beta Release

To Do
---

- Phone Number ID Lookup (Phone Book)
- Phone Number Extension Lookup (Country)

Future Features?
---

Please submit feedback on apps.splunk.com!

- Automated set-up?
- UI management of alerts?

If you would like to contribute to the developement of this app I'll also happily accept any pull requests @ https://github.com/splunkstart/twilio-app