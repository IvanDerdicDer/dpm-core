from pkg_resources import working_set
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass()
class Profile():
    username: str = field(default='')
    password: str = field(default='')
    authentication: str = field(default='')
