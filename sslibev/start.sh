#!/bin/bash
python3 gen.py $@
docker-compose down
docker-compose up -d
docker-compose ps
