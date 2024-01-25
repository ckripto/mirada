from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class ConfigGNSServer:
    schema: str = "http"
    host: str = "localhost"
    port: int = 3080
    path: str = "v2"

    @staticmethod
    def from_dict(config_dict: dict[str, str]) -> "ConfigGNSServer":
        return ConfigGNSServer(**{param: value for param, value in config_dict.items()})


@dataclass
class Config:
    gns_server: ConfigGNSServer

    @staticmethod
    def from_dict(config_dict: dict[str, Any]) -> "Config":
        return Config(
            gns_server=ConfigGNSServer.from_dict(config_dict.get("gns_server", {})),
        )

    @staticmethod
    def from_file(yaml_config_file_name: str) -> "Config":
        with open(yaml_config_file_name) as yaml_config_file:
            config = yaml.load(yaml_config_file, Loader=yaml.FullLoader) or {}
        return Config.from_dict(config)
