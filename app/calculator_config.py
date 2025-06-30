import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
    HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "data")
    LOG_FILE = os.getenv("CALCULATOR_LOG_FILE", "calculator.log")
    HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "history.csv")
    MAX_HISTORY = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", "4"))
    MAX_INPUT = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e6"))
    ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
