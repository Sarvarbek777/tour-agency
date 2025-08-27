from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from services.otp_services import OtpService
from utils.utils import generate_code

auth_router = APIRouter()


def otp_service():
    return OtpService()


@auth_router.post('/register')
async def login_view(service: OtpService = Depends(otp_service)):

    code = generate_code()
    print(code)
    service.send_otp_by_email(str(5121755384), str(code))
    return ORJSONResponse(
        {'message': 'Check your email to verify your account'},
    )
