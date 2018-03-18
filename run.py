from __future__ import absolute_import, unicode_literals
from  r_scrape import rScrapeLogic

def main():
	
	driver = rScrapeLogic()
	driver.load_config('config.json')
	driver.auth_reddit()
	driver.mon_subReddit()

if __name__== '__main__':
	main()
