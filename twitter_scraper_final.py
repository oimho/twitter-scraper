import twitter
import json
import sys
import csv

csvfile = open('codingassignment.csv', 'a')
csvwriter = csv.writer(csvfile) 

consumer_key="cVD7fIgtDSXunWsLzopoSbZSr"
consumer_secret="KtER5JRDRKyAhyYVtDmXKCV69oBR4NJ0MjPlerWn8F4IrUkDgK"
 
 
access_token="2788965003-nxwzrMHRZoNL8e0rIjbsO4FVA68J9CmOr5Psv99"
access_token_secret="VtA03ukFNUS0qMc1LfnxkXdDwksEoEJRlj1DUkQn8yD6J"
 
auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)

q = 'CharlieHebdo'
print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:


	print json.dumps(tweet, indent=1)
	print tweet['text']
	print tweet['user']['screen_name']
	screen_name = tweet['user']['screen_name'].encode('utf-8')
	created_at = tweet['created_at']
	text = tweet['text'].encode('utf-8')

	csvwriter.writerow([screen_name, created_at, text])