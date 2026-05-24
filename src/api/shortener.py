from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from src.schemas.shortener import ShortenRequest, ShortenResponse
from src.services.shortener_service import ShortnerService

router = APIRouter()
service = ShortnerService()

@router.post("/shorten",response_model=ShortenResponse)
def shorten_url(payload:ShortenRequest,request:Request) ->ShortenResponse:
    code = service.save_url(str(payload.long_url))
    short_url = str(request.base_url).rstrip("/")+f"/{code}"

    return ShortenResponse(
        code = code,
        short_url=short_url,
        long_url = payload.long_url
    )


@router.get("/{code}")
def redirect_to_long_url(code: str) -> RedirectResponse:
    long_url = service.get_long_url(code)

    if long_url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Short code not found",
        )

    return RedirectResponse(url=long_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)