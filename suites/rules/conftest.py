import pytest

from libs.gns3 import GNSClient, Node, Project, Template


@pytest.fixture(scope="module")
def project(gns_client: GNSClient) -> Project:
    gns_client.delete_all_projects()
    project = gns_client.create_project("test_rules")
    yield project
    gns_client.delete_project(project.project_id)

@pytest.fixture(scope="module")
def vyos_template(gns_client: GNSClient) -> Template:
    for template in gns_client.list_templates():
        if "VyOS" == template.name:
            yield template
            break
    else:
        raise RuntimeError(f"VyOS not found on GNS server [{gns_client.endpoint}]")

@pytest.fixture(scope="module")
def server(gns_client: GNSClient, project: Project, vyos_template: Template) -> Node:
    vyos_template.name = "server"
    node = gns_client.create_template(vyos_template, project.project_id)
    yield node
    gns_client.delete_node(node)

@pytest.fixture(scope="module")
def client(gns_client: GNSClient, project: Project, vyos_template: Template) -> Node:
    vyos_template.name = "client"
    node = gns_client.create_template(vyos_template, project.project_id)
    yield node
    gns_client.delete_node(node)
