#-*- coding: latin1 -*-
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json, sys, os
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key = "YOUR KEY"
consumer_secret = "YOUR KEY"
access_token = "YOUR KEY"
access_token_secret = "YOUR KEY"
#

t = datetime.now().strftime("%Y%m%d%H%M%S")

class StdOutListener(StreamListener):
	#A listener handles tweets that are received from the stream.
	#This is a basic listener that just prints received tweets to stdout
	batch_size = 50000
	batch = batch_size
	cont = 0
	
	def on_data(self, data):
		#print(data)
		self.__class__.cont += 1
		print(self.__class__.cont)
		if self.__class__.batch == 0:
			self.__class__.batch = self.__class__.batch_size  
		
		name = os.path.basename(__file__)
		name = name.split(".py")
		name = name[0]
		file = open("/home/twitterurt/ProjetoEleicao/data/"+str(name)+"/"+str(t)+'.json','a')
		json.dump(data, file)
		file.close()
		self.__class__.batch -= 1
		return True
	
	def on_error(self, status):
		print('ERRO\n' + status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(follow=['870030409890910210'], track=['meirelles'])
