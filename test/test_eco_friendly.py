import pytest
from data import eco_friendly_data


@pytest.mark.smoke
def test_that_product_can_be_added_to_cart(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.add_product_to_cart()


@pytest.mark.smoke
def test_the_possibility_to_go_to_the_product_page(
        collections_eco_friendly_page
):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.go_to_product_page()


@pytest.mark.medium
def test_page_h1_header(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_h1_is(text=eco_friendly_data.h1)


@pytest.mark.low
def test_page_title(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_title_is(text=eco_friendly_data.title)


@pytest.mark.high
def test_page_does_not_display_more_than_selected_number_of_products(
        collections_eco_friendly_page
):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_number_of_products_is(number=12)
