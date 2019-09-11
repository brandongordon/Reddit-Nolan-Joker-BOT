#!/usr/bin/python3

import praw
import re
import random
import os

quotes_file = "quotes.txt"
listening_subreddit = "nolanbatmanmemes"
listening_term = "joker"

def let_joker_talk(comment, quote):
	print ("Target comment: ", comment.body)
	comment.reply(quote)
	print ("\t|\n\tv\nJoker reply: ", quote)
	print ("-----------------\n")
	
#----------------------------------------------------------------------------------------#


#Read the quote file into a list and remove any empty values
with open(quotes_file, "r", encoding="utf-8") as f:
	joker_quotes = f.read()
	joker_quotes = joker_quotes.split("\n")
	joker_quotes = list(filter(None, joker_quotes))
	
	
#Have we run this code before? If not, create an empty list of posts replied to
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
	
#If we have run the code before, load the list of posts we have replied to
else:
	#Read the file into a list and remove any empty values
	with open("posts_replied_to.txt", "r", encoding="utf-8") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))



#Create the Reddit instance
reddit = praw.Reddit('nolan-joker-bot')

#Select subreddit we are listening to
subreddit = reddit.subreddit(listening_subreddit)


for comment in subreddit.stream.comments():    #For each comment in the subreddit (as they appear)
	if re.search(listening_term, comment.body, re.IGNORECASE) and comment.id not in posts_replied_to:
		#Reply to the comment with a random quote from a list of quotes
		reply = random.choice(joker_quotes)
		let_joker_talk(comment, reply)
				
		#store the current ID into our list
		posts_replied_to.append(comment.id)
			
		#write our updated list back to the file
		with open("posts_replied_to.txt", "w") as f:
			for comment_id in posts_replied_to:
				f.write(comment_id + "\n")
		
