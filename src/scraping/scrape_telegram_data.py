from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

def fetch_message_details():
    TELEGRAM_URL = "https://t.me/tikvahethiopia/87808"
    
    # Example post data
    posts = [{"channel_username": "tikvahethiopia", "message_id": "87808"}]

    messages = {}

    # Configure Selenium
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    for post in posts:
        try:
            # Navigate to the target Telegram message URL
            driver.get(f"{TELEGRAM_URL}?embed=1&mode=tme")
            time.sleep(2)  # Wait for the page to load

            # Extract the message content from the page
            try:
                message_content = driver.find_element(
                    By.CSS_SELECTOR, ".tgme_widget_message_text"
                ).get_attribute("innerHTML")
            except Exception:
                message_content = None

            # Extract the number of views from the page
            try:
                views = driver.find_element(
                    By.CSS_SELECTOR, ".tgme_widget_message_views"
                ).text
            except Exception:
                views = None

            # Extract the date of the post from the page
            try:
                post_date = driver.find_element(By.CSS_SELECTOR, ".datetime").text
            except Exception:
                post_date = None

            # Extract the HTML for any images in the post
            try:
                post_image_html = driver.find_element(
                    By.CSS_SELECTOR, ".tgme_widget_message_grouped_wrap"
                ).get_attribute("innerHTML")
            except Exception:
                try:
                    post_image_html = driver.find_element(
                        By.CSS_SELECTOR, ".tgme_widget_message_photo_wrap"
                    ).get_attribute("style")
                except Exception:
                    post_image_html = None

            # Store the extracted data in the messages object
            messages[post["message_id"]] = {
                "channel_username": post["channel_username"],
                "message_id": post["message_id"],
                "message_link": TELEGRAM_URL,
                "views": views if views else "",
                "message_content": message_content if message_content else "",
                "date": post_date if post_date else "",
                "image_html": post_image_html if post_image_html else "",
            }

        except Exception as e:
            print(f"Error fetching data for post {post['message_id']}: {str(e)}")

    driver.quit()

    return messages

def save_data_to_xlsx(data, filename="telegram_data.xlsx"):
    df = pd.DataFrame.from_dict(data, orient="index")
    df.to_excel(filename, index=False)


# Fetch and save the data
message_data = fetch_message_details()
save_data_to_xlsx(message_data)

# Print the result
print(message_data)
