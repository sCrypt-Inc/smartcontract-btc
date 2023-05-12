from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import PrivateKey, P2wshAddress, P2wpkhAddress
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup('mainnet')

    # TODO: Paste in private key
    priv0 = PrivateKey("")

    pub = priv0.get_public_key()
    fromAddress = pub.get_segwit_address()

    # TODO: Paste in redeem script:
    p2sh_redeem_script = Script.from_raw('0000018257615179547a75537a537a537a0079537a75527a527a7575615279008763537952795279615179517993517a75517a75619c77777777675279518763537952795279949c7777777767006868')

    toAddress = P2wshAddress.from_script(p2sh_redeem_script)

    # TODO: Set values
    txid = '516c4faef046d6895e77469fbde84626ccb3c4a131d39a8d53131917ac14e39d'
    vout = 0
    amount = 0.00332415
    fee = 0.00018070

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)
    redeem_script1 = Script(
        ['OP_DUP', 'OP_HASH160', priv0.get_public_key().to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG'])

    # create transaction output
    txOut = TxOutput(to_satoshis(amount - fee), toAddress.to_script_pub_key())

    # create transaction
    tx = Transaction([txin], [txOut], has_segwit=True)

    print("\nRaw transaction:\n" + tx.serialize())

    sig1 = priv0.sign_segwit_input(tx, 0, redeem_script1, to_satoshis(amount))
    tx.witnesses.append(Script([sig1, pub.to_hex()]))

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()