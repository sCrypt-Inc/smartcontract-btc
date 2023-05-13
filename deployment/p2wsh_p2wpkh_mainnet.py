from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import PrivateKey, P2wshAddress, P2wpkhAddress
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup('mainnet')

    # TODO: Paste in redeem script:
    p2wsh_witness_script = Script.from_raw('000000201e3457f730d001d0fbe60830bded73df7166afd38ab3ac273e385003094371c0205657aa4c420a961153d539f4501457995fad8d27e17a5ec7ffda449e8b8aab1e20e60d1fb5e71b6327214e2e9503027c3ba44331562a8e1d193a1e759bcc27fc4161527952795279587a587a587a757575557a557a557a757575616155007600a26976539f6961946b6c766b796c75a853795379537953007600a26976539f6994618c6b6c766b796c756b7575756c87696155517600a26976539f6961946b6c766b796c75a853795379537953517600a26976539f6994618c6b6c766b796c756b7575756c87696155527600a26976539f6961946b6c766b796c75a853795379537953527600a26976539f6994618c6b6c766b796c756b7575756c876951777777777777')


    fromAddress = P2wshAddress.from_script(p2wsh_witness_script)

    # TODO: Set values
    toAddress = P2wpkhAddress.from_address("bc1q99dsng0pq93r6t97llcdy3s7xz96qer03f55wz")
    txid = 'f7b0d5c2a1b70a3ce13afe06f867a9f3c60fd73c9756bb4f37a343e9a8f9d4c1'
    vout = 0
    amount = 0.00286275
    fee = 0.00010000

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)

    txOut1 = TxOutput(to_satoshis(amount - fee), toAddress.to_script_pub_key())

    tx = Transaction([txin], [txOut1], has_segwit=True)

    # TODO: Paste in correct hash preimages.
    tx.witnesses.append(Script([
        'abc57d70dc5e56ac73e2970077adaf94accfb36dac2b40d34f807cdedad0807b',
        'fe4f237f4e51053fa4cebc55ee15ffd9dd654c2e3b928d4a6243d1f1bcb57ca7',
        '5776ddb41c760c1965401fc4521531c3db68cf1023ce5a294a201ccfc887bc85',
        p2wsh_witness_script.to_hex()]))
    
    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()