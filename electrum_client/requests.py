import json


class Request:
    jsonrpc = "2.0"

    def __init__(self, method: str, params: list):
        self.method = method
        self.params = params

    def set_id(self, id: int):
        self.id = id

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


class BlockHeaderRequest(Request):
    def __init__(self, height: int) -> None:
        super().__init__("blockchain.block.header", [height])


class BlockHeadersRequest(Request):
    def __init__(self, start_height: int, count: int) -> None:
        super().__init__("blockchain.block.headers", [start_height, count])


class FeeEstimateRequest(Request):
    def __init__(self, nblocks: int) -> None:
        super().__init__("blockchain.estimatefee", [nblocks])


class HeadersSubscribeRequest(Request):
    def __init__(self):
        super().__init__("blockchain.headers.subscribe", [])


class RelayFeeRequest(Request):
    def __init__(self):
        super().__init__("blockchain.relayfee", [])


class GetScriptHashBalanceRequest(Request):
    def __init__(self, script_hash: str) -> None:
        super().__init__("blockchain.scripthash.get_balance", [script_hash])


class GetScriptHashHistoryRequest(Request):
    def __init__(self, script_hash: str) -> None:
        super().__init__("blockchain.scripthash.get_history", [script_hash])


class ListUnspentRequest(Request):
    def __init__(self, script_hash: str) -> None:
        super().__init__("blockchain.scripthash.listunspent", [script_hash])


class ScriptHashSubscriptionRequest(Request):
    def __init__(self, script_hash: str):
        super().__init__("blockchain.scripthash.subscribe", [script_hash])


class TransactionBroadcastRequest(Request):
    def __init__(self, tx_hex: str) -> None:
        super().__init__("blockchain.transaction.broadcast", [tx_hex])


class TransactionGetRequest(Request):
    def __init__(self, txid: str, verbose: bool) -> None:
        super().__init__("blockchain.transaction.get", [txid, verbose])


class TransactionMerkleRequest(Request):
    def __init__(self, txid: str, height: int) -> None:
        super().__init__("blockchain.transaction.get_merkle", [txid, height])


class MempoolFeeHistogramRequest(Request):
    def __init__(self) -> None:
        super().__init__("mempool.get_fee_histogram", [])


class ServerBannerRequest(Request):
    def __init__(self) -> None:
        super().__init__("server.banner", [])


class ServerDonationAddressRequest(Request):
    def __init__(self) -> None:
        super().__init__("server.donation_address", [])


class ServerFeaturesRequest(Request):
    def __init__(self) -> None:
        super().__init__("server.features", [])


class ServerPeersRequest(Request):
    def __init__(self) -> None:
        super().__init__("server.peers.subscribe", [])


class ServerPingRequest(Request):
    def __init__(self) -> None:
        super().__init__("server.ping", [])


class ServerVersionRequest(Request):
    def __init__(self, client_id: str, client_version: str) -> None:
        super().__init__("server.version", [client_id, client_version])
