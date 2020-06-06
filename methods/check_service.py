from datetime import datetime
import requests
from sendTeams import sendTeams
from sendDownCode import sendDownCode
from sendError import sendError
import sys
sys.path.insert(0, '<>')#change for config path
import config #imports variables from config.py file

#creates data and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def check_service(service, url):
    serviceName = service
    global errors
    try:
        url = requests.get(url, verify=False)
        status = url.status_code
        if status == 200:
            print("{} is up. Code: {}".format(service, status))
            config.upServices.append(service)
        else:
            print("ALERT! {} IS DOWN. CODE: {}".format(service, status))
            config.errors += 1
            sendDownCode(config.errorHook, service, dt_string, status)
    except Exception as error:
        config.errors += 1
        sendError(config.errorHook, service, dt_string, error)