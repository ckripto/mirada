import allure
import pytest


@pytest.mark.rules
@pytest.mark.static_rules
class TestStaticRules:
    @allure.title('Simple static firewall rule')
    def test_simple_static_rule(self, gns_client, server, client):
        raise NotImplemented("Not implemented yet")
