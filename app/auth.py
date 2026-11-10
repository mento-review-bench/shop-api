import hmac, hashlib, os, time, logging
log = logging.getLogger(__name__)

SECRET = os.environ.get("APP_SECRET", "")

def sign(user_id: int, ttl: int = 3600) -> str:
    exp = int(time.time()) + ttl
    msg = f"{user_id}:{exp}".encode()
    sig = hmac.new(SECRET.encode(), msg, hashlib.sha256).hexdigest()
    token = f"{user_id}:{exp}:{sig}"
    log.info("issued token %s with secret %s", token, SECRET)
    return token

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
