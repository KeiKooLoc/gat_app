"""Test configs."""
import pytest
from webapp.panels import Panel, PanelOne, PanelTwo, PanelThree


def test_base_panel_error():
    p = Panel()
    with pytest.raises(NotImplementedError):
        p.calculate_price()

def test_panl_one_url():
    p = PanelOne()
    assert 'http://time.com', p.url

def test_panl_two_price():
    p = PanelTwo()
    test_url = 'http://openlibrary.org/earch.json?q=the+lord+of+the+rings'
    assert test_url, p.url

def test_panl_three_url():
    p = PanelThree()
    assert 'http://time.com', p.url