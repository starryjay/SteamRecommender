import json
import time
from pathlib import Path

import steamspypi
import steamreviews
import pandas as pd

def download_reviews(page_no=1):
    print(f"Downloading reviews for page={page_no} on {time.asctime()}")
    with open(f'20240706_steamspy_page_{page_no}.json') as f:
        page = json.load(f)
    app_ids = page.keys()
    reviews = steamreviews.download_reviews_for_app_id_batch(app_ids)
    return type(reviews)

if __name__ == '__main__':
    for pagenum in range(64):
        download_reviews(pagenum)
    

    # For every page in folder
    # Get all game ids
    # Call steamreviews.download_reviews_for_app_id_batch(app_ids)
    # Store result in table
    # Concatenate tables until end of page
    # Output to csv and start over