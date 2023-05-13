import {
    assert,
    FixedArray,
    ByteString,
    method,
    prop,
    Sha256,
    SmartContract,
    sha256,
} from 'scrypt-ts'
import { generateRandomHex } from '../util'

export type HashArray = FixedArray<Sha256, typeof MultiPartyHashPuzzle.N>
export type PreimageArray = FixedArray<
    ByteString,
    typeof MultiPartyHashPuzzle.N
>

export class MultiPartyHashPuzzle extends SmartContract {
    static readonly N = 3

    @prop()
    readonly hashes: HashArray

    constructor(hashes: HashArray) {
        super(...arguments)
        this.hashes = hashes
    }

    @method()
    public unlock(preimages: PreimageArray) {
        for (let i = 0; i < MultiPartyHashPuzzle.N; i++) {
            assert(sha256(preimages[i]) == this.hashes[i], 'hash mismatch')
        }
        assert(true)
    }
}

(async () => {
    const _preimages = []
    const _hashes = []
    for (let i = 0; i < MultiPartyHashPuzzle.N; i++) {
        const preimage = generateRandomHex(32)
        _preimages.push(preimage)
        _hashes.push(sha256(preimage))
    }
    const preimages = _preimages as FixedArray<
        ByteString,
        typeof MultiPartyHashPuzzle.N
    >
    const hashes = _hashes as FixedArray<Sha256, typeof MultiPartyHashPuzzle.N>

    await MultiPartyHashPuzzle.compile()
    const instance = new MultiPartyHashPuzzle(hashes)

    console.log('Hash preimages:')
    console.log(preimages)
    console.log('Redeem script:')
    console.log(instance.lockingScript.toHex().replaceAll('5195', '61'))
})()
