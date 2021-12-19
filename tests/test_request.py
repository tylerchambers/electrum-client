from electrum_client import requests

def test_Request():
    r = requests.Request("test", [1, 2, 3])
    assert r.method == "test"
    assert r.params == [1, 2, 3]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "test", "params": [1, 2, 3], "id": 4}'

def test_BlockHeaderRequest():
    r = requests.BlockHeaderRequest(1)
    assert r.method == "blockchain.block.header"
    assert r.params == [1]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.block.header", "params": [1], "id": 4}'

def test_BlockHeadersRequest():
    r = requests.BlockHeadersRequest(1, 2)
    assert r.method == "blockchain.block.headers"
    assert r.params == [1, 2]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.block.headers", "params": [1, 2], "id": 4}'

def test_FeeEstimateRequest():
    r = requests.FeeEstimateRequest(1)
    assert r.method == "blockchain.estimatefee"
    assert r.params == [1]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.estimatefee", "params": [1], "id": 4}'

def test_HeadersSubscribeRequest():
    r = requests.HeadersSubscribeRequest()
    assert r.method == "blockchain.headers.subscribe"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.headers.subscribe", "params": [], "id": 4}'

def test_RelayFeeRequest():
    r = requests.RelayFeeRequest()
    assert r.method == "blockchain.relayfee"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.relayfee", "params": [], "id": 4}'

def test_GetScriptHashBalanceRequest():
    r = requests.GetScriptHashBalanceRequest("a")
    assert r.method == "blockchain.scripthash.get_balance"
    assert r.params == ["a"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.scripthash.get_balance", "params": ["a"], "id": 4}'

def test_GetScriptHashHistoryRequest():
    r = requests.GetScriptHashHistoryRequest("a")
    assert r.method == "blockchain.scripthash.get_history"
    assert r.params == ["a"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.scripthash.get_history", "params": ["a"], "id": 4}'

def test_ListUnspentRequest():
    r = requests.ListUnspentRequest("a")
    assert r.method == "blockchain.scripthash.listunspent"
    assert r.params == ["a"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.scripthash.listunspent", "params": ["a"], "id": 4}'

def test_ScrptHashSubscriptionRequest():
    r = requests.ScriptHashSubscriptionRequest("a")
    assert r.method == "blockchain.scripthash.subscribe"
    assert r.params == ["a"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.scripthash.subscribe", "params": ["a"], "id": 4}'

def test_TransactionBroadcastRequest():
    r = requests.TransactionBroadcastRequest("a")
    assert r.method == "blockchain.transaction.broadcast"
    assert r.params == ["a"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.transaction.broadcast", "params": ["a"], "id": 4}'

def test_TransactionGetRequest():
    r = requests.TransactionGetRequest("a", True)
    assert r.method == "blockchain.transaction.get"
    assert r.params == ["a", True]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.transaction.get", "params": ["a", true], "id": 4}'

def test_TransactionMerkleRequest():
    r = requests.TransactionMerkleRequest("a", 4)
    assert r.method == "blockchain.transaction.get_merkle"
    assert r.params == ["a", 4]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "blockchain.transaction.get_merkle", "params": ["a", 4], "id": 4}'

def test_MempoolFeeHistogramRequest():
    r = requests.MempoolFeeHistogramRequest()
    assert r.method == "mempool.get_fee_histogram"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "mempool.get_fee_histogram", "params": [], "id": 4}'

def test_ServerBannerRequest():
    r = requests.ServerBannerRequest()
    assert r.method == "server.banner"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.banner", "params": [], "id": 4}'

def test_ServerDonationAddressRequest():
    r = requests.ServerDonationAddressRequest()
    assert r.method == "server.donation_address"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.donation_address", "params": [], "id": 4}'

def test_ServerFeaturesRequest():
    r = requests.ServerFeaturesRequest()
    assert r.method == "server.features"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.features", "params": [], "id": 4}'

def test_ServerPeersRequest():
    r = requests.ServerPeersRequest()
    assert r.method == "server.peers.subscribe"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.peers.subscribe", "params": [], "id": 4}'

def test_ServerPingRequest():
    r = requests.ServerPingRequest()
    assert r.method == "server.ping"
    assert r.params == []
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.ping", "params": [], "id": 4}'

def test_ServerVersionRequest():
    r = requests.ServerVersionRequest("test", "test")
    assert r.method == "server.version"
    assert r.params == ["test", "test"]
    r.set_id(4)
    assert r.id == 4
    assert r.to_json() == '{"method": "server.version", "params": ["test", "test"], "id": 4}'