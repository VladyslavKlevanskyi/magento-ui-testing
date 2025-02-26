import pytest

from data import sale_data


@pytest.mark.medium
def test_page_h1_header(sale_page):
    sale_page.open_page()
    sale_page.check_h1_is(text=sale_data.h1)


@pytest.mark.low
def test_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_title_is(text=sale_data.title)
