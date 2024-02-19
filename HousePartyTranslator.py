import os
import requests
import time
import json
import google.generativeai as genai
from pathlib import Path
from termcolor import colored, cprint
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from gpt import *
from filesHandler import *

# Load environment variables
load_dotenv(".env")

# Set environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Original language files location
source_folder = "./original"

# Translated language files location
translated_folder = "./translated"

# Define version
version = os.getenv('VERSION')
# Define Story
story = os.getenv('STORY')
# Define Language
language = os.getenv('LANGUAGE')

# UI
cprint(f"Starting translation of {story} (version {version}) to {language}", "white")

# Dialogs original folder
source_dialogs_folder = f"{source_folder}/{version}/{story}/"

# Parse dialog files in folder
for original_file in Path(source_dialogs_folder).glob("*.txt"):
  # UI
  cprint(f"[+] Reading file: {original_file.name}", "blue")
  # Read file
  source_file = open(Path(source_dialogs_folder, original_file.name), "r", encoding="utf-8-sig")
  source_file_contents = source_file.read()
  # Break file into parts
  parsed_dialogs = read_translate_file(source_file_contents)
  # Create json database
  json_db = create_json_file(parsed_dialogs, original_file.name.split('.')[0], language)
  # Based on json file, check how many dialogs is left to translate
  required_translation = []
  for item in json_db:
    if not item['translated_text']:
      required_translation.append(item)
  # UI
  cprint(f"[-->] Found {len(required_translation)} of {len(json_db)} dialogs to translate\n", "blue")

  # break