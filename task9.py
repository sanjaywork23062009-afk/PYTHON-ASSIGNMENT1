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

def run_tests():
    assert validate_entry(10.0, 3.5, 8.5) == True
    assert validate_entry(-2.0, 3.5, 8.5) == False
    assert validate_entry(10.0, 1.5, 8.5) == False
    assert validate_entry(10.0, 7.5, 8.5) == False
    assert rate_per_litre(3.5, 8.5) == 30.00
    assert rate_per_litre(4.2, 8.7) == 33.40
    assert payout(10.0, 3.5, 8.5) == 300
