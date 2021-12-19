from electrum_client import util


def test_P2PKHToHash():
    out = util.addr_to_hash("15e15hWo6CShMgbAfo8c2Ykj4C6BLq6Not")
    assert out == "9bf772598922e7ad83ea5a5d3d0d727329d12db4350c0620f35bb3c72a31ea8a"


def test_P2WPKHtoHash():
    out = util.addr_to_hash("bc1q42lja79elem0anu8q8s3h2n687re9jax556pcc")
    assert out == "b33565c601313f9307862bae35cbe14cc7f06d54cfb9724b63a7087fa852f972"


def test_P2SHToHash():
    out = util.addr_to_hash("35PBEaofpUeH8VnnNSorM1QZsadrZoQp4N")
    assert out == "c2d8bc011ee75821cf9751be13c7002069cb17a55ffa956a7440fa8e5e93d504"


def test_P2WPKHToHash():
    out = util.addr_to_hash("bc1q42lja79elem0anu8q8s3h2n687re9jax556pcc")
    assert out == "b33565c601313f9307862bae35cbe14cc7f06d54cfb9724b63a7087fa852f972"


def test_P2TR():
    out = util.addr_to_hash(
        "bc1p5d7rjq7g6rdk2yhzks9smlaqtedr4dekq08ge8ztwac72sfr9rusxg3297")
    assert out == "b0fbaa5866e707148231ebf5af1a1b8a62507c0566a5ff4ca63d893f3f5c953c"
