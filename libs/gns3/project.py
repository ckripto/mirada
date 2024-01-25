from dataclasses import dataclass
from typing import Optional


@dataclass
class Project:
    name: Optional[str] = None
    project_id: Optional[str] = None
    filename: Optional[str] = None
    path: Optional[str] = None
    status: Optional[str] = None
    auto_close: Optional[bool] = None
    auto_open: Optional[bool] = None
    auto_start: Optional[bool] = None
    drawing_grid_size: Optional[int] = None
    grid_size: Optional[int] = None
    scene_height: Optional[int] = None
    scene_width: Optional[int] = None
    show_grid: Optional[bool] = None
    show_interface_labels: Optional[bool] = None
    show_layers: Optional[bool] = None
    snap_to_grid: Optional[bool] = None
    zoom: Optional[int] = None
    supplier: Optional[str] = None
    variables: Optional[str] = None

    @staticmethod
    def from_dict(project_dict: dict[str, str]) -> "Project":
        return Project(**{param: value for param, value in project_dict.items()})
