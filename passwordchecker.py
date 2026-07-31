def checklength(password):
    if len(password) >= 12:
        return True

def checkuppercase(password):
    return any(char.isupper() for char in password)

def checklowercase(password):
    return any(char.islower() for char in password)

def checkdigit(password):
    return any(char.isdigit() for char in password)

def checkspecial(password):
    special = "!@#$%^&*"
    return any(char in special for char in password)


def checkpassword(password):
    issues = []
    passed = 0
    if checklength(password):
        passed += 1
    else:
        issues.append("Password must be at least 12 characters")

    if checkuppercase(password):
        passed += 1
    else:
        issues.append("Password must contain at least 1 uppercase character")

    if checklowercase(password):
        passed += 1
    else:
        issues.append("Password must contain at least 1 lowercase character")

    if checkdigit(password):
        passed += 1
    else:
        issues.append("Password must contain at least 1 digit")

    if checkspecial(password):
        passed += 1
    else:
        issues.append("Password must contain at least 1 special character")

    if passed == 5:
        strength = "STRONG"
    elif passed == 4:
        strength = "MODERATE"
    elif passed == 3:
        strength = "WEAK"
    elif passed <= 2:
        strength = "VERY WEAK"
    return {
        "passed": passed,
        "strength": strength,
        "issues": issues
    }


def suggestimprovement(password):
    suggestion = password
    if not checkuppercase(suggestion):
        suggestion += "A"
    if not checkdigit(suggestion):
        suggestion += "1"
    if not checkspecial(suggestion):
        suggestion += "!"
    if not checklength(suggestion):
        # pad it until it reaches 12 characters
        while len(suggestion) < 12:
            suggestion += "abcdefghijkl"
    return suggestion


def main():
    print("=== PASSWORD STRENGTH CHECKER ===")
    while True:
        pass2 = input("Enter password (or 'quit' to exit): ")
        if pass2 == "quit":
            print("Goodbye")
            break
        result1 = checkpassword(pass2)
        print(f"Rules passed: {result1["passed"]} / 5")
        print(f"Strength: {result1["strength"]}")
        print("")
        if result1["strength"] == "STRONG":
            print("No issues found.")
        else:
            print("Issues found:")
            for a in result1["issues"]:
                print(f"    x {a}")
        if result1["strength"] != "STRONG":
            print(f"Suggest improvement: {suggestimprovement(pass2)}")
        print("------------------------------")

main()