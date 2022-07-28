# Reddit User Metrics Exporter

Extract basic user metrics for a user and collect them in a OpenMetrics format (also consumable by Prometheus)


# Setup

Populate a local `.env` file with your reddit app's client id, client secret, the 
user you want to collect the metrics of and the [crontab schedule](https://crontab.guru/#0_*_*_*_*) for how often to request the value:
```bash
CLIENT_ID="<your client id>"
CLIENT_SECRET="<your client secret>"
USER="<your-user-name. for instance ExampleUser for u/ExampleUser>"
CRONTAB_SCHEUDLE="<schedule of how often to retreve the metrics from reddit. recommended to do this hourly via 0 * * * *>"
```
You can find the credentials for your app [here on reddit](https://www.reddit.com/prefs/apps). you may need to create a new developer-app to access your data first.

# Run

```bash
./restart-service.sh
```
and stop with 

```bash
./stop-service.sh
```

# Developer Info

* [Documentation of Reddit Python API (PRAW) for a redditor](https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html)
