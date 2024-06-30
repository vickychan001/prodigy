import re
def password_checker(password):
    l = len(password)
    uc = any(char.isupper() for char in password)
    lc = any(char.islower() for char in password)
    ns = any(char.isdigit() for char in password)
    spchar = bool(re.match('[W_]', password))

    result = l * 4
    if uc:
        result += 10
    if lc:
        result += 10
    if ns:
        result += 10
    if spchar:
        result += 10

    if l < 8:
        feedback = "Password is too short"
    elif result < 40:
        feedback = "Weak password"
    elif result < 70:
        feedback = "Moderate password"
    elif result < 100:
        feedback = "Strong password"
    else:
        feedback = "Very strong password"

    return feedback

def main():
    password = input("Enter your password: ")
    strength = password_checker(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
