# Mining Software Installation Notes

**Date:** 2026-02-16
**Purpose:** Non-invasive benchmark installation for profitability analysis

## Installation Summary

Two miners installed to both AI nodes for comprehensive algorithm coverage:

### 1. lolMiner v1.98a
- **Location:** `~/crypto/miners/lolminer/`
- **Binary:** `~/crypto/miners/lolminer/lolMiner`
- **Source:** https://github.com/Lolliedieb/lolMiner-releases/releases/tag/1.98a
- **Type:** Open source, statically linked ELF64 (14MB)
- **Dev Fee:** 0.75-2.0% depending on algorithm

**Supported Target Algorithms:**
- ✅ Autolykos2 (Ergo) — 1.5% fee
- ✅ Flux/ZelHash — 1.5% fee
- ✅ Octopus (Conflux) — 2.0% fee
- ✅ Karlsenhash V2 (Kaspa-compatible) — 1.0% fee
- ✅ HeavyHash-Pyrin — 1.0% fee
- ❌ KawPow (Ravencoin) — NOT SUPPORTED

**Other Algorithms:**
- Ethash, Etchash (0.7% fee)
- FishHash (1.0% fee)
- NexaPoW (2.0% fee)
- BeamHash III (1.0% fee)
- Equihash 144/5, 192/7 (1.0% fee)
- Various Cuckatoo/Cuckaroo variants

**Usage Examples:**
```bash
# Ergo (Autolykos2)
./lolMiner --algo AUTOLYKOS2 --pool POOL_URL --user WALLET_ADDRESS

# Flux (ZelHash)
./lolMiner --algo FLUX --pool POOL_URL --user WALLET_ADDRESS

# Conflux (Octopus)
./lolMiner --algo OCTOPUS --pool POOL_URL --user WALLET_ADDRESS

# Pyrin (HeavyHash)
./lolMiner --algo PYRIN --pool POOL_URL --user WALLET_ADDRESS
```

### 2. T-Rex Miner v0.26.8
- **Location:** `~/crypto/miners/trex-miner/`
- **Binary:** `~/crypto/miners/trex-miner/t-rex`
- **Source:** https://github.com/trexminer/T-Rex/releases/tag/0.26.8
- **Type:** Closed source, dynamically linked ELF64 (45MB)
- **Dev Fee:** 1-2% depending on algorithm
- **License:** Proprietary (free for personal use)

**Supported Target Algorithms:**
- ✅ KawPow (Ravencoin) — 1% fee
- ✅ Autolykos2 (Ergo) — 2% fee
- ✅ Octopus (Conflux) — 2% fee
- ❌ Flux/ZelHash — NOT SUPPORTED in recent versions
- ❌ KHeavyHash (Kaspa) — NOT SUPPORTED

**Other Algorithms:**
- Ethash, Etchash
- FiroPow
- ProgPoW variants
- Many others

**Usage Example:**
```bash
# Ravencoin (KawPow)
./t-rex -a kawpow -o stratum+tcp://POOL_URL -u WALLET_ADDRESS -p x
```

## Algorithm Coverage Matrix

| Algorithm | Coin | lolMiner | T-Rex | Primary Miner |
|-----------|------|----------|-------|---------------|
| KawPow | Ravencoin | ❌ | ✅ | T-Rex |
| Autolykos2 | Ergo | ✅ | ✅ | lolMiner (lower fee) |
| Octopus | Conflux | ✅ | ✅ | lolMiner |
| Flux/ZelHash | Flux | ✅ | ❌ | lolMiner |
| KHeavyHash | Kaspa | ❌ | ❌ | NEED ALTERNATIVE |
| HeavyHash-Pyrin | Pyrin | ✅ | ❌ | lolMiner (similar) |

## Benchmark Strategy

**Approach:** Use miner best suited for each algorithm to get most realistic performance.

### Planned Benchmarks:

1. **KawPow (Ravencoin)** — T-Rex Miner
2. **Autolykos2 (Ergo)** — lolMiner
3. **Octopus (Conflux)** — lolMiner
4. **Flux (ZelHash)** — lolMiner
5. **Pyrin (HeavyHash)** — lolMiner (Kaspa proxy)

## Installation Commands (Reference)

### Dev-main download:
```bash
cd ~/crypto/profit-run

# lolMiner
wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.98a/lolMiner_v1.98a_Lin64.tar.gz
tar -xzf lolMiner_v1.98a_Lin64.tar.gz
mv 1.98a lolminer

# T-Rex
wget https://github.com/trexminer/T-Rex/releases/download/0.26.8/t-rex-0.26.8-linux.tar.gz
tar -xzf t-rex-0.26.8-linux.tar.gz
mkdir trex-miner && mv t-rex config_example README.md help trex-miner/
```

### Copy to AI nodes:
```bash
# To gpu-node-1
scp -r lolminer user@gpu-node-1:~/crypto/miners/
scp -r trex-miner user@gpu-node-1:~/crypto/miners/

# To gpu-node-2
scp -r lolminer user@gpu-node-2:~/crypto/miners/
scp -r trex-miner user@gpu-node-2:~/crypto/miners/
```

## Hardware Targets

- **gpu-node-1:** NVIDIA GeForce RTX 3060 (12GB)
- **gpu-node-2:** NVIDIA GeForce GTX 1660 SUPER (6GB)

## Safety Notes

- ✅ User-space installation only (no system daemons)
- ✅ No automatic startup configured
- ✅ No wallet private keys stored
- ✅ Placeholders used for wallet addresses in examples
- ⚠️ Close Ollama on gpu-node-1 before benchmarking
- ⚠️ Monitor GPU temperature (stop if >75°C sustained)
- ⚠️ Power limits applied before benchmarks

## Next Steps

1. Set GPU power limits (gpu-node-1: 120W, gpu-node-2: 80W)
2. Run 10-minute benchmarks per algorithm per GPU
3. Collect nvidia-smi metrics (power, temp, utilization)
4. Calculate profitability: (network revenue × hashrate) - (power cost)
5. Generate recommendation for 72-hour test

## Uninstall (if needed)

```bash
# On each AI node
rm -rf ~/crypto/miners/lolminer
rm -rf ~/crypto/miners/trex-miner
rm -rf ~/mining-test
```

---

**Status:** Installation complete, ready for benchmarking
**No daemons running** — miners will only run during explicit benchmark tests
