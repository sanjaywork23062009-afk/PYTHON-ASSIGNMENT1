def get_recommended_design(litres, fat, snf):
    base_rate = 30.00
    fat_steps = round((fat - 3.5) / 0.1, 0)
    snf_steps = round((snf - 8.5) / 0.1, 0)
    rate = base_rate + (fat_steps * 0.40) + (snf_steps * 0.30)
    return round(litres * rate, 2)

if __name__ == "__main__":
    test_litres = 500.0
    test_fat = 4.2
    test_snf = 8.7
    payout = get_recommended_design(test_litres, test_fat, test_snf)
    print(f"Recommended Design Payout: {payout}")
```[cite: 14]
