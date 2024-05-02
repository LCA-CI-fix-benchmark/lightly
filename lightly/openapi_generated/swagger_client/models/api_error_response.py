# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import Extra,  BaseModel, Field, StrictStr, conlist
from lightly.openapi_generated.swagger_client.models.api_error_code import ApiErrorCode

class ApiErrorResponse(BaseModel):
    """
    ApiErrorResponse
    """
    code: ApiErrorCode = Field(...)
    error: StrictStr = Field(..., description="The detailed error message or code of the error")
    request_id: Optional[StrictStr] = Field(None, alias="requestId", description="The identifier of a request. Helpful for debugging")
    error_labels: Optional[conlist(StrictStr)] = Field(None, alias="errorLabels", description="Can occur on database errors")
    __properties: List[str] = ["code", "error", "requestId", "errorLabels"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = Extra.forbid

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> ApiErrorResponse:
        """Create an instance of ApiErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiErrorResponse:
        """Create an instance of ApiErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorResponse.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ApiErrorResponse) in the input: " + str(obj))

        _obj = ApiErrorResponse.parse_obj({
            "code": obj.get("code"),
            "error": obj.get("error"),
            "request_id": obj.get("requestId"),
            "error_labels": obj.get("errorLabels")
        })
        return _obj

