# add Microsoft Teams Incoming Webhook first

import pymsteams



# you must create the connectorcard object with the Microsoft Webhook URL

myTeamsMessage = pymsteams.connectorcard("")



myTeamsMessage.title("This is my message title")

myTeamsMessage.text("this is my text")

myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")



# preview your object

# myTeamsMessage.printme()



# send the message

myTeamsMessage.send()
