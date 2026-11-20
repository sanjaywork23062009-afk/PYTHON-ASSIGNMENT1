def validate_entry(litres, fat, snf):
    if litres < 0 or not (2.0 <= fat <= 7.0) or not (6.0 <= snf <= 11.0):
        return False
    return True

def rate_per_litre(fat, snf):
    base_rate = 30.00
    fat_steps = round((fat - 3.5) / 0.1, 0)
    snf_steps = round((snf - 8.5) / 0.1, 0)
    return round(base_rate + (fat_steps * 0.40) + (snf_steps * 0.30), 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    total = 0.0
    for litres, fat, snf in entries:
        if validate_entry(litres, fat, snf):
            total += payout(litres, fat, snf)
        else:
            print("Invalid entry encountered.")
    return round(total, 2)

if __name__ == "__main__":
    entries = [
        (10.0, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12.0, 3.1, 8.3)
    ]
    print("Ten-day total:", ten_day_total(entries))
```[cite: 10, 11, 12]
