def read_input():
    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))
        if litres < 0 or not (2.0 <= fat <= 7.0) or not (6.0 <= snf <= 11.0):
            print("Error: Values out of valid range.")
            return None
        return litres, fat, snf
    except ValueError:
        print("Error: Invalid numeric input format.")
        return None

if __name__ == "__main__":
    result = read_input()
    if result:
        litres, fat, snf = result
        print(f"Validated Input -> Litres: {litres:.2f}, Fat: {fat:.2f}, SNF: {snf:.2f}")
```[cite: 7]
