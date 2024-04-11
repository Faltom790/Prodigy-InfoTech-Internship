import re

def check_password_strength(password):
    # Define criteria weights
    criteria_weights = {
        'length': 2,
        'uppercase': 2,
        'lowercase': 2,
        'numbers': 2,
        'special_chars': 4,
    }

    # Initialize criteria scores
    criteria_scores = {
        'length': len(password) >= 12,  # Minimum length of 12 characters
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'numbers': bool(re.search(r'[0-9]', password)),
        'special_chars': bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\[\]\\\|`~]', password)),
    }

    # Calculate total score
    total_score = sum(criteria_scores[criteria] * weight for criteria, weight in criteria_weights.items())

    # Determine strength based on total score
    if total_score >= 12:
        strength = 'Very Strong'
    elif total_score >= 9:
        strength = 'Strong'
    elif total_score >= 6:
        strength = 'Moderate'
    else:
        strength = 'Weak'

    return strength, total_score

# Test the function
password = input("Enter your password: ")
strength, total_score = check_password_strength(password)
print(f"Password strength: {strength}")
print(f"Total score: {total_score}")
