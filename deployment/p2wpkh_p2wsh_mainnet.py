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
    p2sh_redeem_script = Script.from_raw('000000201e3457f730d001d0fbe60830bded73df7166afd38ab3ac273e385003094371c0205657aa4c420a961153d539f4501457995fad8d27e17a5ec7ffda449e8b8aab1e20e60d1fb5e71b6327214e2e9503027c3ba44331562a8e1d193a1e759bcc27fc4161527952795279587a587a587a757575557a557a557a757575616155007600a26976539f6961946b6c766b796c75a853795379537953007600a26976539f6994618c6b6c766b796c756b7575756c87696155517600a26976539f6961946b6c766b796c75a853795379537953517600a26976539f6994618c6b6c766b796c756b7575756c87696155527600a26976539f6961946b6c766b796c75a853795379537953527600a26976539f6994618c6b6c766b796c756b7575756c876951777777777777')

    toAddress = P2wshAddress.from_script(p2sh_redeem_script)

    # TODO: Set values
    txid = 'a6d5e6f5f36c5587653df4841b1ec8e726018b15cadeeb542b2da780b38e9a21'
    vout = 0
    amount = 0.00296275
    fee = 0.00010000

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