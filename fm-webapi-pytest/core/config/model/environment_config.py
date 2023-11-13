from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class EnvironmentConfigDto:
    api_url: str = field(metadata=config(field_name="ApiUrl"))
    api_port: int = field(metadata=config(field_name="ApiPort"))
    api_base_path: str = field(metadata=config(field_name="ApiBasePath"))
