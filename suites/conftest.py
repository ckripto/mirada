import os
import socket

import pytest

from libs.common import get_full_path_for, wait_for_success
from libs.config import Config
from libs.gns3 import GNSClient


@pytest.fixture(scope="session")
def config():
    yaml_config = os.getenv("CONFIG_FILE") or "configs/default.yaml"
    yield Config.from_file(get_full_path_for(yaml_config))


@pytest.fixture(scope="session")
def gns_client(config) -> GNSClient:
    wait_until_port_available(config.gns_server.host, config.gns_server.port)
    yield GNSClient(endpoint=f"{config.gns_server.schema}://{config.gns_server.host}:{config.gns_server.port}/"
                             f"{config.gns_server.path}/")


@wait_for_success(60, 5)
def wait_until_port_available(host: str, port: int = 3080) -> None:
    assert check_port_available(host, port), f"Port {port} on host {host} unavailable."


def check_port_available(host: str, port: int, timeout: int = 2) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
