import praw
import matplotlib.pyplot as plt

#Create reddit bot, needed for anaylzing top posts. I used one of my old bots for this
reddit = praw.Reddit(client_id='zvcDckQJ3VJmLw',
                     client_secret='yUtcmzs7X9IYls7Ru6hBtCFsI8g',
                     password='GR101_ARN',
                     user_agent='script with checkBasedBot',
                     username='checkBasedBot',
                     )


subreddit = reddit.subreddit('PoliticalCompassMemes')
storedDict = {}

for submission in subreddit.top(limit=1000):
    #For the top 1000 posts, get the flair of the poster
    flairText = submission.author_flair_text

    if flairText != None:
        #If the poster has a flair, store it in a dictionary with the number of times flair has been used
        flairTemp = flairText.split(' - ')
        authorFlair = flairTemp[1]
        if '2' in flairTemp[0]:
            authorFlair = 'Purple Lib'
        if authorFlair not in storedDict.keys():
            storedDict[authorFlair] = 1
        else:
            storedDict[authorFlair] += 1


#Use the dictionary to get the labels and sizes needed for displaying the matplotlib chart
labels = list(storedDict.keys())
sizes = list(storedDict.values())
colors = ['royalblue', 'gray', 'green', 'yellow', 'orange', 'lime', 'lightsteelblue', 'red', 'mediumorchid', 'lightsalmon']

#Create the pie chart with matplotlib
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
