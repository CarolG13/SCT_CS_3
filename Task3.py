import re

common_passwords = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}
dictionary_words = {"apple", "hello", "sunshine", "dragon", "football", "monkey"}

def suggest_stronger_password():
    return "Try mixing UPPER/lower case, numbers, and symbols (e.g. Abc$789!xyZ)"

def check_password_strength(password):
    strength_score = 0
    suggestions = []

    if len(password) >= 12:
        strength_score += 1
    else:
        suggestions.append("Make it at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        suggestions.append("Include numbers (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        suggestions.append("Include special characters (!@#$ etc).")

    # Extra Checks
    if re.search(r"(.)\1\1", password):
        suggestions.append("Avoid repeating characters (e.g. aaa, 111).")

    if any(word in password.lower() for word in common_passwords):
        suggestions.append("Avoid using common passwords.")

    if any(word in password.lower() for word in dictionary_words):
        suggestions.append("Avoid dictionary words.")

    # Final Result
    if strength_score == 5 and not suggestions:
        return "Strong Password ✅"
    elif strength_score >= 3:
        return "Moderate Password ⚠️\nSuggestions: " + "\n- " + "\n- ".join(suggestions + [suggest_stronger_password()])
    else:
        return "Weak Password ❌\nSuggestions: " + "\n- " + "\n- ".join(suggestions + [suggest_stronger_password()])

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))
