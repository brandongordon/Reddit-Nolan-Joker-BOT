#!/usr/bin/python3

import praw
import re
import random

#Library of quotes
joker_quotes = \
[
"",
"",
]

reddit = praw.Reddit('nolan-joker-bot')

subreddit = reddit.subreddit("nolanbatmanmemes")

for comment in subreddit.stream.comments():
	print (comment.body)
	if re.search("joker", comment.body, re.IGNORECASE):
		joker_reply = "**" + random.choice(joker_quotes) + "**"
		comment.reply(joker_reply)
		print (joker_reply)
