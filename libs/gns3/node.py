from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional


class NodeStatus(Enum):
    started = "started"
    stopped = "stopped"
    undefined = None


@dataclass
class Node:
    compute_id: str = "local"
    console: Optional[int] = None
    console_host: Optional[str] = None
    console_type: Optional[str] = None
    console_auto_start: Optional[bool] = None
    locked: Optional[bool] = None
    command_line: Optional[str] = None
    custom_adapters: list = field(default_factory=list)
    ports: list = field(default_factory=list)
    label: dict = field(default_factory=dict)
    first_port_name: Optional[str] = None
    port_name_format: Optional[str] = None
    port_segment_size: Optional[int] = None
    height: Optional[int] = None
    name: Optional[str] = None
    node_id: Optional[str] = None
    node_type: Optional[str] = None
    node_directory: Optional[str] = None
    symbol: Optional[str] = None
    project_id: Optional[str] = None
    status: NodeStatus = NodeStatus.undefined
    properties: dict = field(default_factory=dict)
    template_id: Optional[str] = None
    width: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    z: Optional[int] = None

    @staticmethod
    def from_dict(node_dict: dict[str, Any]) -> "Node":
        if "status" in node_dict:
            node_dict["status"] = NodeStatus(node_dict["status"])
        return Node(**{param: value for param, value in node_dict.items()})

    def create_dict(self) -> dict[str, str]:
        return {
            "compute_id": self.compute_id,
            "name": self.name,
            "node_type": self.node_type,
            "template_id": self.template_id,
        }
