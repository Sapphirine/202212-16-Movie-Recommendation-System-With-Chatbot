import json
import os
from datetime import datetime
import time

# from dotenv import load_dotenv
import requests
# from botocore.vendored import requests

from utils.action_types import close, elicit_slot, elicit_intent
from utils.helpers import get_slot, get_session_attributes, get_request_attributes

# load_dotenv()

HEADERS = {"Authorization": "bearer %s" % os.getenv("S3_KEY")}


def welcome(intent_request):
    session_attributes = get_session_attributes(intent_request)
    fulfillment_state = "Fulfilled"
    message = {
        "contentType": "PlainText",
        "content": "Hi there, I am your personal movie recommend. How can I help?"
    }

    return elicit_intent(intent_request, session_attributes, fulfillment_state, message)
    
def login(intent_request):
    session_attributes = get_session_attributes(intent_request)
    requests_attributes = get_request_attributes(intent_request)
    session_id = intent_request["sessionId"]
    user_id = get_slot(intent_request, "userID")
    uid = requests.get(url=os.getenv("mangodb_URL") + user_id, headers=HEADERS)
    fulfillment_state = "Fulfilled"
    session_attributes["user"] = uid
    message = {
        "contentType": "PlainText",
        "content": "your username has been loged in"
    }
    intent = {
            "confirmationState": "None",
            "name": "login",
            "slots": {
                "businessID": None
            },
            "state": "InProgress"
        }
    return elicit_slot(session_attributes, intent, slot_to_elicit, messages, requests_attributes, session_id)


def collect_type(intent_request):
    session_attributes = get_session_attributes(intent_request)
    requests_attributes = get_request_attributes(intent_request)
    session_id = intent_request["sessionId"]
    movie_type = get_slot(intent_request, "type")
    session_attributes["type"] = movie_type
    fulfillment_state = "Fulfilled"
    intent = {
            "confirmationState": "None",
            "name": "collect_type",
            "slots": {
                "type": movie_type
            },
            "state": "InProgress"
        }
    messages = [{
                "contentType": "PlainText",
                "content": "Your recommendation will be generated shortly"
            }]
    return elicit_slot(session_attributes, intent, slot_to_elicit, messages, requests_attributes, session_id)
    
    
    
    
    
def collect_data():
    session_attributes = get_session_attributes(intent_request)
    requests_attributes = get_request_attributes(intent_request)
    
    # requests_attributes = get_request_attributes(intent_request)


    passon_data = {'user_id': session_attributes["user"],
                     'Type': session_attributes["type"]
                     }

    session_id = intent_request["sessionId"]

    API_ENDPOINT = "http://44.206.***.99:8080/save"
    
    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, json=passon_data)

    # for test
    # return r.json()
    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)

    session_id = intent_request["sessionId"]

    intent = {
        "confirmationState": "None",
        "name": "collect_data",
        "slots": {
            "reserve": None
        },
        "state": "InProgress"
    }
    
    messages = [{
        "contentType": "PlainText",
        "content": ""
    }]

    return elicit_slot(session_attributes, intent, "reserve", messages, requests_attributes, session_id)
    