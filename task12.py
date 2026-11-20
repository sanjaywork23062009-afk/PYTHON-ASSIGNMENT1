def get_rate_card(month):
    if 4 <= month <= 6:
        return 32.00, 0.45, 0.30
    return 30.00, 0.40, 0.30

def rate_per_litre(fat, snf, month):
    base, fat_step, snf_step = get_rate_card(month)
    fat_steps = round((fat - 3.5) / 0.1, 0)
    snf_steps = round((snf - 8.5) / 0.1, 0)
    rate = base + (fat_steps * fat_step) + (snf_steps * snf_step)
    return round(rate, 2)

def payout(litres, fat, snf, month):
    rate = rate_per_litre(fat, snf, month)
    total = litres * rate
    if litres > 500:
        total += litres * 0.50
    return round(total, 2)

if __name__ == "__main__":
    print(payout(550, 4.25, 8.63, 5))
```[cite: 14, 15]
