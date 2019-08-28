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


reddit = praw.Reddit('nolan-joker-bot')

subreddit = reddit.subreddit("nolanbatmanmemes")

for comment in subreddit.stream.comments():
	if re.search("joker", comment.body, re.IGNORECASE):
		print ("Target comment: ", comment.body)
		joker_reply = "**" + random.choice(joker_quotes) + "**"
		comment.reply(joker_reply)
		print ("Joker reply: ", joker_reply)
		print ("-----------------\n")
