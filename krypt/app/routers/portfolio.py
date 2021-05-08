from fastapi import APIRouter

from utils import portfolio_utils, messaging_utils

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
    responses={404: {"description": "not found."}}
)


@router.get("/")
def get_portfolio():
    portfolio = portfolio_utils.Portfolio()
    return portfolio.breakdown()


@router.get("/sms_update")
def send_portfolio_sms_update():
    portfolio_summary = portfolio_utils.Portfolio().breakdown(format_for_sms=True)
    message_id = messaging_utils.send_sms(body=portfolio_summary)
    return message_id