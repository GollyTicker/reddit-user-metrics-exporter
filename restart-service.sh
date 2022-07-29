#!/bin/bash
set -e
./stop-service.sh || true
docker-compose build --pull
docker-compose up -d
