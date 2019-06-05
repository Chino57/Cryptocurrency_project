from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """ A transaction which can be added to a block in a blockchain
    Attributes:
        :sender: the sender of the coins.
        :recipient: the recipient of the coins.
        :signature: the signature of the transaction
        :amount: the amount of the coins sent

    """
    def __init__(self,sender,recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def __repr__(self):
        return str(self.__dict__)

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
