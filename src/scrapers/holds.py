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
            print(f"Error: Unable to process {target_url}: {e}")
        finally:
            browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper


def scrape_menagerie(
    site_identifier="menagerie",
    target_url="https://menagerieclimb.com/collections/all-grips",
):
    """
    scrapes product images from menagerie website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            while True:
                page.wait_for_selector("div.grid-view-item")
                product_items = page.query_selector_all("div.grid-view-item")
                for item in product_items:
                    link_element = item.query_selector("a")
                    img_element = item.query_selector(
                        "div.grid-view-item__image-wrapper.js div img"
                    )
                    image_id = (
                        link_element.get_attribute("href") if link_element else None
                    )
                    image_source = (
                        img_element.get_attribute("src") if img_element else None
                    )
                    product_image = {
                        "image_id": image_id.lstrip("/collections/all-grips/products"),
                        "image_source": f"https:{image_source}",
                    }
                    product_array.append(product_image)
                if page.query_selector(
                    "a.btn.btn--secondary.btn--narrow svg.icon.icon--wide.icon-arrow-right"
                ):
                    next_button = page.query_selector(
                        "svg.icon.icon--wide.icon-arrow-right >> .."
                    )
                    next_button.click()
                    page.wait_for_timeout(3000)
                    # print("Success: Navigating to next page")
                else:
                    # print("Success: No more pages to navigate to")
                    break
        except Exception as e:
            print(f"Error: Unable to process {target_url}: {e}")
        finally:
            browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper


def scrape_decoy(
    site_identifier="decoy", target_url="https://decoy-holds.com/pages/8x12-board-sets"
):
    """
    scrapes product images from the decoy website
    """
    product_array = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            page.wait_for_selector("div.rte")
            center_items = page.query_selector_all(
                "div.rte div[style='text-align: center;']"
            )
            for item in center_items:
                title_element = item.query_selector("a")
                img_element = item.query_selector("img")
                if img_element and title_element:
                    image_id = (
                        title_element.get_attribute("title").strip()
                        if title_element
                        else None
                    )
                    image_source = (
                        img_element.get_attribute("src").strip()
                        if img_element
                        else None
                    )
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
        site_identifier: product_array,
    }
    return wrapper


def scrape_setter_closet(
    site_identifier="setter_closet",
    target_url="https://settercloset.com/collections/all-grips",
):
    """
    NOTE - this function is deprecated
    scrapes product images from the setter closet website
    """
    product_array = []
    count = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url)
            print(f"Success: Retrieved page URL {target_url}")
            page.wait_for_selector("a.product-card")
            product_cards = page.query_selector_all("a.product-card")
            for card in product_cards:
                count += 1
                image_id = card.get_attribute("href")
                img_element = card.query_selector(
                    "div.product-card__image-container div.product-card__image-wrapper div.product-card__image.js div img"
                )
                if img_element:
                    page.wait_for_timeout(1000)
                    data_srcset = img_element.get_attribute("data-srcset")
                    if data_srcset:
                        image_source = data_srcset.split(",")[-1].strip()
                    else:
                        image_source = None
                else:
                    image_source = None
                product_image = {
                    "image_id": image_id,
                    "image_source": f"https{image_source}".rstrip("1080w").strip(),
                }
                print(count, product_image)
                product_array.append(product_image)
        except Exception as e:
            print(f"Error: Unable to process {target_url}: {e}")
        finally:
            browser.close()
    wrapper = {
        site_identifier: product_array,
    }
    return wrapper


def scrape_tension(
    site_identifier="tension",
    target_url="https://tensionclimbing.com/products/wooden-hold-packs",
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
            page.wait_for_selector("ul.slider__grid li")
            items = page.query_selector_all("ul.slider__grid li")
            for item in items:
                image_id = item.get_attribute("data-media-id")
                link_element = item.query_selector("a")
                image_source = (
                    link_element.get_attribute("href") if link_element else None
                )
                product_image = {
                    "image_id": image_id,
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


def scrape_moon(
    site_identifier="moon",
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
                img_element = card.query_selector(
                    "div div a.product.photo.product-item-photo.block img"
                )
                image_source = (
                    img_element.get_attribute("data-src") if img_element else None
                )
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
        site_identifier: product_array,
    }
    return wrapper
