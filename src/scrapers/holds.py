import json
from playwright.sync_api import sync_playwright


def scrape_atomik(
    site_identifier="atomik",
    target_url="https://www.atomikclimbingholds.com/bulk-packs-2",
):
    """
    scrapes product images from atomik's website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            page.wait_for_selector("div.item-box div.product-item.product-box")
            product_items = page.query_selector_all(
                "div.item-box div.product-item.product-box"
            )
            for item in product_items:
                picture_element = item.query_selector("div.picture")
                if picture_element:
                    link_element = picture_element.query_selector("a")
                    img_element = picture_element.query_selector("img")
                    image_id = (
                        link_element.get_attribute("href") if link_element else None
                    )
                    image_source = (
                        img_element.get_attribute("src") if img_element else None
                    )
                    product_image = {
                        "image_id": image_id.strip("/"),
                        "image_source": image_source,
                    }
                    product_array.append(product_image)
        except Exception as e:
            print(f"Error processing {target_url}: {e}")
        finally:
            browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper
