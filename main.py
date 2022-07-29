from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import prometheus_client

import os
import metrics

# I would like to not use a logging library and simply log to stdout, but
# the output seems to be completely dropped - even before the scheduler.start() statement is reached!
# Weird interaction. It very much seemed like a bug, but maybe it was misconfiguration.
from logger import logger

if "CRONTAB_SCHEDULE" not in os.environ:
    logger.error("Please provide a CRONTAB_SCHEDULE. Aborting.")
    exit(1)

CRONTAB_SCHEDULE = os.environ["CRONTAB_SCHEDULE"]

if __name__ == "__main__":
    logger.info("Getting metrics once initially...")
    metrics.get_latest_user_metrics()

    logger.info(f"Starting server at port: {8080}")
    prometheus_client.start_http_server(8080)

    logger.info(
        f"Scheduling to update metrics according to crontab schedule: {CRONTAB_SCHEDULE}")
    scheduler = BlockingScheduler()
    cron_triggerer = CronTrigger.from_crontab(CRONTAB_SCHEDULE)
    scheduler.add_job(metrics.get_latest_user_metrics, cron_triggerer)

    scheduler.start()
