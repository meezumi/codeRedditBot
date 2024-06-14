# print("hello world")
from dotenv import load_dotenv
import praw

load_dotenv()
import os

username = "testing_me"
password = os.getenv("PASSWORD")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# this is to make that call for connection to the reddit
reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="testing_bot"
)
# to fetch the username/account to from which the api call is being made
# print(reddit_instance.user.me())

# to get submissions from a subreddit, we need a subreddit
subreddit = reddit_instance.subreddit("cats")
print(subreddit)

# to get the top 25 top posts in the subreddit, from the current week
top_25_subs = subreddit.top(limit=25, time_filter="week")

# similarly:
hot_25_subs = subreddit.top(limit=25)
new_25_subs = subreddit.new(limit=25)

for subs in top_25_subs:
    print(subs.title)
# this is how to extract post from subreddits

# next how to create a post on a subreddit:
test_subreddit = reddit_instance.subreddit("testingground4bots")
print(test_subreddit)
test_subreddit.submit(title="this is my test post from a new bot", selftext="howdy, how ya doing?")

# next to fetch/get comments from a post in a subreddit:

# this is the submission id can be fetched from a submission in a subreddit
get_coms_subreddit = reddit_instance.submission("dloggg")
# the id can be found from the url,
# for reference/example: https://www.reddit.com/r/catsareliquid/comments/dloggg/meta_stop_posting_normal_pics_of_cats/
print(get_coms_subreddit.title)
# total comments: 180 here

comments = get_coms_subreddit.comments
print(len(get_coms_subreddit.comments))
# this returns a comment forest object, not the actual comments, and are done in paging system, meaning only the
# comments visible in that page will be visible, not all of them, hence we get 78 for the time being.
# to get more comments, we can use replace_more() function, untill we hi the max comments

for comment in comments:
    if "cat" in comment.body:
        print(comment.body)
        # comment.reply("your comment contains cat")
        # this will reply all the comments that have word cat in it 🗿
