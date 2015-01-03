# Reddit API practice

#author: Dylan Thiemann
#email: dylanthiemann@gmail.com

#date: 1/1/14

import praw

def main():

    # Get access to Reddit
    # try to keep user_agent as unique as possible
    user_agent = "just having some fun /u/bassistdt"
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

main()
