import json
import time
from pathlib import Path

import steamspypi
import steamreviews
import pandas as pd
def download_reviews(page_no=1):
    print(f"Downloading reviews for page={page_no} on {time.asctime()}")

    # For every page in folder
    # For every game id in page
    # Call steam_review_scraper.get_game_review(id=game_id)
    # Store result in table
    # Concatenate tables until end of page
    # Output to csv and start over