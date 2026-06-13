def main():
    return main_menu()

def main_menu():
    while True:
        print("Welcome to ClauseGuard")
        print("")
        print("Choose an Option:")
        print("1. Scan")
        print("2. About")
        print("3. Exit")
    
    
        choice = input()
        
        if choice == "1":
            scan()
        elif choice == "2":
            about()
        elif choice == "3":
            print("Thank you for using ClauseGuard")
            break
        else:
            print("Invalid input. Please try again")

def scan():
    print("Please paste in the TOS or Contract you would like to scan")
            
    scan_text = input()
    
    print("Scanning...")
    return main_menu()

def about():
    print("Developed by Matt McGrath")
    print("Scan any form of Terms of Service, Contract, Lease Contracts, App Agreements, and more.")
    print("ClauseGuard provides a list of categories that contain flags for you to further read into.")
    print("These categories contain buzz words that are commonly seen in these files/terms, and are used to sneakily have you agree to something you may not want to agree to.")
    print("")
    print("ClauseGuard is not a substitution for legal counsel. Always have someone you trust look over any contract prior to signing.")
    print("ClauseGuard is not responsible for any legal discourse created or caused by the use of this tool.")
    print("ClauseGuard is not to be used for legal advice.")
    return main_menu()

main()