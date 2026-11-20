BASE_RATE = 30.00
FAT_BASE = 3.5
SNF_BASE = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def compute_payment(litres, fat, snf):
    fat_steps = round((fat - FAT_BASE) / 0.1, 0)
    snf_steps = round((snf - SNF_BASE) / 0.1, 0)
    rate_per_litre = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)
    amount = litres * rate_per_litre
    return round(rate_per_litre, 2), round(amount, 2)

if __name__ == "__main__":
    litres, fat, snf = 8.5, 4.2, 8.7
    rate, amt = compute_payment(litres, fat, snf)
    print(f"Rate per litre: {rate}")
    print(f"Total amount: {amt}")
```[cite: 6, 7]
