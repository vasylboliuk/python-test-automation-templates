import dataclasses
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional, Dict, Any


@dataclass_json
@dataclass
class UserGeo:
    lat: str
    lng: str


@dataclass_json
@dataclass
class UserAddress:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: UserGeo


@dataclass_json
@dataclass
class UserCompany:
    name: str
    catch_phrase: str = field(metadata=config(field_name="catchPhrase"))
    bs: str


@dataclass_json
@dataclass
class UserDto:
    name: str
    username: str
    id: Optional[int] = None
    email: Optional[str] = None
    address: Optional[UserAddress] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[UserCompany] = None

    def as_dict(self, exclude_none=False) -> Dict[str, Any]:
        if exclude_none:
            return dataclasses.asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        return dataclasses.asdict(self, dict_factory=lambda x: {k: v for (k, v) in x})
