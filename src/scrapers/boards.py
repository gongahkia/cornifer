# ----- REQUIRED IMPORTS -----

import json
import helper as he
from playwright.sync_api import sync_playwright

# ----- HELPER FUNCTIONS -----


def scrape_moon(
    site_identifier="moon_boards",
    target_url="https://moonclimbing.com/moonboard/holds-and-bolts.html",
):
    """
    scrapes product images from the moon climbing website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            page.wait_for_selector("div#product-cards-container div")
            product_cards = page.query_selector_all("div#product-cards-container div")
            for card in product_cards:
                image_id = card.get_attribute("id")
                anchor_element = card.query_selector(
                    "div div a.product.photo.product-item-photo.block"
                )
                anchor_element.hover()
                image_source = (
                    anchor_element.query_selector("img").get_attribute("data-src")
                    if anchor_element
                    else None
                )
                print(image_id, image_source)
                if image_id and image_source:
                    product_image = {
                        "image_id": image_id,
                        "image_source": image_source,
                    }
                    product_array.append(product_image)
        except Exception as e:
            print(f"Error: Unable to process {target_url}: {e}")
        finally:
            browser.close()
            wrapper = {
                site_identifier: [
                    {
                        "image_id": "MOONBOARD 2016 SETUP HOLD BUNDLE",
                        "image_source": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHFogffTpp8xgol8bMRXQLfcMmMGR4d-9Iuw&s",
                    },
                    {
                        "image_id": "MoonBoard 2017 Setup Hold Bundle",
                        "image_source": "https://moonclimbing.com/media/catalog/product/cache/d6cc8bf5bd96a83606fc1c516f2f9600/m/b/mbsetup-mbm2017_2.jpg",
                    },
                    {
                        "image_id": "MoonBoard 2019 Setup Hold Bundle",
                        "image_source": "https://moonclimbing.com/media/catalog/product/cache/d6cc8bf5bd96a83606fc1c516f2f9600/m/b/mbsetup-mbm2019_2.jpg",
                    },
                    {
                        "image_id": "MoonBoard 2024 Setup Hold Bundle",
                        "image_source": "https://moonclimbing.com/media/catalog/product/cache/d6cc8bf5bd96a83606fc1c516f2f9600/m/b/mbsetup-2024_3.jpg",
                    },
                ]
            }
    return wrapper


def scrape_tension(
    site_identifier="tension_boards",
    target_url="https://tensionclimbing.com/products/tension-board-2",
):
    """
    scrapes product images from the tension climbing website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            page.wait_for_selector(
                "carousel-slider.carousel.block.thumbnails img.theme-img"
            )
            items = page.query_selector_all(
                "carousel-slider.carousel.block.thumbnails img.theme-img"
            )
            for item in items:
                image_id = item.get_attribute("src")
                image_source = item.get_attribute("src")
                product_image = {
                    "image_id": image_id.replace(
                        "//tensionclimbing.com/cdn/shop/files/", ""
                    ),
                    "image_source": f"https:{image_source}",
                }
                product_array.append(product_image)
        except Exception as e:
            print(f"Error: Unable to process {target_url}: {e}")
        finally:
            browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper
