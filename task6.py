BASE_RATE = 30.00
FAT_BASE = 3.5
SNF_BASE = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Returns the price per litre, rounded to 2 decimals."""
    fat_steps = round((fat - FAT_BASE) / 0.1, 0)
    snf_steps = round((snf - SNF_BASE) / 0.1, 0)
    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)
    return round(rate, 2)

def payout(litres, fat, snf):
    """Returns the amount payable to the farmer, rounded to 2 decimals."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)

def ten_day_total(daily_entries):
    """Returns the total ten-day payout for a list of daily entries."""
    total = 0.0
    for litres, fat, snf in daily_entries:
        total += payout(litres, fat, snf)
    return round(total, 2)

if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    print(f"Ten-day total: {ten_day_total(entries)}")
```[cite: 8]
