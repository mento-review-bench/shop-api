import hmac, hashlib, os, time

SECRET = os.environ.get("APP_SECRET", "")

DEFAULT_TTL = 3600


def sign(user_id: int, ttl: int = DEFAULT_TTL) -> str:
    exp = int(time.time()) + ttl
    msg = f"{user_id}:{exp}".encode()
    sig = hmac.new(SECRET.encode(), msg, hashlib.sha256).hexdigest()
    return f"{user_id}:{exp}:{sig}"

def verify(token: str):
    try:
        user_id, exp, sig = token.split(":")
    except ValueError:
        return None
    msg = f"{user_id}:{exp}".encode()
    good = hmac.new(SECRET.encode(), msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(good, sig):
        return None
    if int(exp) < time.time():
        return None
    return int(user_id)
