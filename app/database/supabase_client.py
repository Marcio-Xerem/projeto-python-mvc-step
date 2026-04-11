
# app/database/supabase_client.py

from supabase import create_client

SUPABASE_URL = ''
SUPABASE_KEY = ''

supabase = {
    "url": SUPABASE_URL,
    "key": SUPABASE_KEY
}

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
