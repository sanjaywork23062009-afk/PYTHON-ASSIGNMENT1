class MilkPaymentAnalyzer:
    def __init__(self):
        self.inputs = {
            "farmer_id": "string",
            "litres": "float",
            "fat_percentage": "float",
            "snf_percentage": "float",
            "shift": "string"
        }
        self.outputs = {
            "rate_per_litre": "float",
            "amount": "float",
            "ten_day_total": "float"
        }
        self.constants = {
            "BASE_RATE": 30.00,
            "BASE_FAT": 3.5,
            "BASE_SNF": 8.5,
            "FAT_STEP_RATE": 0.40,
            "SNF_STEP_RATE": 0.30,
            "DAYS_IN_CYCLE": 10
        }

if __name__ == "__main__":
    analyzer = MilkPaymentAnalyzer()
    print("Inputs:", list(analyzer.inputs.keys()))
    print("Outputs:", list(analyzer.outputs.keys()))
    print("Constants:", list(analyzer.constants.keys()))
```[cite: 3]
