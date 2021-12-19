from hashlib import sha256
from binascii import b2a_hex
from pycoin.symbols.btc import network as BTC
from . import segwit_addr

# TODO (tylerchambers): Remove the Pycoin dependency.
def addr_to_hash(addr_str: str) -> str:
    addr = BTC.parse(addr_str)
    if addr is None:
        try:  # try taproot
            witver, witprog = segwit_addr.decode("bc", addr_str)
            print(witver, witprog)
            sh = sha256(
                bytes([witver + 0x50 if witver else 0, len(witprog)] + witprog)
            ).digest()[::-1]
            return str(b2a_hex(sh), "ascii")
        except ValueError:
            raise ValueError("Invalid address")
    sh = sha256(addr.script()).digest()[::-1]
    return str(b2a_hex(sh), "ascii")
