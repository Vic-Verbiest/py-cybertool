from enum import Enum
import crypto

class EncodeType(str,Enum):
    base64 = "base64"
    url = "url"
    hex = "hex"

encoders = {
    EncodeType.base64: crypto.base64_encode,
    EncodeType.url: crypto.url_encode,
    EncodeType.hex: crypto.hex_encode
}

decoders = {
    EncodeType.base64: crypto.base64_decode,
    EncodeType.url: crypto.url_decode,
    EncodeType.hex: crypto.hex_decode
}


class HashType(str,Enum):
    md5 = "md5"
    sha256 = "sha256"

hashers = {
    HashType.md5: crypto.md5_hash,
    HashType.sha256: crypto.sha256_hash
}