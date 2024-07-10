import json
import time
from pathlib import Path
import os
import steamspypi
import steamreviews
import pandas as pd
import requests

def download_reviews(page_no=1):
    print(f"Downloading reviews for page={page_no} on {time.asctime()}")
    with open(f'20240706_steamspy_page_{page_no}.json') as f:
        page = json.load(f)
    app_ids = page.keys()
    for appid in page.keys():
        request_params = dict()
        request_params['filter'] = 'recent'
        request_params['day_range'] = '28'
        reviews = steamreviews.download_reviews_for_app_id(appid, chosen_request_params=request_params)


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