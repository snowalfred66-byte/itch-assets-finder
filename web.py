import requests
from bs4 import BeautifulSoup
import json
import os

def loop_through_assets(assets):
  while True:
    search = input("search for assets (or type quit): ")
    found = 0
    if search.lower() == "quit":
      return

    for asse in assets:
      if search.lower() in asse["description"].lower() or search.lower() in asse["title"].lower():
        found += 1
        print("=" * 30)
        print(f"Title: {asse['title']}")
        print(f"Author: {asse['author']}")
        print(f"Description: {asse['description']}")
        print(f"Link: {asse['link']}")
        print(f"Image : {asse['img']}")
        print("=" * 30, "\n")
    if found <= 0:
      print("no results were found", "\n")

    print(f"Items found: {found}")

def load_from_json():
  if os.path.exists("assets.json"):
    with open("assets.json", "r")as file:
      assets = json.load(file)
      print(f"assets loaded: {len(assets)} ")
      return assets
  else:
    print("No assets found")
    print("Save file is empty")
    return []

def search_online(assets):

  for page in range(1,100):
    main_url = f"https://itch.io/game-assets/free/tag-3d?page={page}"
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")
    finder = soup.find_all("div", class_="game_cell")

    for find in finder:
      the_links_tag = find.find("a")
      the_links = the_links_tag.get("href") if the_links_tag else "no link found"

      the_img_tag = find.find("img")
      the_img_links = the_img_tag.get("data-lazy_src") if the_img_tag else "no image found"

      the_athour = find.find("div", class_="game_author").text.strip()
      the_title = find.find("div", class_="game_title").text.strip()
      the_description = find.find("div", class_="game_text")

      asset = {"title" : the_title,"author" : the_athour,"img" : the_img_links,"link" : the_links, "description" : the_description.text.strip() if the_description else "no description"}
      assets.append(asset)

  save_assets(assets)
  print(f"Total assets found ", len(assets))
  loop_through_assets(assets)

def save_assets(assets):
  with open("assets.json", "w") as file:
    print("saving...")
    json.dump(assets, file, indent=4)

def choise_():
  while True:
    print("*" * 25)
    print("1. Load saved assets")
    print("2. Scrap assets")
    print("3. exit")
    print("*" * 25)
    choise = input("enter yor choise:")
    if choise == "1":
      print("loading assets...")
      assets = load_from_json()
      loop_through_assets(assets)

    elif choise == "3":
      print("exiting...")
      break

    elif choise == "2":
      print("please wait...")
      assets = []
      search_online(assets)
    else:
      print("haha so... funny")
      print("invalid choise")

choise_()