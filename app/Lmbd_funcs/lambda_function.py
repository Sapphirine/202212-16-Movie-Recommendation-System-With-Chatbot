import time
import os
import logging
from utils.intents import collect_type, collect_data, welcome, login

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def dispatch(intent_request, context):
    """
    Called when the user specifies an intent for this bot.
    """

    # logger.debug(
    #     "dispatch userId={}, intentName={}".format(intent_request["userId"], intent_request["currentIntent"]["name"]))

    intent_name = intent_request["sessionState"]["intent"]["name"]

    # Dispatch to your chatbot intent handlers
    if intent_name == "collect_type":
        return collect_type(intent_request, context)
    elif intent_name == "collect_data":
        return collect_data(intent_request, context)
    elif intent_name == "Welcome":
        return welcome(intent_request)
    elif intent_name == "login":
        return login(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ["TZ"] = "America/New_York"
    time.tzset()
    # logger.debug("event.bot.name={}".format(event["bot"]["name"]))

    return dispatch(event, context)


