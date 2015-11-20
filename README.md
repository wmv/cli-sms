#Installation instructions:

(Requires a valid Nexmo account with credit/trial)
- Download zip & extract
- From within the downloaded folder, run ```pip install --editable .``` (don't forget the period at the end.)
- Make sure the environment variables for ```NEXMO_API_KEY``` and ```NEXMO_API_SECRET``` have been set.

The values for those are available in your Nexmo dashboard. To set, run:

 ```echo export NEXMO_API_KEY=YourNexmoApiKeyHere >> ~/.bash_profile``` (replace YourNexmoApiKeyHere with actual value)

 and 

 ```echo export NEXMO_API_KEY=YourNexmoApiSecretHere >> ~/.bash_profile``` (replace YourNexmoApiSecretHere with actual value)

- Optionally, to set a default recipient number (for when you choose to ommit the --number parameter; please note this is not required), run this:

 ```echo export SMS_MESSAGE_DEFAULT_RECIPIENT=YourCellNumberOfChoice >> ~/.bash_profile``` (replace YourCellNumberOfChoice with actual value)


The instructions above assume you are using bash, but feel free to replace bash_profile with the equivalent for your shell of choice.

#Usage: ```sms``` [OPTIONS]

#Options:
 - ```--number``` TEXT  This is the phone number that the SMS will be sent to.
 - ```--text``` TEXT    This is the text that will form the body of the SMS.
 - ```--verbose```      Set this option to see extra details.
 - ```-v```             Set this option to see extra details.
 - ```--help```         Show help information and exit.
