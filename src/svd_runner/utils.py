import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_cache_dir():
    cache_dir = os.getenv("CACHE_DIR", "D:/svd runner/cache")
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    return cache_dir

def log(message: str):
    print(f"[svd_runner] {message}")
