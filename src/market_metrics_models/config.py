import os
from pathlib import Path
from dotenv import load_dotenv
from market_metrics_models.utils.global_enums import ConfigEnums

BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path)


def get_db_param(param_type: ConfigEnums) -> str:
  """
  Function to get a database parameter.
  :param param_type: Indicator for the parameter type.
  :return: The parameter type.
  """
  if param_type is ConfigEnums.DB_URL:
    return os.getenv("DATABASE_URL", "sqlite:///./dev.db")
  return ""

def get_path(param_type: ConfigEnums) -> Path:
  """
  Function to get a file or directory path.
  :param param_type: Indicator for the parameter type.
  :return: A file or directory path.
  """
  if param_type is ConfigEnums.RAW_DATA_DIR:
    return Path(os.getenv("RAW_DATA_DIR_PATH"))
  return BASE_DIR
