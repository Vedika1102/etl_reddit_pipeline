from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import connect_reddit, extract_posts

def reddit_pipeline(file_name: str, subreddit: str, time_limit: str, limit: int = None):
    # Connect to Reddit API
    instance = connect_reddit(CLIENT_ID, SECRET, 'MyRedditETL')

    # Extraction process
    posts = extract_posts(instance, subreddit, time_limit, limit)  # ✅ Correct parameter name
