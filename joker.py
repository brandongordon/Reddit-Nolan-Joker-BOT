#!/usr/bin/python3

import praw
import re
import random
import os

#Read the quote file into a list and remove any empty values
with open("quotes.txt", "r") as f:
	joker_quotes = f.read()
	joker_quotes = joker_quotes.split("\n")
	joker_quotes = list(filter(None, joker_quotes))
	
	
#Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
	
#If we have run the code before, load the list of posts we have replied to
else:
	#Read the file into a list and remove any empty values
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))



#Create the Reddit instance
reddit = praw.Reddit('nolan-joker-bot')

subreddit = reddit.subreddit("nolanbatmanmemes")

for comment in subreddit.stream.comments():
	if re.search("joker", comment.body, re.IGNORECASE) and comment.id not in posts_replied_to:
		print ("Target comment: ", comment.body)
		joker_reply = random.choice(joker_quotes)
		comment.reply(joker_reply)
		print ("Joker reply: ", joker_reply)
		print ("-----------------\n")
		
		#store the current ID into our list
		posts_replied_to.append(comment.id)
			
		#write our updated list back to the file
		with open("posts_replied_to.txt", "w") as f:
			for comment_id in posts_replied_to:
				f.write(comment_id + "\n")
		
