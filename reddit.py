import os
import platform

import praw

from logger import logger

DEVELOPER_REDDIT_USERNAME = "_swnt_"

APP_NAME = "reddit-user-metrics-exporter"
VERSION = "0.1"
PLATFORM = platform.system()
USER_AGENT = f"{PLATFORM}:{APP_NAME}:{VERSION} (by /u/{DEVELOPER_REDDIT_USERNAME})"

if "USER" not in os.environ:
    logger.error("Please provide a username via USER. Aborting.")
    exit(1)

if "CLIENT_ID" not in os.environ or "CLIENT_SECRET" not in os.environ:
    logger.error(
        "Please provide a client id and client secret. At least one was not provided. Aborting.")
    exit(1)

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
USER = os.environ['USER']


def get_user_from_reddit():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    ).redditor(USER)
