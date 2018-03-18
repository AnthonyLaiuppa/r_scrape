from __future__ import absolute_import, unicode_literals
from slackclient import SlackClient
import praw
import json 

class rScrapeLogic(object):

	def __init__(self, mode=None):
		self.mode=mode

	def load_config(self, data):
		self.config = json.load(open(data))
		self.config['details']['keywords'] = [x.strip() for x in self.config['details']['keywords'].split(',')]
		return self.config

	def auth_reddit(self):
		try:
			self.reddit = praw.Reddit(
				client_id = self.config['reddit']['id'],
				client_secret = self.config['reddit']['secret'],
				user_agent = self.config['reddit']['user_agent'],
				username = self.config['reddit']['username']
			)
			return self.reddit
		except Exception as exc:
			print('{0} - Unable to auth to reddit, check your creds'.format(exc))	
			exit(0)

	def slack_it(self, message):	
		slack_client = SlackClient(self.config['slack']['token'])
		try:
			slack_client.rtm_connect()
			slack_client.api_call(
				"chat.postMessage", 
				channel=self.config['slack']['channel'], 
				text=message, 
				as_user=True)
		except Exception as exc:
			print('{0} - Unable to use slack, please check configs'.format(exc))

	def mon_subReddit(self):
		for submission in self.reddit.subreddit(self.config['details']['subreddit']).stream.submissions():
			try:
				self.check_submission(submission)
			except Exception as exc: 
				print('{0} - We are out of submissions waiting on more'.format(exc))

	def check_submission(self, submittal):
		for word in self.config['details']['keywords']:
			if word in submittal.selftext_html:
				message = '@channel We have a match - {0} - {1}'.format(word, submittal.url)
				self.slack_it(message)
