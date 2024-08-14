import re
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait


def parse_html(html):
    """Parse content from various tags from OpenTable restaurants listing"""
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(html, "lxml")
    for i, resto in enumerate(
        soup.find_all("div", class_="styles_businessUnitResult__L3bbC")
    ):
        try:
            card = resto.find("a", attrs={"name": "business-unit-card"})

            name = card.find("p", class_="styles_displayName__GOhL2")
            item["name"] = name.text if name else None

            site = card["href"] if "href" in card.attrs else None
            item["site"] = (
                re.search(r"/review/([^/]+)", site).group(1) if site else None
            )

            reviews = card.find("p", class_="styles_ratingText__yQ5S7")
            item["reviews"] = (
                int(re.search(r"\d+", reviews.text).group()) if reviews else None
            )

            rating = reviews.find("span", class_="styles_trustScore__8emxJ")
            item["rating"] = (
                float(re.search(r"\d+.*\d*", rating.text).group()) if rating else None
            )

            location = card.find(
                "span",
                class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l "
                + "styles_metadataItem__Qn_Q2 styles_location__ILZb0",
            )
            item["location"] = location.text if location else None
        except Exception:
            pass

        try:
            foot = resto.find(
                "div",
                class_="styles_wrapper___E6__ styles_categoriesLabels__FiWQ4 "
                + "styles_desktop__U5iWw",
            )
            label_values = []
            for _, label in enumerate(
                foot.find_all(
                    "span",
                    class_="typography_appearance-default__AAY17",
                )
            ):
                if label:
                    label_values.append(label.text)
            item["category"] = ",".join(label_values)
        except Exception:
            pass

        data[i] = pd.Series(item)
    return data.T


# Start selenium and click through pages until reach end
# store results by iteratively appending to csv file
driver = webdriver.Chrome()
url = "https://www.trustpilot.com/search?query=tribal+loan"
driver.get(url)
page = collected = 0
while True:
    sleep(5)
    new_data = parse_html(driver.page_source)
    if new_data.empty:
        break
    if page == 0:
        new_data.to_csv("./03_alternative_data/01_opentable/results.csv", index=False)
    elif page > 0:
        new_data.to_csv(
            "./03_alternative_data/01_opentable/results.csv",
            index=False,
            header=None,
            mode="a",
        )
    page += 1
    collected += len(new_data)
    print(f"Page: {page} | Downloaded: {collected}")
    WebDriverWait(driver, 10).until(
        element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Next page']"))
    )
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Next page']").click()

driver.close()
restaurants = pd.read_csv("./03_alternative_data/01_opentable/results.csv")
print(restaurants)
