# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well the last blockchain value to the blockchain

    :param transaction_amount: the amount that should be added.
    :param last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_imput():
    """Returns the imput of the user (a new transaction amount) as a float"""
    user_input = float(input('Your transaction amount please: '))
    return user_input


tx_amount = get_user_imput()
add_value(tx_amount)


tx_amount = get_user_imput()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_imput()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)