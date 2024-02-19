import os
import json
import re
from termcolor import colored, cprint

def read_translate_file(contents):
  """
  Lê um arquivo txt com diálogos e retorna um array multidimensional.

  Args:
    nome_arquivo (str): O nome do arquivo txt a ser lido.

  Returns:
    list: Um array multidimensional com a seguinte hierarquia:
      [Grupo] => [ID do diálogo]: Diálogo
  """
  # Init vars
  dialogs = {}
  current_group = None

  # Get content splited by rows
  rows = contents.split("\n")

  # Parse rows
  for row in rows:
    # Remove empty characters form start and end of string
    row = row.strip()
    
    try:
      # If is a group title
      # if row.startswith("[") and row.endswith("]"):
      if re.match(r"^\[.*\]$", row):
        # Start a new group
        current_group = row[1:-1]
        dialogs[current_group] = {}
      
      # If is a dialog line
      elif "|" in row:
        # New dialog line
        id_dialog, dialog = row.split("|")
        dialogs[current_group][id_dialog] = dialog
      
      # If is a empty line
      elif row == "":
        continue

      # Is a continuation of last dialog
      else:
        # Continuação do diálogo anterior
        dialogs[current_group][id_dialog] += f"\n{row}"

    except Exception as e:
      # UI
      cprint(f"Error when parsing row:\n{row}\nError: {e}", "red")
      cprint(f"Tests: {re.match(r"^\[.*\]$", row.strip())} | {row[0] == "[" and row[-1] == "]"} | {row.startswith("[") and row.endswith("]")}", "red")

  return dialogs


def create_json_file(data, file_name, language):
  # File buffer
  json_content = []

  # Get env data
  version = os.getenv('VERSION')
  story = os.getenv('STORY')

  # File location
  file_path = f"./temp/{version}/{story}/{file_name}.json"

  # Create folders if not exists
  create_folders_if_not_exists(file_path)

  # UI
  cprint(f"[i] Handling JSON local database in {file_path}", "blue")

  # Parse data
  for group, dialogs in data.items():
    for id_dialog, dialog in dialogs.items():
      json_content.append({
        "id": id_dialog,
        "original_text": dialog,
        "translated_text": "",
        "language": language,
        "group": group
      })
  
  # Try create file
  try:
    # If file doesn't exists create
    if not os.path.exists(file_path):
      with open(file_path, "w") as json_file:
        json.dump(json_content, json_file, indent=2)
        # UI
        cprint(f"[i] Creating database file for {file_name}...", "blue")
    
    # Read the file and update content to return
    json_file_read = open(file_path, "r", encoding="utf-8")
    # UI
    cprint(f"[i] Reading JSON file", "blue")
    # Read it contents
    json_file_contents = json_file_read.read()
    # Convert into JSON
    json_parsed = json.loads(json_file_contents)

  except Exception as e:
    cprint(f"Error when creating json file: {e}", "red")

  return json_parsed


def create_folders_if_not_exists(path):
  # Separar o nome do arquivo do caminho
  directory, file_name = os.path.split(path)

  # Criar as pastas caso não existam
  try:
    cprint(f"[i] Creating folder {directory}...", "blue")
    os.makedirs(directory, exist_ok=True)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise