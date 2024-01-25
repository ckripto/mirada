import json
from typing import Any, Optional

from libs.common import Requests
from libs.gns3.node import Node
from libs.gns3.project import Project
from libs.gns3.template import Template


class GNSClient:
    endpoint: str
    _default_project_id: Optional[str] = None

    def __init__(self, endpoint: str):
        self.endpoint: str = endpoint

    def create_project(self, name: str) -> Project:
        response = Requests.post(
            url=self.endpoint + "projects",
            json_data={"name": name},
        )
        assert response.status_code == 201
        return Project.from_dict(
            json.loads(response.text),
        )

    def list_projects(self) -> list[Project]:
        return [Project.from_dict(project) for project in self._get("projects")]

    def delete_project(self, project_id: str) -> None:
        response = Requests.delete(
            url=self.endpoint + f"projects/{project_id}",
        )
        assert response.status_code == 204

    def delete_all_projects(self) -> None:
        for project in self.list_projects():
            self.delete_project(project.project_id)

    def create_node(self, node: Node, project_id: Optional[str] = None) -> Node:
        project_id = project_id or node.project_id or self._default_project_id
        assert project_id, "Project ID must be set"
        response = Requests.post(
            url=self.endpoint + f"projects/{project_id}/nodes",
            json_data=node.create_dict(),
        )
        assert response.status_code == 201
        return Node.from_dict(
            json.loads(response.text),
        )

    def list_nodes(self, project_id: str) -> list[Node]:
        return [Node.from_dict(node) for node in self._get(f"projects/{project_id}/nodes")]

    def delete_node(self, node: Node) -> None:
        response = Requests.delete(
            url=self.endpoint + f"projects/{node.project_id}/nodes/{node.node_id}",
        )
        assert response.status_code == 204

    def create_template(self, template: Template, project_id: Optional[str] = None) -> Node:
        project_id = project_id or self._default_project_id
        assert project_id, "Project ID must be set"
        response = Requests.post(
            url=self.endpoint + f"projects/{project_id}/templates/{template.template_id}",
            json_data={"compute_id":"local", "x": 0, "y":0, "name": template.name},
        )
        assert response.status_code == 201
        return Node.from_dict(
            json.loads(response.text),
        )

    def list_templates(self) -> list[Template]:
        response = Requests.get(
            url=self.endpoint + "templates",
        )
        assert response.status_code == 200
        return [Template.from_dict(template) for template in json.loads(response.text)]

    def _post(self, handle: str, json_data: Optional[dict] = None) -> dict[str, Any]:
        response = Requests.post(
            url=self.endpoint + handle,
            json_data=json_data,
        )
        assert response.status_code == 200
        return json.loads(response.text)

    def _get(self, handle: str) -> Any:
        response = Requests.get(
            url=self.endpoint + handle,
        )
        assert response.status_code == 200
        return json.loads(response.text)
