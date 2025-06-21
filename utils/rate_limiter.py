import time

RATE_LIMIT_SECONDS = 10
user_last_seen = {}

def is_rate_limited(user_id: int) -> int:
    now = time.time()
    last_seen = user_last_seen.get(user_id, 0)
    if now - last_seen < RATE_LIMIT_SECONDS:
        return int(RATE_LIMIT_SECONDS - (now - last_seen))
    user_last_seen[user_id] = now
    return 0
