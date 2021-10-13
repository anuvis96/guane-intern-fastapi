from typing import Any, Dict, Optional, TypeVar

from pydantic.main import BaseModel

from app.infra.httpx.client import HTTPClient
from app.infra.services.base import IServiceBase
from app.infra.services.responses import Responses

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(IServiceBase[CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        url: str,
        check_codes: Responses = Responses(),
        client: HTTPClient = HTTPClient(),
    ):
        self.url = url
        self._client = client
        self._check_codes = check_codes

    async def create(self, *, obj_in: CreateSchemaType) -> Any:
        url = f"{self.url}"
        body = obj_in.dict()
        response = await self._client.post(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def update(self, *, _id: int, obj_in: UpdateSchemaType) -> Any:
        url = f"{self.url}/{_id}"
        body = obj_in.dict()
        response = await self._client.patch(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def delete(self, *, _id: int) -> Any:
        url = f"{self.url}/{_id}"
        response = await self._client.delete(url_service=url)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def get_by_id(self, *, _id: int) -> Any:
        url = f"{self.url}/{_id}"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def get_all(
        self, payload: Optional[Dict[str, Any]], skip: int, limit: int
    ) -> Any:
        if payload:
            payload.update({"skip": skip, "limit": limit})
        else:
            payload = {"skip": skip, "limit": limit}
        response = await self._client.get(url_service=self.url, params=payload)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response
