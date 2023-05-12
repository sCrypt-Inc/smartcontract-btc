Read [article]() for more details.

## Requirements:

Run:

```sh
npm i && pip3 install bitcoin-utils
```

## Deployment:

Produce redeem script:

```sh
npx ts-node src/contracts/demo.ts
```

Next, adjust values (marked with "TODO") in deployment scripts under `deployment/`. After that you can construct the serialized transactions which may be broadcast.

This will construct that pays the redeem script using a P2WSH output:

```sh
python3 deployment/p2wpkh_p2wsh_mainnet.py
```

And this will construct a transaction to spend it:

```sh
python3 deployment/p2wsh_p2wpkh_mainnet.py
```
