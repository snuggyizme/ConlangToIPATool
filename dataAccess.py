from pathlib import Path
import json

from config import tools as configTools
import main

langdataFile = Path.home() / "snuggyizme" / ".ipatlanguages.json"
appdataFile = Path.home() / "snuggyizme" / ".ipatappdata.json"

def loadData(file="langs") -> dict:
    if not langdataFile.parent.exists():
        langdataFile.parent.mkdir(parents=True, exist_ok=True)

    if not langdataFile.exists():
        defaultData = {
            "English": configTools.defaultCompiled
        }
        saveData(defaultData)
        langData = defaultData
    else:
        with open(langdataFile, "r", encoding="utf-8") as f:
            langData = json.load(f)

    if not appdataFile.exists():
        defaultAppData = {"version": main.VERSION}
        saveData(defaultAppData, file="appdata")

    with open(appdataFile, "r", encoding="utf-8") as f:
        appData = json.load(f)

    if file == "langs":
        return langData
    elif file == "appdata":
        return appData

def saveData(data: dict, file="langs"):
    if file == "langs":
        with open(langdataFile, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    elif file == "appdata":
        with open(appdataFile, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
langs = loadData()
print(langs)