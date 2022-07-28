from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import prometheus_client

import os
import metrics


if "CRONTAB_SCHEDULE" not in os.environ:
    print("Please provide a CRONTAB_SCHEDULE. Aborting.")
    exit(1)

CRONTAB_SCHEDULE = os.environ["CRONTAB_SCHEDULE"]

if __name__ == "__main__":
    print("Getting metrics once initially...")
    print(metrics)
    metrics.get_latest_user_metrics()

    print("Starting server at port:", 8080)
    prometheus_client.start_http_server(8080)

    print("Scheduling to update metrics according to crontab schedule:",
          CRONTAB_SCHEDULE)
    scheduler = BlockingScheduler()
    cron_triggerer = CronTrigger.from_crontab(CRONTAB_SCHEDULE)
    scheduler.add_job(metrics.get_latest_user_metrics, cron_triggerer)
    try:
        # TODO. docker seems to freeze, when this line is here.
        scheduler.start()
        # this is weird, because docker hangs even before this line is reached!
    except (KeyboardInterrupt, SystemExit):
        pass
