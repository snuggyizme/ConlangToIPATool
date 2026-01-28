from pathlib import Path
import json

from config import tools as configTools

dataFile = Path.home() / "snuggyizme" / ".ipatlanguages.json"

def loadData():
    if not dataFile.exists():
        dataFile.parent.mkdir(parents=True, exist_ok=True)
        defaultData = {
            "English": configTools.defaultCompiled
        }
        saveData(defaultData)
        return defaultData
    with open(dataFile, "r", encoding="utf-8") as f:
        return json.load(f)

def saveData(data: dict):
    with open(dataFile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
langs = loadData()
print(langs)