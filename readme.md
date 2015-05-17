#Twilio App for Splunk

Twilio App for Splunk helps you ingest Twilio logs into Splunk. This app comes prebuilt with searches powering a number of dashboards and alerts for the ingested log data. It also provides Twilio SMS alerting functionality via Splunk's scripted alert triggers.

##What's included

*1 x Index (twilio)
*4 x Prebuilt Dashboards (call center, call stats, sms center, billing)
*1 x Prebuilt Alert (billing)

##Installation

Download this app from Splunkbase then upload the tar.gz file to Splunk.

##Log Input Config

**1) Download your Twilio call and SMS logs**

Twilio provides an easy way to access your call and SMS logs using the web interface.

[Download your Twilio call logs here](https://www.twilio.com/user/account/log/calls).

[Download your Twilio SMS logs here](https://www.twilio.com/user/account/log/messages).

**Protip:** Place both files in a folder together.

**2) Upload these files to Splunk**

Navigate to: Settings > Data inputs > Files & directories

Click add new.

Follow the steps, making sure you set **sourcetype=csv**, and **index=twilio**.

You can choose wether to monitor a file or a directory. **Protip:** If you placed both files in the same directory during step one, it is quicker to provide Splunk with the directory to monitor. This way, if new Twilio logs are added in the future, Splunk will automatically ingest them.

**3) Profit**

If everything has worked well, a simple search for "index=twilio" should return some results. You might need to restart Splunk first.

##Splunk SMS Alert Setup

**0) Overview**

**1) Get your Twilio account keys**

Get your Twilio Account SID and Auth Token on your [Twilio Dashboard](https://www.twilio.com)

**2) Edit alert scripts**

*Go to "$SPLUNK_HOME/etc/apps/twilio-app/bin"
*Using your favourite text editor open "$SPLUNK_HOME/etc/apps/twilio-app/bin/textalert-twilio.py"
*Enter your Twilio Account SID (starting with AC) / Auth token
*Enter "TO phone number" (recipient of SMS Text Message)
*Enter "FROM phone number" (sender of message, must be one of your Twilio Account phone #)

**3) Configure an alert**

*Configure a Splunk alert and select the "Run a Script" option.
*Set "textalert-twilio.py" as the script

__Note: Twilio will charge you for every SMS message sent. You can view Twilio pricing @ https://www.twilio.com/sms/pricing__

**4) Profit**

If everything has worked well the "TO phone number" should be recieving alerts. If not, check the alerts are being fired in the alert manager in the Splunk GUI via: "Activity" > "Alert Manager"

##Upcoming features

*Automated (real-time) collection of logs into Splunk via Twilio API.

##More

[Github repo](https://github.com/himynamesdave/splunk-twilio-app)