def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']


def get_slot(intent_request, slot_name):
    slots = get_slots(intent_request)
    if slots is not None and slot_name in slots and slots[slot_name] is not None:
        return slots[slot_name]['value']['interpretedValue']
    else:
        return None


def get_session_attributes(intent_request):
    session_state = intent_request['sessionState']
    if 'sessionAttributes' in session_state:
        return session_state['sessionAttributes']

    return {}


def get_request_attributes(intent_request):
    if 'sessionAttributes' in intent_request:
        return intent_request['requestAttributes']

    return {}

