import praw
import psycopg2

query = "INSERT INTO SUBMISSION VALUES (%s,%s,%s,%s);"
conn = psycopg2.connect(database="template1", user = "postgres", password = "xxxxxx", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
reddit = praw.Reddit(client_id='xxxxxxxx',
                     client_secret='xxxxxxxxxxx',
                     user_agent='eltox')

id=0
subreddit=reddit.subreddit('worldnews')
for submission in subreddit.stream.submissions():
	try:
		data=(id,submission.ups,submission.downs,submission.title)
		cur.execute(query,data)
		conn.commit()
		id=id+1
	except Exception as e:
		print(str(e))