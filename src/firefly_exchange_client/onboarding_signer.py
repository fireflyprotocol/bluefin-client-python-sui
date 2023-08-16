from web3 import Web3
from .interfaces import *
from .signer import Signer
import hashlib

class OnboardingSigner(Signer):
    def __init__(self):
        super().__init__()

    def create_signature(self, msg, private_key, encoding="utf-8"):
        """
            Signs the message.
            Inputs:
                - msg: the message to be signed
                - private_key: the signer's private key
            Returns:
                - str: signed msg hash
        """
        hash=hashlib.sha256(msg.encode(encoding=encoding))
        return self.sign_hash(hash.digest(), private_key)

