import pymsteams
import sys
sys.path.insert(0, '<>')#change for config path
import config #imports variables from config.py file

def sendError(errorHook, service, date, error):
    #channel URL
    teamsURL = config.errorHook
    myTeamsMessage = pymsteams.connectorcard(teamsURL)
    myTeamsMessage.title("TEST REPORT ERROR FOR " + str(service))
    myTeamsMessage.text("Test run at " + str(date))
    #section with the up services
    myMessageSection = pymsteams.cardsection()
    myMessageSection.activityTitle(service)
    myMessageSection.activityText(str(error))
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()