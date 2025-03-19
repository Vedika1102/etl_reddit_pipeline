import praw

reddit = praw.Reddit(
    client_id="WPQI71le5b2GNpKlwJR38w",
    client_secret="rR1pcuwxmBQB-POIwX7CLT7EBjnEug",
    user_agent="MyRedditETL",
    username="VedikaScript",  # <-- Add your Reddit username here
    password="#Vedikasaee11",  # <-- Add your Reddit password here
    check_for_async=False  # Prevent async issues in Jupyter/IDE
)

try:
    user = reddit.user.me()
    if user:
        print(f"✅ Authenticated as: {user}")
    else:
        print("❌ Authentication failed. Check credentials or permissions.")
except Exception as e:
    print(f"❌ Failed to authenticate: {e}")

subreddit = reddit.subreddit("dataengineering")
for post in subreddit.hot(limit=5):
    print(f"{post.title} - {post.score} upvotes")
