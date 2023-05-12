from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import PrivateKey, P2wshAddress, P2wpkhAddress
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup('mainnet')

    # TODO: Paste in redeem script:
    p2wsh_witness_script = Script.from_raw('0000018257615179547a75537a537a537a0079537a75527a527a7575615279008763537952795279615179517993517a75517a75619c77777777675279518763537952795279949c7777777767006868')

    fromAddress = P2wshAddress.from_script(p2wsh_witness_script)

    # TODO: Set values
    toAddress = P2wpkhAddress.from_address("bc1q99dsng0pq93r6t97llcdy3s7xz96qer03f55wz")
    txid = '353551efaf4ab11d2eb90ec07e2a8a7979a0cab770b88adf3ea5a2be39491b34'
    vout = 0
    amount = 0.00314345
    fee = 0.00018070

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)

    txOut1 = TxOutput(to_satoshis(amount - fee), toAddress.to_script_pub_key())

    tx = Transaction([txin], [txOut1], has_segwit=True)

    tx.witnesses.append(Script(['05', '', p2wsh_witness_script.to_hex()]))
    
    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()