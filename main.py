import praw
import psycopg2

query = "INSERT INTO SUBMISSION VALUES (%s,%s,%s,%s);"
conn = psycopg2.connect(database="template1", user = "postgres", password = "XXXXXX", host = "127.0.0.1", port = "5432")
cur = conn.cursor()


reddit = praw.Reddit(client_id='XXXXXX',
                     client_secret='XXXXXX',
                     user_agent='eltox')
id=0
subreddit = reddit.subreddit('worldnews')
hot_python = subreddit.hot(limit=None)
for submission in hot_python:
	if not submission.stickied:
		print(submission.title)
		try:
			data=(id,submission.ups,submission.downs,submission.title)
			cur.execute(query,data)
			conn.commit()
			id=id+1
		except Exception as e:
			print(str(e))
conn.close()
