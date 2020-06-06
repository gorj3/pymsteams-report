#!/usr/bin/python3
import requests
import sys
sys.path.insert(0, '<>') #change for config path
from sendTeams import sendTeams
from check_service import check_service
from datetime import datetime
import config #imports variables from config.py file

#disables ssl warnings and set the time for the reports
requests.packages.urllib3.disable_warnings() 
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def main():
    for x in config.services:
        check_service(x, config.services.get(x))

    if config.errors == 0:
        sendTeams(config.reportHook, dt_string, config.upServices)

if __name__ == "__main__":
    main()