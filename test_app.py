from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#line-graph", timeout=10)


def test_show_all_button_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#show-all-button", timeout=10)


def test_show_none_button_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#show-none-button", timeout=10)
