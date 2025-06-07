# config/paths.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGIN_DATA_FILE = BASE_DIR / "testData" / "LoginData.xlsx"
