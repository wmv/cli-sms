__author__ = 'Wilson Canda (wilsonmaravilha@gmail.com)'

import os
import getpass
import click
from nexmomessage import NexmoMessage

class SMS(object):

	CREDENTIALS = {
		'nexmo': {
		'api_key': os.environ['NEXMO_API_KEY'],
		'api_secret': os.environ['NEXMO_API_SECRET']
		}
	}

	#  DEFAULTS {} holds the default values.
	DEFAULTS = {
		'text': 'Hello from {} :)'.format(getpass.getuser()),
	}

	@staticmethod
	def fire(recipient, text):

		return NexmoMessage(
			{
				'reqtype': 'json',
				'api_key': SMS.CREDENTIALS['nexmo']['api_key'],
				'api_secret': SMS.CREDENTIALS['nexmo']['api_secret'],
				'from': getpass.getuser(),
				'to': recipient,
				'text': text
			}
		).send_request()


@click.command()
@click.option('--number', 
	help='This is the phone number that the SMS will be sent to.\n' +
		 'Required if SMS_MESSAGE_DEFAULT_RECIPIENT environment variable has not been set.'
	)
@click.option('--text', 
	default=SMS.DEFAULTS['text'], 
	help='This is the text that will form the body of the SMS.'
	)
@click.option('--verbose', 
	default=False, 
	is_flag=True, 
	help='Set this option to see extra details.'
	)
@click.option('-v', 
	default=False, 
	is_flag=True,
	help='Set this option to see extra details.'
	)
def send(number, text, verbose, v):
	""" This script sends an SMS given the recipient's number and text. """
	if not number:
		try:
			#  Attempt to get the default number from user's env.
			number = os.environ['SMS_MESSAGE_DEFAULT_RECIPIENT']
		except KeyError:
			raise click.BadParameter('SMS not sent due to unspecified recipient. Re-run with --help for help.')
	result = SMS.fire(number, text)

	try:
		for message in result['messages']:
			assert message['status'] == '0'
		click.echo('SMS to {} delivered.'.format(number))
		if verbose or v:
			click.echo('\nText: {}'.format(text))
	except AssertionError:
		click.echo('SMS sending failed due to unspecified error.')
		if verbose or v:
			click.echo('\nDebug info: \n' + result)
	except Exception as e:
		click.echo('SMS sending failed due to the following error: {}.')
		if verbose or v:
			click.echo('\nDebug info: \n' + str(e) + result)
