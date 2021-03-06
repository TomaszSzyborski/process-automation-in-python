from fastapi import APIRouter, Request

from application_server.rest_introduction_app.api.fundamentals.core.headers_dicts import \
    playing_with_headers_non_authorized, API_KEY, playing_with_headers_auth_dict
from application_server.rest_introduction_app.api.fundamentals.core.responses import get_response

router = APIRouter()


@router.get("/header_check")
async def check_your_request_header(request: Request):
    """
    Try that on Swagger Docs. If should return status code 200.
    Use header "apikey": "woohoo"
    """

    return get_response(200 if request.headers.get(API_KEY) == playing_with_headers_auth_dict.get(API_KEY) else 403,
                        playing_with_headers_non_authorized)
