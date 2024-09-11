def within_x_percent(ref, data, x):
    """Check if data is within x% of the reference value ref."""
    lower_bound = ref - (x / 100) * ref
    upper_bound = ref + (x / 100) * ref
    return lower_bound <= data <= upper_bound

def identify_substance(boiling_point):
    """Identify the substance based on its boiling point within a 5% range."""
    substances = {
        "Water": 100,
        "Mercury": 357,
        "Copper": 1187,
        "Silver": 2193,
        "Gold": 2660
    }
    
    for substance, normal_boiling_point in substances.items():
        if within_x_percent(normal_boiling_point, boiling_point, 5):
            return substance
    
    return "Substance unknown"

# Prompt the user for the observed boiling point
observed_boiling_point = float(input("Enter the observed boiling point in °C: "))

# Identify the substance
substance = identify_substance(observed_boiling_point)
print(f"Substance {substance}")