from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Optional


class TemplateType(Enum):
    cloud = "cloud"
    ethernet_hub = "ethernet_hub"
    ethernet_switch = "ethernet_switch"
    docker = "docker"
    dynamips = "dynamips"
    vpcs = "vpcs"
    traceng = "traceng"
    virtualbox = "virtualbox"
    vmware = "vmware"
    iou = "iou"
    qemu = "qemu"
    nat = "nat"
    frame_relay_switch = "frame_relay_switch"
    atm_switch = "atm_switch"


@dataclass
class Template:
    builtin: Optional[bool] = None
    category: Optional[str] = None
    compute_id: Optional[str] = None
    console_type: Optional[str] = None
    console_auto_start: Optional[bool] = None
    cpu_throttling: Optional[bool] = None
    cpus: Optional[str] = None
    default_name_format: Optional[str] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    template_id: Optional[str] = None
    template_type: Optional[TemplateType] = None
    adapter_type: Optional[str] = None
    bios_image: Optional[str] = None
    boot_priority: Optional[str] = None
    properties: Optional[field(default_factory=dict)] = None
    adapters: Optional[field(default_factory=list)] = None
    cdrom_image: Optional[str] = None

    @staticmethod
    def from_dict(template_dict: dict[str, Any]) -> "Template":
        if "template_type" in template_dict:
            template_dict["template_type"] = TemplateType(template_dict["template_type"])
        return Template(**{param: value for param, value in template_dict.items() if param in Template.__dict__.keys()})

    def dict(self) -> dict[str, Any]:
        template_dict = asdict(self)
        return {param: value for param, value in template_dict.items() if value is not None}
