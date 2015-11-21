from setuptools import setup

setup(
	name='sms',
	version='1.0',
	py_modules=['sms'],
	install_requires=[
		'Click',
		'libpynexmo'
	],
	entry_points='''
		[console_scripts]
		sms=sms:send
	''',
)
