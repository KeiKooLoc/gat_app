"""Test configs."""
import pytest
from webapp.panels import Panel, PanelOne, PanelTwo, PanelThree


def test_base_panel_error():
    p = Panel()
    with pytest.raises(NotImplementedError):
        p.calculate_price()

    # def test_panl_one_price():
    #     assert True

    # def test_panl_two_price():
    #     assert True

    # def test_panl_three_price():
    #     assert True