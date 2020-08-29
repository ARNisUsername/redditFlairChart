import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='zvcDckQJ3VJmLw',
                     client_secret='yUtcmzs7X9IYls7Ru6hBtCFsI8g',
                     password='GR101_ARN',
                     user_agent='script with checkBasedBot',
                     username='checkBasedBot',
                     )


subreddit = reddit.subreddit('PoliticalCompassMemes')
storedDict = {}

for submission in subreddit.top(limit=1000):
    flairText = submission.author_flair_text

    if flairText != None:
        flairTemp = flairText.split(' - ')
        authorFlair = flairTemp[1]
        if '2' in flairTemp[0]:
            authorFlair = 'Purple Lib'
        if authorFlair not in storedDict.keys():
            storedDict[authorFlair] = 1
        else:
            storedDict[authorFlair] += 1



labels = list(storedDict.keys())
sizes = list(storedDict.values())
colors = ['royalblue', 'gray', 'green', 'yellow', 'orange', 'lime', 'lightsteelblue', 'red', 'mediumorchid', 'lightsalmon']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
