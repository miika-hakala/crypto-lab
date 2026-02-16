# Ergo Wallet Creation Guide — crypto-lab

**Purpose:** Safely create a self-custody Ergo (ERG) wallet for mining payouts.

**Date:** 2026-02-16
**Status:** Required before EXP-001 (72h Ergo mining test)

---

## ⚠️ ABSOLUTE RULES — READ FIRST

### NEVER Do This:
- ❌ **NEVER** store seed phrase on mining nodes (gpu-node-1, gpu-node-2, control-node)
- ❌ **NEVER** screenshot seed phrase (screenshots can leak)
- ❌ **NEVER** save seed phrase to clipboard managers or cloud services
- ❌ **NEVER** share seed phrase over chat, email, or any digital channel
- ❌ **NEVER** enter seed phrase into websites asking for "wallet recovery"
- ❌ **NEVER** commit seed phrase to git or any version control

### ALWAYS Do This:
- ✅ **ALWAYS** write seed phrase on paper immediately
- ✅ **ALWAYS** verify seed phrase by restoring wallet (test recovery)
- ✅ **ALWAYS** store paper backup in secure physical location
- ✅ **ALWAYS** use strong spending password (if wallet supports it)
- ✅ **ALWAYS** double-check receive address before mining
- ✅ **ONLY** share public receive address (not private keys)

---

## Recommended Wallets for Ergo

### Primary Option: Nautilus Wallet (Browser Extension)

**Platform:** Chrome, Firefox, Edge
**Type:** Self-custody, non-custodial
**Seed:** 15-word mnemonic (BIP39)
**URL:** https://github.com/nautls/nautilus-wallet

**Pros:**
- ✅ Official Ergo wallet
- ✅ Easy to use
- ✅ Active development
- ✅ Supports mining payouts

**Cons:**
- ⚠️ Browser-based (less secure than hardware wallet)

### Alternative: Ergo Mobile Wallet

**Platform:** iOS, Android
**Type:** Self-custody, non-custodial
**Seed:** 15-word mnemonic
**URL:** https://ergoplatform.org/en/mobile-wallets/

**Pros:**
- ✅ Mobile convenience
- ✅ Official wallet
- ✅ Good security

**Cons:**
- ⚠️ Requires mobile device

---

## ❌ NOT Ergo Wallets

**Important:** The following wallets do **NOT** support Ergo:
- ❌ **Yoroi** — This is a Cardano wallet, NOT Ergo
- ❌ **Daedalus** — Cardano only
- ❌ **MetaMask** — Ethereum/EVM chains only

---

## Wallet Creation Checklist

### Step 1: Install Wallet

**For Nautilus (Browser Extension):**
```
1. Go to Chrome Web Store or Firefox Add-ons
2. Search "Nautilus Wallet"
3. Verify publisher: nautls
4. Click "Add to Browser"
5. Pin extension to toolbar
```

**Security Check:**
- [ ] Verified official source (GitHub or official store)
- [ ] Checked developer/publisher name
- [ ] Read recent reviews for red flags

---

### Step 2: Create New Wallet

**DO NOT** import an existing wallet unless you already have one.

1. Open Nautilus extension
2. Click "Create New Wallet"
3. Choose strong spending password (12+ characters)
4. **CRITICAL:** Wallet will display 15-word seed phrase

---

### Step 3: Write Seed Phrase Offline

**This is the MOST IMPORTANT step.**

1. **Get paper and pen** (not digital)
2. **Write down all 15 words** in exact order
3. **Number each word** (1-15)
4. **Verify spelling** (reread each word)
5. **DO NOT** take photo or screenshot

**Example Format (DO NOT use these words):**
```
1. example
2. words
3. here
4. never
5. use
... (15 total)
```

**Storage:**
- Store paper in secure location (safe, lockbox, secure drawer)
- Consider making 2 copies, stored in different locations
- Never store with computer or phone
- Tell trusted person where backup is (optional)

---

### Step 4: Test Seed Phrase Recovery

**CRITICAL:** Verify you wrote seed correctly.

1. Close wallet completely
2. Reopen wallet
3. Choose "Restore from seed"
4. Enter your 15 words in exact order
5. Verify wallet loads correctly
6. Check receive address matches

**If restore fails:**
- Recheck word spelling
- Verify word order
- Some words look similar (affect vs effect)

---

### Step 5: Set Spending Password

**If wallet supports it:**
- Use strong, unique password
- Store password separately from seed phrase
- Consider password manager (NOT for seed!)
- Enable biometric lock if available

---

### Step 6: Get Receive Address

**This is what goes into mining config.**

1. Open wallet
2. Go to "Receive" or "Deposit" section
3. Copy receive address (long alphanumeric string)
4. Verify address format:
   - Starts with `9` (mainnet Ergo address)
   - Length: ~50-60 characters
   - Example format: `9f4QP8...(more characters)...ABC123`

**DO NOT confuse with:**
- ❌ Private key (never share this)
- ❌ Seed phrase (15 words, never share)
- ❌ Spending password (wallet unlock)

---

## What to Use in Mining Config

### Format:
```
ERG_WALLET_ADDRESS_HERE
```

### Worker Naming:
When configuring miners, append worker name:
- **gpu-node-1:** `ERG_WALLET_ADDRESS_HERE.ai1`
- **gpu-node-2:** `ERG_WALLET_ADDRESS_HERE.ai2`

**Example command structure (PLACEHOLDER ONLY):**
```bash
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user ERG_WALLET_ADDRESS_HERE.ai1 \
  --pass x
```

**Replace `ERG_WALLET_ADDRESS_HERE` with your actual receive address.**

---

## Address Format Validation

### Valid Ergo Address Checklist:
- [ ] Starts with `9` (mainnet)
- [ ] Length approximately 50-60 characters
- [ ] Contains only alphanumeric characters (no spaces)
- [ ] Copied from "Receive" section of wallet
- [ ] Does NOT contain seed words
- [ ] Does NOT contain private key

### Test Before Mining:
1. **Send test transaction:**
   - Get small amount of ERG from faucet or exchange
   - Send 0.01 ERG to your address
   - Verify it arrives in wallet
   - **Only proceed with mining if test succeeds**

---

## Security Best Practices

### Physical Security:
- Store seed phrase in fireproof safe (ideal)
- Keep separate from computer/phone
- Consider bank safety deposit box for large amounts
- Tell trusted family member location (in case of emergency)

### Digital Security:
- **Never** type seed phrase on internet-connected device
- Use strong spending password
- Enable 2FA if wallet supports it
- Keep wallet software updated
- Beware of phishing (fake wallet websites)

### Pool Security:
- Use SSL/TLS pool connections (stratum+tcp:// or stratum+ssl://)
- Verify pool URL before connecting
- Monitor first payout to confirm address works

---

## Wallet Backup Checklist

Before starting 72h mining test:

- [ ] Seed phrase written on paper
- [ ] Seed phrase verified (wallet restored successfully)
- [ ] Paper backup stored securely
- [ ] Spending password recorded separately
- [ ] Receive address copied and verified
- [ ] Test transaction sent and received (optional but recommended)
- [ ] Worker names decided (.ai1, .ai2)
- [ ] NO seed phrase on mining nodes
- [ ] NO private keys in mining config

---

## Troubleshooting

### "My wallet won't restore from seed"
- Check word spelling (some words are similar)
- Verify word order (must be exact)
- Try different wallet software (Nautilus vs Mobile)
- Ensure using Ergo wallet (not Yoroi/Cardano)

### "I lost my seed phrase"
- **If wallet still open:** Generate new wallet, transfer funds
- **If wallet closed:** Funds may be unrecoverable
- **Prevention:** Always verify backup before storing funds

### "Can I change my address?"
- Yes, generate new wallet
- Transfer funds from old to new (requires fee)
- Update mining config with new address

---

## Final Pre-Mining Verification

**Complete this checklist before starting EXP-001:**

1. [ ] Seed phrase written and stored securely
2. [ ] Wallet recovery tested successfully
3. [ ] Receive address copied (starts with `9`)
4. [ ] Test transaction completed (optional)
5. [ ] Worker names decided
6. [ ] Mining config template prepared
7. [ ] NO seed/private keys on mining nodes
8. [ ] Confirmed: Receive address only (public)

---

## References

- **Ergo Official:** https://ergoplatform.org/
- **Nautilus Wallet:** https://github.com/nautls/nautilus-wallet
- **Ergo Explorer:** https://explorer.ergoplatform.com/ (check transactions)
- **Mining Guide:** See `ERG_72H_TEST.md` in this directory

---

## Next Steps

After wallet creation:
1. Proceed to `ERG_72H_TEST.md` for mining test runbook
2. Configure miners with your receive address
3. Start 72h test on gpu-node-1 and gpu-node-2
4. Monitor earnings at pool dashboard

---

**Created:** 2026-02-16
**For:** crypto-lab EXP-001 (72h Ergo mining test)
**Safety Level:** 🔒 Maximum (seed phrase never on mining nodes)
