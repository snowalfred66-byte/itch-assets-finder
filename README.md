 Itch.io Assets Finder

A small Python web scraping tool I built to find free 3D game assets from itch.io.

 Features

- Scrapes free 3D assets from itch.io
- Gets the asset title
- Gets the author
- Gets the description
- Gets the asset link
- Gets the image link
- Saves the results to a JSON file
- Loads previously saved assets
- Searches through the collected assets

 Built With

- Python
- Requests
- BeautifulSoup
- JSON

 How It Works

The program requests pages from itch.io and uses BeautifulSoup to
extract information about the available assets.

The collected information is saved in `assets.json`, which can
later be loaded and searched.

 How To Run

Install the required Python libraries:

```bash
pip install requests beautifulsoup4
