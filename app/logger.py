import logging, os
from .calculator_config import Config

os.makedirs(Config.LOG_DIR, exist_ok=True)
log_path = os.path.join(Config.LOG_DIR, Config.LOG_FILE)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding=Config.ENCODING
)
logger = logging.getLogger(__name__)
