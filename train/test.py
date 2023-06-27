<<<<<<< HEAD
# add Microsoft Teams Incoming Webhook first

import pymsteams



# you must create the connectorcard object with the Microsoft Webhook URL

myTeamsMessage = pymsteams.connectorcard("https://tejcomtw.webhook.office.com/webhookb2/9d4d4036-fa12-4c6a-bd26-5da955301e40@c3654575-c406-43b3-9dfa-d367e3435661/IncomingWebhook/e5c7235fc3864e5a971fff30a1d51069/e7a99f51-fa98-4f71-bd56-be6932556da9")



myTeamsMessage.title("This is my message title")

myTeamsMessage.text("this is my text")

myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")



# preview your object

# myTeamsMessage.printme()



# send the message

myTeamsMessage.send()
=======
# add Microsoft Teams Incoming Webhook first

import pymsteams



# you must create the connectorcard object with the Microsoft Webhook URL

myTeamsMessage = pymsteams.connectorcard("https://tejcomtw.webhook.office.com/webhookb2/9d4d4036-fa12-4c6a-bd26-5da955301e40@c3654575-c406-43b3-9dfa-d367e3435661/IncomingWebhook/e5c7235fc3864e5a971fff30a1d51069/e7a99f51-fa98-4f71-bd56-be6932556da9")



myTeamsMessage.title("This is my message title")

myTeamsMessage.text("this is my text")

myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")



# preview your object

# myTeamsMessage.printme()



# send the message

myTeamsMessage.send()
>>>>>>> 861a9871df338b80afdd4171139c81bf64ade184
