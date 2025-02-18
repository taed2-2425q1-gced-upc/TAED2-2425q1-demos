import logging
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

root = os.getenv("ROOT")
if root is None:
    raise ValueError(
        "ROOT environment variable is not set in .env file. Use dot-env-template file to create .env file."
    )

PROJ_ROOT = Path(root)

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

METRICS_DIR = PROJ_ROOT / "metrics"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

TEST_DIR = PROJ_ROOT / "tests"
TEST_DATA_DIR = TEST_DIR / "data"

logging.basicConfig(level=logging.INFO)
