from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from src.schemas.shortener import ShortenRequest, ShortenResponse
from src.services.shortener_service import ShortnerService

router = APIRouter()
service = ShortnerService()

@router.post("/shorten",response_model=ShortenResponse)
def shorten_url(payload:ShortenRequest,request:Request) ->ShortenResponse:



@router.get("/{code}")
def redirect_to_long_url(code: str) -> RedirectResponse:


    return RedirectResponse(url=long_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)