#!/usr/bin/env python3
"""
Paper Ranking - Cryptocurrency Mining Profitability Analysis
Analyzes WhatToMine data to rank coin/algorithm combinations
"""

import json
import sys
import os
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# Target algorithms for GPU mining (prioritized)
TARGET_ALGORITHMS = [
    'KHeavyHash',    # Kaspa
    'Autolykos2',    # Ergo
    'KawPow',        # Ravencoin
    'ZelHash',       # Flux (EquihashZero)
    'Octopus',       # Conflux
]

# Additional GPU-mineable algorithms
GPU_ALGORITHMS = [
    'KHeavyHash', 'Autolykos2', 'KawPow', 'ZelHash', 'Octopus',
    'Ethash', 'EtHash', 'Etchash', 'FiroPow',
    'ProgPoW', 'ProgPowZ', 'KAWPOW',
    'Equihash', 'BeamHashIII', 'ZHash',
    'RandomX', 'CryptoNightR', 'CryptoNightGPU',
    'NexaPow', 'FishHash', 'SHA512256d'
]

def normalize_algorithm(algo: str) -> str:
    """Normalize algorithm name for comparison"""
    algo_map = {
        'KAWPOW': 'KawPow',
        'Autolykos': 'Autolykos2',
        'EquihashZero': 'ZelHash',
        'Equihash 125,4': 'ZelHash',
    }
    return algo_map.get(algo, algo)

def load_whattomine(filepath: Path) -> List[Dict[str, Any]]:
    """Load and parse WhatToMine coins data"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        coins = []
        for coin_name, coin_data in data.get('coins', {}).items():
            if not isinstance(coin_data, dict):
                continue

            algo = normalize_algorithm(coin_data.get('algorithm', ''))

            # Skip non-GPU algorithms
            if algo not in GPU_ALGORITHMS:
                continue

            # Parse market cap (remove $ and commas)
            market_cap_str = coin_data.get('market_cap', '$0')
            try:
                market_cap = float(market_cap_str.replace('$', '').replace(',', ''))
            except (ValueError, AttributeError):
                market_cap = 0

            coins.append({
                'name': coin_name,
                'tag': coin_data.get('tag', ''),
                'algorithm': algo,
                'profitability': coin_data.get('profitability', 0),
                'profitability24': coin_data.get('profitability24', 0),
                'btc_revenue': float(coin_data.get('btc_revenue', 0)),
                'btc_revenue24': float(coin_data.get('btc_revenue24', 0)),
                'market_cap': market_cap,
                'nethash': coin_data.get('nethash', 0),
                'lagging': coin_data.get('lagging', False),
                'exchange_rate_vol': coin_data.get('exchange_rate_vol', 0),
            })

        return coins
    except Exception as e:
        print(f"Error loading WhatToMine data: {e}", file=sys.stderr)
        return []

def score_coin(coin: Dict[str, Any]) -> float:
    """
    Calculate composite score for ranking
    Factors: profitability, market cap, liquidity, stability
    """
    # Base profitability score
    prof_score = coin['profitability24'] or coin['profitability'] or 0

    # Market cap bonus (larger = more established)
    if coin['market_cap'] > 100_000_000:  # >100M
        mcap_bonus = 1.3
    elif coin['market_cap'] > 10_000_000:  # >10M
        mcap_bonus = 1.1
    else:
        mcap_bonus = 1.0

    # Liquidity bonus (exchange volume)
    liquidity_bonus = 1.0 + (coin['exchange_rate_vol'] * 0.1)

    # Penalty for lagging
    lag_penalty = 0.7 if coin['lagging'] else 1.0

    # Priority bonus for target algorithms
    algo_bonus = 1.5 if coin['algorithm'] in TARGET_ALGORITHMS else 1.0

    return prof_score * mcap_bonus * liquidity_bonus * lag_penalty * algo_bonus

def format_market_cap(mcap: float) -> str:
    """Format market cap for display"""
    if mcap >= 1_000_000_000:
        return f"${mcap/1_000_000_000:.2f}B"
    elif mcap >= 1_000_000:
        return f"${mcap/1_000_000:.1f}M"
    elif mcap >= 1_000:
        return f"${mcap/1_000:.0f}K"
    else:
        return f"${mcap:.0f}"

def main():
    data_dir = Path(__file__).parent
    whattomine_path = data_dir / 'whattomine_coins.json'

    print("# Cryptocurrency Mining - Paper Ranking")
    print()
    print("**Data Source:** WhatToMine API")
    if whattomine_path.exists():
        mtime = datetime.fromtimestamp(os.path.getmtime(whattomine_path))
        print(f"**Date:** {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("**Date:** N/A")
    print()

    # Load data
    coins = load_whattomine(whattomine_path)

    if not coins:
        print("⚠️ No coin data loaded!", file=sys.stderr)
        sys.exit(1)

    print(f"**Total GPU-mineable coins analyzed:** {len(coins)}")
    print()

    # Score and rank
    for coin in coins:
        coin['score'] = score_coin(coin)

    coins_sorted = sorted(coins, key=lambda x: x['score'], reverse=True)

    # Top 10 Overall
    print("## Top 10 Coin/Algorithm Combinations (Composite Score)")
    print()
    print("| Rank | Coin | Tag | Algorithm | Prof24 | BTC/day | Market Cap | Notes |")
    print("|------|------|-----|-----------|--------|---------|------------|-------|")

    for i, coin in enumerate(coins_sorted[:10], 1):
        tag = coin['tag']
        name = coin['name']
        algo = coin['algorithm']
        prof = coin['profitability24'] or coin['profitability']
        btc = coin['btc_revenue24'] or coin['btc_revenue']
        mcap = format_market_cap(coin['market_cap'])

        notes = []
        if coin['algorithm'] in TARGET_ALGORITHMS:
            notes.append("🎯 Target")
        if coin['lagging']:
            notes.append("⚠️ Lagging")
        if coin['market_cap'] > 100_000_000:
            notes.append("💎 Large cap")

        notes_str = " ".join(notes) if notes else "—"

        print(f"| {i} | {name} | {tag} | {algo} | {prof} | {btc:.8f} | {mcap} | {notes_str} |")

    print()

    # Top 5 Target Algorithms
    print("## Top Coins by Target Algorithm (for Benchmarking)")
    print()

    for target_algo in TARGET_ALGORITHMS:
        algo_coins = [c for c in coins_sorted if c['algorithm'] == target_algo]

        if not algo_coins:
            print(f"### {target_algo}: ❌ No coins found")
            print()
            continue

        top_coin = algo_coins[0]
        print(f"### {target_algo}: {top_coin['name']} ({top_coin['tag']})")
        print(f"- **Profitability 24h:** {top_coin['profitability24']}")
        print(f"- **BTC Revenue/day:** {top_coin['btc_revenue24']:.8f}")
        print(f"- **Market Cap:** {format_market_cap(top_coin['market_cap'])}")
        print(f"- **Network Hashrate:** {top_coin['nethash']}")
        print()

    # Algorithm distribution
    print("## Algorithm Distribution (GPU-mineable)")
    print()
    algo_counts = {}
    for coin in coins:
        algo = coin['algorithm']
        algo_counts[algo] = algo_counts.get(algo, 0) + 1

    sorted_algos = sorted(algo_counts.items(), key=lambda x: x[1], reverse=True)

    print("| Algorithm | Coins | Priority |")
    print("|-----------|-------|----------|")
    for algo, count in sorted_algos[:15]:
        priority = "🎯 YES" if algo in TARGET_ALGORITHMS else "—"
        print(f"| {algo} | {count} | {priority} |")

    print()
    print("---")
    print()
    print("**Next Steps:**")
    print("1. Install miner supporting target algorithms")
    print("2. Run real benchmarks on gpu-node-1 (RTX 3060) and gpu-node-2 (GTX 1660 SUPER)")
    print("3. Combine paper ranking with real hashrate + power data")

if __name__ == '__main__':
    main()
