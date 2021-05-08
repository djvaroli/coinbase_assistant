import os
from typing import *
from app.utils.twilio_api_utils import get_twilio_client, TWILIO_PHONE_NUMBER


DEFAULT_TO_PHONE_NUMBER = os.environ.get("DEFAULT_TO_PHONE_NUMBER")


def send_sms(
    to: str = None,
    body: str = "",
    from_: str = TWILIO_PHONE_NUMBER
):
    if to is None:
        to = DEFAULT_TO_PHONE_NUMBER
    client = get_twilio_client()

    message = client.messages.create(
        body=body,
        from_=from_,
        to=DEFAULT_TO_PHONE_NUMBER
    )
    
    return message.sid


def compute_mean(values: List[Union[int, float]]):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)