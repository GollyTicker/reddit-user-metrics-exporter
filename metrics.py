import datetime
from prometheus_client import Gauge
import reddit

reddit_user_link_karma = Gauge(
    "reddit_user_link_karma",
    "Number of link karma points",
    ["user"],
)

reddit_user_comment_karma = Gauge(
    "reddit_user_comment_karma",
    "Number of comment karma points",
    ["user"],
)


def get_latest_user_metrics():
    try:
        user = reddit.get_user_from_reddit()

        name = user.name
        link_karma = user.link_karma
        comment_karma = user.comment_karma

        reddit_user_link_karma.labels(name).set(link_karma)
        reddit_user_comment_karma.labels(name).set(comment_karma)

        print(
            f"{datetime.datetime.now()} Retrieved: /u/{name}, {link_karma} link-karma, {comment_karma} comment-karma")

    except Exception as e:
        print(f"{datetime.datetime.now()} ERROR: {e}")
