import json
import time
from pathlib import Path

import steamspypi
import steamreviews
import pandas as pd

def get_cooldown():
    cooldown = 62  # 1 minute plus a cushion

    return cooldown


def get_some_sleep():
    cooldown = get_cooldown()
    print("Sleeping for {} seconds on {}".format(cooldown, time.asctime()))

    time.sleep(cooldown)

    return


def download_a_single_page(page_no=1):
    print(f"Downloading page={page_no} on {time.asctime()}")

    data_request = dict()
    data_request["request"] = "all"
    data_request["page"] = str(page_no)

    data = steamspypi.download(data_request)

    return data

# def download_reviews(page_no=1):
#     print(f"Downloading reviews for page={page_no} on {time.asctime()}")
#
#     # For every page in folder
#     # For every game id in page
#     # Call steam_review_scraper.get_game_review(id=game_id)
#     # Store result in table
#     # Concatenate tables until end of page
#     # Output to csv and start over

def get_file_name(page_no=1):
    # Get current day as yyyymmdd format
    date_format = "%Y%m%d"
    current_date = time.strftime(date_format)
    
    file_name = "{}_steamspy_page_{}.json".format(current_date, page_no)
    
    return file_name


def download_all_pages(num_pages):
    # Download

    for page_no in range(1, num_pages):
        file_name = get_file_name(page_no)

        if not Path(file_name).is_file():
            page_data = download_a_single_page(page_no=page_no)

            with open(file_name, "w", encoding="utf8") as f:
                json.dump(page_data, f)

            if page_no != (num_pages):
                get_some_sleep()

    # Aggregate

    data = dict()

    for page_no in range(1, num_pages):
        file_name = get_file_name(page_no)

        with open(file_name, "r", encoding="utf8") as f:
            page_data = json.load(f)

            data.update(page_data)

    return data


if __name__ == "__main__":
    # TODO: one would have to figure out the number of pages, it should be close to 40 as of August 2020.
    data = download_all_pages(num_pages=64)