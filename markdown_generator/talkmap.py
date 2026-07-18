# Leaflet cluster map of talk locations
#
# Run from the repo root or this directory. Scrapes the location YAML field from
# each talk in _talks/, geolocates it with geopy/Nominatim, and uses getorg to
# write HTML/JS into the repo-root talkmap/ folder.
# This is functionally the same as talkmap.ipynb.
from pathlib import Path

import frontmatter
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

ROOT = Path(__file__).resolve().parent.parent
TALKS_DIR = ROOT / "_talks"
OUTPUT_DIR = ROOT / "talkmap"

# Collect the Markdown files
g = sorted(TALKS_DIR.glob("*.md"))

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location and report the status
    try:
        location_dict[description] = geocoder.geocode(location, timeout=TIMEOUT)
        print(description, location_dict[description])
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {location} with message {ex}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(
    location_dict, folder_name=str(OUTPUT_DIR), hashed_usernames=False
)
