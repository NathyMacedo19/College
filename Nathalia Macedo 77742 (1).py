#NAME: NATHALIA_FIGUEREDO_MACEDO
#STUDENTID: 77742
#EMAIL: 77742@student.dorset-college.ie
#PERSONAL-EMAIL: nathy.macedo@hotmail.com

#Continuous Assessment 2

def display_welcome_message():
    print("Welcome to the Blood Type Compatibility Checker!")
    print("-------------------------------------------------------------")
    print("This program helps you understand blood type compatibility.")
#Function as "Display Welcome Msg", brings it up for the user the initial message.
#Function Definition (def): display_welcome_message() is the function's name.
#Body of Function: The print statements output the welcome message and program purpose.
#Purpose: This sets the stage for the user, explaining what the program does and making them feel welcome.

def display_menu():
    print("Choose an option:")
    print("1. Check who can donate to your blood type.")
    print("2. Check who you can donate blood to.")
    print("3. Exit the program.")
#The "Display Menu Options" is a function that allows the user to interact with the system, giving multiple choise.
#Function Definition (def): display_menu() is the function's name.
#Body of Function: The print statements display the menu options.
#Purpose: This guides the user to select from different actions they can take.
  

def get_donation_compatibility():
    return {
        'A+': ['A+', 'AB+'],
        'O+': ['O+', 'A+', 'B+', 'AB+'],
        'B+': ['B+', 'AB+'],
        'AB+': ['AB+'],
        'A-': ['A+', 'A-', 'AB+', 'AB-'],
        'O-': ['Everyone'],
        'B-': ['B+', 'B-', 'AB+', 'AB-'],
        'AB-': ['AB+', 'AB-']
    }

def get_receive_compatibility():
    return {
        'A+': ['A+', 'A-', 'O+', 'O-'],
        'O+': ['O+', 'O-'],
        'B+': ['B+', 'B-', 'O+', 'O-'],
        'AB+': ['Everyone'],
        'A-': ['A-', 'O-'],
        'O-': ['O-'],
        'B-': ['B-', 'O-'],
        'AB-': ['AB-', 'A-', 'B-', 'O-']
    }
#Function as "Blood Type Compatibility Data" its a kind of library that is interacting with the most part of the code.
#Function Definitions (def): get_donation_compatibility() and get_receive_compatibility() return dictionaries.
#Dictionaries: These store blood type compatibility data.
#Purpose: These functions provide the rules for blood donation and reception, which are crucial for the compatibility checks. 

def check_donation(blood_type):
    compatibility = get_donation_compatibility()
    if blood_type in compatibility:
        return compatibility[blood_type]
    else:
        return None

def check_receiving(blood_type):
    compatibility = get_receive_compatibility()
    if blood_type in compatibility:
        return compatibility[blood_type]
    else:
        return None
#Checking Compatibility this function - check the compatibility of the blood type using the dictionaries from the previous step to return the list of compatible blood types or None if the blood type is not found.
#Function Definitions (def): check_donation(blood_type) and check_receiving(blood_type) check compatibility.
#Get Compatibility Data: They call the compatibility functions to get the data.
#Conditional Check (if): They check if the blood_type is in the compatibility dictionary.
#Return Values: If found, they return the compatible blood types; otherwise, they return None.
#Purpose: These functions determine the compatibility of blood types for donation and reception.

def validate_blood_type(blood_type):
    valid_blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    return blood_type in valid_blood_types
#Validating Blood Type list prevents the system of invalid inputs, for example if the user tap another letter out of this set.
#Function Definition (def): validate_blood_type(blood_type) checks if the input blood type is valid.
#List of Valid Blood Types: valid_blood_types stores all acceptable blood types.
#Membership Test (in): The function checks if blood_type is in the list of valid blood types.
#Return Value: It returns True if valid, False otherwise.
#Purpose: This ensures that only recognized blood types are accepted, preventing invalid input.

def main():
    display_welcome_message()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            blood_type = input("Enter your blood type (e.g., A+, O-, AB+): ")
            if validate_blood_type(blood_type):
                compatible_donors = check_receiving(blood_type)
                if compatible_donors:
                    print(f"Blood Type {blood_type} can receive donations from: {', '.join(compatible_donors)}")
                else:
                    print("No compatibility information found.")
            else:
                print(f"Invalid blood type: {blood_type}. Please try again.")
                
        elif choice == '2':
            blood_type = input("Enter your blood type (e.g., A+, O-, AB+): ")
            if validate_blood_type(blood_type):
                compatible_recipients = check_donation(blood_type)
                if compatible_recipients:
                    print(f"Blood Type {blood_type} can donate to: {', '.join(compatible_recipients)}")
                else:
                    print("No compatibility information found.")
            else:
                print(f"Invalid blood type: {blood_type}. Please try again.")
                
        elif choice == '3':
            print("Thank you for using the Blood Type Compatibility Checker. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
#Main Program.
#Function Definition (def): main() is the main function that runs the program.
#Welcome Message: display_welcome_message() is called to greet the user.
#Infinite Loop (while True): Keeps the program running until the user chooses to exit.
#Display Menu: display_menu() is called to show the user the menu options.
#User Input (input()): Captures the user’s menu choice and blood type.Menu Choice Handling:
#Option 1: Checks who can donate to the user's blood type.
#Option 2: Checks who the user can donate to.
#Option 3: Exits the program with a goodbye message.
#Invalid Input: Prompts the user to enter a valid choice.
#Blood Type Validation: Uses validate_blood_type() to ensure the input blood type is valid.
#Compatibility Checks: Uses check_donation() and check_receiving() to find compatible blood types.
