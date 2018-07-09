"""Test configs."""
import json 
import pytest
from webapp.panels import Panel, PanelOne, PanelTwo, PanelThree

HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Title</title>
    </head>
    <body>
        <header>
        </header>
        <main>
            <p>Lorem ipsum dolor sit amet justo. Aliquam ante sit amet ultricies urna orci eget egestas sodales,
            augue nec sem nec nulla. Duis ornare euismod. Vestibulum ullamcorper pellentesque. 
            Proin scelerisque sem. Pellentesque at arcu. Pellentesque habitant morbi tristique sodales. 
            Vivamus iaculis, dui sit amet dui. Etiam varius, scelerisque a, faucibus orci ac nunc fringilla enim. 
            Aliquam fringilla, massa. Vivamus ut massa. Curabitur nunc. Suspendisse auctor, sapien sapien, ornare id, 
            tortor. Cum sociis natoque penatibus et nunc ac lectus. In quis nisl. Curabitur arcu quis ipsum. 
            Lorem ipsum primis in vestibulum ac, accumsan vestibulum. Nullam justo. Nulla cursus ut, eleifend
            pede urna sem pede eget augue. Morbi et lacus ultrices posuere, lacus eu odio. Mauris metus. 
            Nulla gravida gravida justo, eget magna. Aliquam nec magna sapien, tempus arcu. Cum sociis natoque penatibus et leo.
            Suspendisse vel ipsum eget nisl. Nulla ligula lorem urna fringilla ante in risus. Sed tempus nulla. 
            Ut wisi vulputate sed, urna. Donec ullamcorper, risus at porttitor magna. Suspendisse ut pede. 
            Curabitur interdum. Donec porttitor varius sit amet lacus. Vivamus lacus sit amet augue at elit eu ante. 
            Quisque.</p>
        </main>
    </body>
</html>
"""

data = """{
    "cars": {
        "Nissan": [
            {"model":"Sentra", "doors":4},
            {"model":"Maxima", "doors":4},
            {"model":"Skyline", "doors":2}
        ],
        "Ford": [
            {"model":"Taurus", "doors":4},
            {"model":"Escort", "doors":4}
        ]
    }
}"""

# TODO Refactor tests.

def test_base_panel_calculate_price():
    p = Panel()
    with pytest.raises(NotImplementedError):
        p.calculate_price()

def test_panel_one_url():
    p = PanelOne()
    assert 'http://time.com', p.url

def test_panel_two_url():
    p = PanelTwo()
    test_url = 'http://openlibrary.org/earch.json?q=the+lord+of+the+rings'
    assert test_url, p.url

def test_panel_three_url():
    p = PanelThree()
    assert 'http://time.com', p.url

def test_panel_one_price():
    p = PanelOne()
    p.url_content = HTML
    assert 0.88, p.calculate_price()

#  TODO panel two class and test
# def test_panel_two_price():
#     p = PanelTwo()
#     p.url_content = data
#     assert 0, p.calculate_price()


def test_panel_three_price():
    p = PanelThree()
    p.url_content = HTML
    assert 0.01, p.calculate_price()