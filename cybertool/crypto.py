import base64
import hashlib
import urllib.parse

#========================
# Encode/Decode functions
#========================

#===== base64 =====
def base64_encode(text:str) -> str:
    return base64.b64encode(text.encode()).decode()

def base64_decode(text:str) -> str:
    return base64.b64decode(text.encode()).decode()

#===== url encoding =====
def url_encode(text:str)->str:
    return urllib.parse.quote(text)

def url_decode(text:str)->str:
    return urllib.parse.unquote(text)

#===== hex encoding =====
def hex_encode(text:str)->str:
    return text.encode().hex()

def hex_decode(text:str)->str:
    return bytes.fromhex(text).decode()


#===============
# Hash functions
#===============

def md5_hash(text:str)->str:
    return hashlib.md5(text.encode()).hexdigest()

def sha256_hash(text:str)->str:
    return hashlib.sha256(text.encode()).hexdigest()

