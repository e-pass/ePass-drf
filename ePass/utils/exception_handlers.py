from typing import Optional

from rest_framework import status
from rest_framework.exceptions import APIException


class UniqueUserHandler(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'User is already registered.'
    default_code = 'existing_user'

    def __init__(self, detail: Optional[str] = None, code: Optional[int] = None, attr: Optional[str] = None) -> None:
        detail = detail or self.default_detail
        code = code or self.default_code
        self.attr = attr
        super().__init__(detail, code)

    def get_full_details(self) -> list:
        return [
            {
                'code': self.default_code,
                'detail': self.detail,
                'attr': self.attr
            }
        ]
