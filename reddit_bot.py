# Reddit API practice

#author: Dylan Thiemann
#email: dylanthiemann@gmail.com

#date: 3/20/15

import praw, os

user_agent = "myBotDT v0.1"

def main():

    # Get access to Reddit
    # try to keep user_agent as unique as possible
    reddit = praw.Reddit(user_agent=user_agent)

    # Get the user
    user_name = "bassistdt"
    user = reddit.get_redditor(user_name)

    comments = user.get_submitted()
    karma_by_subreddit = {}
    for item in comments:
        subreddit = item.subreddit.display_name
        karma_by_subreddit[subreddit] = karma_by_subreddit.get(subreddit,0) + item.score

    for i in karma_by_subreddit.keys():
        print(i, karma_by_subreddit[i])
    
    return 0

def getKarmaBreakdown(userAgent, userName):

    # Get access to Reddit
    # try to keep user_agent as unique as possible
    reddit = praw.Reddit(user_agent=userAgent)

    # Get the user
    user = reddit.get_redditor(userName)

    comments = user.get_submitted()
    karma_by_subreddit = {}
    for item in comments:
        subreddit = item.subreddit.display_name
        karma_by_subreddit[subreddit] = karma_by_subreddit.get(subreddit,0) + item.score

    return karma_by_subreddit

def getSubredditHotPosts(user_angent, subreddit, limit):
    reddit = praw.Reddit(user_agent=user_agent)
    subReddit = reddit.get_subreddit(subreddit)

    for submission in subReddit.get_hot(limit = limit):
        print("Title: " + submission.title)
        print("Score: " + str(submission.score))

    print("done")

def commentingAndPosting(user_agent):
    username = input("Enter Reddit user name: ")
    pw = input("Enter Reddit password: ")

    # Login to Reddit
    r = praw.Reddit(user_agent=user_agent)
    r.login(username, pw)

    posts_replied_to = []

    # Check to see if we have a list of posts replied to
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = filter(None, posts_replied_to)

    # Use a testing subreddit designed for this - 'pythonforengineers'
    subR = r.get_subreddit('pythonforengineers')
    for submission in subR.get_hot(limit=5):

        submission.add_comment("This is a test :-)")
        print("bot replied to: ", submission.title)

        posts_replied_to.append(submission.id)

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

commentingAndPosting(user_agent)

