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
    scrapes product images from the moonboard website
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
    scrapes product images from the tension board website
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


def scrape_grasshopper(
    site_identifier="grasshopper_boards",
    target_url="https://grasshopperclimbing.com/products/",
):
    """
    scrapes product images from the grasshopper board website
    """
    wrapper = {
        site_identifier: [
            {
                "image_id": "GRASSHOPPER 8 X 10",
                "image_source": "https://grasshopperclimbing.com/wp-content/uploads/2022/10/ninja_01.png",
            },
            {
                "image_id": "GRASSHOPPER 8 X 12",
                "image_source": "https://grasshopperclimbing.com/wp-content/uploads/2022/10/master_01.png",
            },
            {
                "image_id": "GRASSHOPPER 12 X 12",
                "image_source": "https://grasshopperclimbing.com/wp-content/uploads/2022/10/grandmaster_01.png",
            },
        ]
    }
    return wrapper


def scrape_kilter(
    site_identifier="kilter_boards",
    target_url="https://settercloset.com/pages/kb-layouts",
):
    """
    scrapes product images from the kilter board website
    """
    wrapper = {
        site_identifier: [
            {
                "image_id": "Home Wall Kilter Board 7x10 Mainline (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb710main-whitecrop.jpg?v=1668723662&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 7x10 Auxiliary (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb710aux-whitecrop.jpg?v=1668723662&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 7x10 Fullride (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb710full-whitecrop.jpg?v=1668723768&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 8x12 Mainline (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb812main-kick.jpg?v=1668723659&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 8x12 Auxiliary (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb812aux-kick.jpg?v=1668723656&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 8x12 Fullride (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb812full-kick.jpg?v=1668723661&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x10 Mainline (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1010main-whitecrop.jpg?v=1668723669&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x10 Auxiliary (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1010aux-whitecrop.jpg?v=1668723670&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x10 Fullride (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1010full-whitecrop.jpg?v=1668723670&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x12 Mainline (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1012main-kick.jpg?v=1668723666&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x12 Auxiliary (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1012aux-kick.jpg?v=1668723666&width=1946",
            },
            {
                "image_id": "Home Wall Kilter Board 10x12 Fullride (Holds)",
                "image_source": "https://seriousclimbing.com/cdn/shop/products/hwkb1012full-kick.jpg?v=1668723666&width=1946",
            },
        ]
    }
    return wrapper


def scrape_decoy(
    site_identifier="decoy_boards",
    target_url_array=[
        "https://decoy-holds.com/collections/decoy-board/products/decoy-board-8x10-cropped-without-light-kit",
        "https://decoy-holds.com/collections/decoy-board/products/decoy-board-12x12-layout-without-lights",
        "https://decoy-holds.com/collections/decoy-board/products/copy-of-decoy-board-8x12-complete-without-light-kit",
    ],
):
    """
    scrapes product images from decoy board website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for url in target_url_array:
            try:
                page.goto(url)
                print(f"Success: Retrieved page URL {url}")
                page.wait_for_selector(
                    "div.product__photo.slick-slide.slick-active img.productImg"
                )
                img_element = page.query_selector(
                    "div.product__photo.slick-slide.slick-active img.productImg"
                )
                if img_element:
                    image_source = img_element.get_attribute("src")
                    image_id = img_element.get_attribute("data-image-id")
                    product_image = {
                        "image_id": image_id,
                        "image_source": f"http:{image_source}",
                    }
                    product_array.append(product_image)
            except Exception as e:
                print(f"Error: Unable to process {url}: {e}")
        browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper


def scrape_boards_wrapper(target_log_filepath):
    """
    wrapper function that calls all working boards scrapers and writes the result to the specified filepath
    """
    try:
        he.write_json(scrape_moon(), target_log_filepath)
        he.write_json(scrape_tension(), target_log_filepath)
        he.write_json(scrape_grasshopper(), target_log_filepath)
        he.write_json(scrape_kilter(), target_log_filepath)
        he.write_json(scrape_decoy(), target_log_filepath)
        print("Success: All boards scrapers completed execution")
        return True
    except Exception as e:
        print(
            f"Error: Unable to run all scrapers and write to {target_log_filepath}: {e}"
        )
        return False
