#!/usr/bin/env python3
"""
Real Ranking - Combine paper ranking with actual benchmark results
Analyzes real GPU hashrates, power consumption, and temperature data
"""

import json
import csv
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from statistics import mean

# Benchmark results (manual extraction from outputs)
BENCHMARK_RESULTS = {
    'gpu-node-1': {  # RTX 3060
        'KawPow': {'hashrate': 9.55, 'unit': 'MH/s', 'coin': 'Ravencoin', 'power': 119, 'temp': 60},
        'Autolykos2': {'hashrate': 103.05, 'unit': 'MH/s', 'coin': 'Ergo', 'power': 119, 'temp': 62},
        'Octopus': {'hashrate': 80.27, 'unit': 'MH/s', 'coin': 'Conflux', 'power': 112, 'temp': 62},
        'Flux': {'hashrate': 41.1, 'unit': 'Sol/s', 'coin': 'Flux', 'power': 111, 'temp': 61},
        'Pyrin': {'hashrate': 3113.51, 'unit': 'MH/s', 'coin': 'Pyrin', 'power': 112, 'temp': 62},
    },
    'gpu-node-2': {  # GTX 1660 SUPER
        'KawPow': {'hashrate': 10.10, 'unit': 'MH/s', 'coin': 'Ravencoin', 'power': 78, 'temp': 75},
        'Autolykos2': {'hashrate': 49.66, 'unit': 'MH/s', 'coin': 'Ergo', 'power': 79, 'temp': 72},
        'Octopus': {'hashrate': 0.0, 'unit': 'MH/s', 'coin': 'Conflux', 'power': 0, 'temp': 0},  # FAILED - insufficient VRAM
        'Flux': {'hashrate': 17.6, 'unit': 'Sol/s', 'coin': 'Flux', 'power': 70, 'temp': 70},
        'Pyrin': {'hashrate': 1137.33, 'unit': 'MH/s', 'coin': 'Pyrin', 'power': 74, 'temp': 77},
    }
}

GPU_NAMES = {
    'gpu-node-1': 'RTX 3060 (12GB)',
    'gpu-node-2': 'GTX 1660 SUPER (6GB)'
}

def parse_nvidia_smi_csv(filepath: Path) -> Dict[str, float]:
    """Parse nvidia-smi CSV and calculate averages"""
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            return {}

        # Extract numeric values
        power_vals = []
        temp_vals = []
        util_vals = []

        for row in rows:
            try:
                power_str = row.get('power.draw [W]', '0').strip()
                power = float(power_str.replace(' W', ''))
                power_vals.append(power)

                temp_str = row.get('temperature.gpu', '0').strip()
                temp = float(temp_str)
                temp_vals.append(temp)

                util_str = row.get('utilization.gpu [%]', '0').strip()
                util = float(util_str.replace(' %', ''))
                util_vals.append(util)
            except (ValueError, KeyError):
                continue

        return {
            'avg_power': mean(power_vals) if power_vals else 0,
            'avg_temp': mean(temp_vals) if temp_vals else 0,
            'avg_util': mean(util_vals) if util_vals else 0,
            'max_temp': max(temp_vals) if temp_vals else 0,
            'min_power': min(power_vals) if power_vals else 0,
            'max_power': max(power_vals) if power_vals else 0,
        }
    except Exception as e:
        print(f"Warning: Failed to parse {filepath}: {e}")
        return {}

def normalize_algorithm(algo: str) -> str:
    """Normalize algorithm names"""
    algo_map = {
        'KAWPOW': 'KawPow',
        'kawpow': 'KawPow',
        'AUTOLYKOS2': 'Autolykos2',
        'autolykos2': 'Autolykos2',
        'OCTOPUS': 'Octopus',
        'octopus': 'Octopus',
        'FLUX': 'Flux',
        'flux': 'Flux',
        'ZelHash': 'Flux',
        'PYRIN': 'Pyrin',
        'pyrin': 'Pyrin',
        'HeavyHash': 'Pyrin',
    }
    return algo_map.get(algo, algo)

def load_profitability_data(whattomine_path: Path) -> Dict[str, Any]:
    """Load profitability data from WhatToMine"""
    try:
        with open(whattomine_path, 'r') as f:
            data = json.load(f)

        algo_profit = {}
        for coin_name, coin_data in data.get('coins', {}).items():
            if not isinstance(coin_data, dict):
                continue

            algo = normalize_algorithm(coin_data.get('algorithm', ''))
            if algo not in algo_profit or coin_data.get('profitability24', 0) > algo_profit[algo].get('profitability24', 0):
                algo_profit[algo] = {
                    'coin': coin_name,
                    'tag': coin_data.get('tag', ''),
                    'algorithm': algo,
                    'profitability24': coin_data.get('profitability24', 0),
                    'btc_revenue24': float(coin_data.get('btc_revenue24', 0)),
                }

        return algo_profit
    except Exception as e:
        print(f"Warning: Failed to load profitability data: {e}")
        return {}

def main():
    bench_dir = Path(__file__).parent / 'bench_results'
    data_dir = Path(__file__).parent

    print("# Real Benchmark Results & Profitability Analysis")
    print()
    print(f"**GPU Nodes:** {', '.join(GPU_NAMES.values())}")
    print(f"**Date:** {Path(__file__).parent.name if Path(__file__).parent.name != 'profit-run' else '2026-02-16'}")
    print()

    # Load profitability data
    whattomine_path = data_dir / 'whattomine_coins.json'
    profit_data = load_profitability_data(whattomine_path)

    # Parse all CSV files
    results = []

    for node in ['gpu-node-1', 'gpu-node-2']:
        for algo, bench in BENCHMARK_RESULTS[node].items():
            csv_file = bench_dir / f"bench_{algo.lower()}_${node.replace('-', '')}.csv"

            # Try different filename patterns
            possible_files = [
                bench_dir / f"bench_{algo.lower()}_{node.replace('-', '')}.csv",
                bench_dir / f"bench_{algo.lower()}_{node}.csv",
            ]

            metrics = {}
            for csv_file in possible_files:
                if csv_file.exists():
                    metrics = parse_nvidia_smi_csv(csv_file)
                    break

            # Use hardcoded metrics from benchmark outputs
            power = bench.get('power', 0)
            temp = bench.get('temp', 0)

            hashrate = bench['hashrate']
            unit = bench['unit']
            coin = bench['coin']

            # Get profit data
            algo_norm = normalize_algorithm(algo)
            profit_info = profit_data.get(algo_norm, {})

            # Calculate efficiency
            efficiency = (hashrate / power) if power > 0 else 0

            # Estimate daily BTC revenue (very rough estimate)
            # This is a placeholder - real calculation would need network difficulty
            btc_revenue_ref = profit_info.get('btc_revenue24', 0)

            results.append({
                'node': node,
                'gpu': GPU_NAMES[node],
                'algorithm': algo,
                'coin': coin,
                'hashrate': hashrate,
                'unit': unit,
                'power': power,
                'temp': temp,
                'max_temp': temp,
                'efficiency': efficiency,
                'profitability24': profit_info.get('profitability24', 0),
                'btc_revenue24': btc_revenue_ref,
                'status': 'OK' if hashrate > 0 else 'FAILED',
            })

    # Filter out failed benchmarks
    valid_results = [r for r in results if r['status'] == 'OK']

    print("## Raw Benchmark Results")
    print()
    print("| GPU | Algorithm | Coin | Hashrate | Power | Temp | Efficiency |")
    print("|-----|-----------|------|----------|-------|------|------------|")

    for r in results:
        status_icon = "✅" if r['status'] == 'OK' else "❌"
        print(f"| {r['gpu']} | {r['algorithm']} | {r['coin']} | "
              f"{r['hashrate']:.2f} {r['unit']} | {r['power']:.1f}W | "
              f"{r['temp']:.0f}°C | {r['efficiency']:.2f} {r['unit'][0]}H/W {status_icon} |")

    print()

    # Ranking 1: Top by raw hashrate per algorithm
    print("## Ranking 1: Best GPU per Algorithm (by Hashrate)")
    print()
    print("| Algorithm | Winner | Hashrate | Power | Efficiency | Notes |")
    print("|-----------|--------|----------|-------|------------|-------|")

    algos_checked = set()
    for r in sorted(valid_results, key=lambda x: (x['algorithm'], -x['hashrate'])):
        if r['algorithm'] in algos_checked:
            continue
        algos_checked.add(r['algorithm'])

        notes = []
        if r['temp'] > 70:
            notes.append("⚠️ High temp")
        if r['efficiency'] > 1.0:
            notes.append("💚 Efficient")

        print(f"| {r['algorithm']} | **{r['gpu']}** | {r['hashrate']:.2f} {r['unit']} | "
              f"{r['power']:.0f}W | {r['efficiency']:.2f} | {' '.join(notes) if notes else '—'} |")

    print()

    # Ranking 2: Top by efficiency (hashrate per watt)
    print("## Ranking 2: Most Efficient (Hashrate per Watt)")
    print()
    print("| Rank | GPU | Algorithm | Efficiency | Hashrate | Power |")
    print("|------|-----|-----------|------------|----------|-------|")

    sorted_by_eff = sorted(valid_results, key=lambda x: -x['efficiency'])
    for i, r in enumerate(sorted_by_eff[:10], 1):
        print(f"| {i} | {r['gpu']} | {r['algorithm']} | "
              f"**{r['efficiency']:.2f}** {r['unit'][0]}H/W | "
              f"{r['hashrate']:.2f} {r['unit']} | {r['power']:.0f}W |")

    print()

    # Ranking 3: Most stable (low temp, stable power)
    print("## Ranking 3: Most Stable (Low Temperature)")
    print()
    print("| Rank | GPU | Algorithm | Avg Temp | Max Temp | Power | Hashrate |")
    print("|------|-----|-----------|----------|----------|-------|----------|")

    sorted_by_temp = sorted(valid_results, key=lambda x: (x['temp'], -x['hashrate']))
    for i, r in enumerate(sorted_by_temp[:10], 1):
        temp_status = "🟢" if r['temp'] < 65 else ("🟡" if r['temp'] < 75 else "🔴")
        print(f"| {i} | {r['gpu']} | {r['algorithm']} | "
              f"{r['temp']:.0f}°C {temp_status} | {r['max_temp']:.0f}°C | "
              f"{r['power']:.0f}W | {r['hashrate']:.2f} {r['unit']} |")

    print()

    # Summary & Recommendation
    print("## Summary & 72h Test Recommendation")
    print()

    # Find best overall option
    # Criteria: high profit potential, good efficiency, stable temps
    scored = []
    for r in valid_results:
        score = 0
        # Efficiency bonus
        if r['efficiency'] > 1.0:
            score += r['efficiency'] * 10
        # Temperature penalty
        if r['temp'] < 65:
            score += 20
        elif r['temp'] < 75:
            score += 10
        # Profitability bonus (if data available)
        score += r['profitability24'] / 10
        # Power efficiency bonus
        if r['power'] < 100:
            score += 10

        scored.append((score, r))

    scored.sort(key=lambda x: -x[0])

    if scored:
        best = scored[0][1]
        print(f"### 🏆 Recommended: {best['algorithm']} ({best['coin']})")
        print()
        print(f"**Hardware:** {best['gpu']}")
        print(f"**Hashrate:** {best['hashrate']:.2f} {best['unit']}")
        print(f"**Power Consumption:** {best['power']:.1f}W")
        print(f"**Temperature:** {best['temp']:.0f}°C (max {best['max_temp']:.0f}°C)")
        print(f"**Efficiency:** {best['efficiency']:.2f} {best['unit'][0]}H/W")
        print()
        print("**Rationale:**")
        reasons = []
        if best['efficiency'] > 1.0:
            reasons.append(f"- Excellent power efficiency ({best['efficiency']:.2f} {best['unit'][0]}H/W)")
        if best['temp'] < 70:
            reasons.append(f"- Low operating temperature ({best['temp']:.0f}°C) = long-term stability")
        if best['power'] < 100:
            reasons.append(f"- Low power consumption ({best['power']:.0f}W) = reduced electricity cost")
        if best['node'] == 'gpu-node-1':
            reasons.append("- RTX 3060 has 12GB VRAM for future flexibility")

        for reason in reasons:
            print(reason)
        print()

        # Runner-ups
        print("**Alternative options:**")
        for i, (score, r) in enumerate(scored[1:4], 2):
            print(f"{i}. **{r['algorithm']}** on {r['gpu']}: "
                  f"{r['hashrate']:.2f} {r['unit']}, {r['power']:.0f}W, {r['temp']:.0f}°C")
        print()

    # Important notes
    print("## Important Notes")
    print()
    print("1. **GTX 1660 SUPER Octopus FAIL:** Insufficient VRAM (6GB < requirement)")
    print("2. **Power Limits Active:** gpu-node-1=120W, gpu-node-2=80W (hardware throttled)")
    print("3. **Profitability estimates** are based on WhatToMine data and may vary with:")
    print("   - Network difficulty changes")
    print("   - Cryptocurrency price fluctuations")
    print("   - Pool fees and payout methods")
    print("4. **72h test** should monitor:")
    print("   - Actual shares accepted vs rejected")
    print("   - Pool-reported hashrate stability")
    print("   - Hardware stability and temperature trends")
    print("   - Actual earnings vs estimates")
    print()
    print("---")
    print()
    print("**Next Step:** Configure chosen algorithm for 72h production test with real wallet address.")

if __name__ == '__main__':
    main()
