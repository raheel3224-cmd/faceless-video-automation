import os
from dotenv import load_dotenv
load_dotenv()
def get_env(name: str, default=None):
    val = os.getenv(name, default)
    if val is None:
        raise RuntimeError(f"Missing env var: {name}")
    return val
