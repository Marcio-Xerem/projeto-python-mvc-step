# app/database/supabase_client.py

import os
import requests

def _load_env_file():
    """Carrega variaveis do .env sem depender de bibliotecas externas."""
    env_path = ".env"
    if not os.path.exists(env_path):
        return

    with open(env_path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


_load_env_file()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = {
    "url": SUPABASE_URL,
    "key": SUPABASE_KEY
}

# ou se quiser criar um helper para requests
def supabase_request(path, method="GET", data=None):
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("SUPABASE_URL e SUPABASE_KEY devem estar definidas no arquivo .env")

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    normalized_path = path.lstrip("/")
    url = f"{SUPABASE_URL}/rest/v1/{normalized_path}"
    if method.upper() == "GET":
        return requests.get(url, headers=headers)
    elif method.upper() == "POST":
        return requests.post(url, json=data, headers=headers)
            
