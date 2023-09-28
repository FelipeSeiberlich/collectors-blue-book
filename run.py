import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('blue_book')
ALLOWED_CHARACTERS=['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
ALLOWED_CHARACTERS_PHONE=['1','2','3','4','5','6','7','8','9','0',' ']

contact = {}
panel = """
                                                    
### #           ##   #              ##          #   
 #  ### ###     # #  #  # # ###     # # ### ### # # 
 #  # # ##      ##   #  # # ##      ##  # # # # ##  
 #  # # ###     # #  ## ### ###     # # ### ### # # 
 #              ##                  ##              

"""
print(panel)
print('***Welcome to the Smurfs collectors Contact Book***')
smurfette = """
/(**(**(**///**              
  */******/*/**/***//         
     *///**//***/********     
          /////***********.   
          /(#        #(,      
          (#(   ,,,..         
          ((/   ,.,. ..         Hi! I am Smurfette. Nice to meet you.
          /((  ..,,***,,      
           ((  /*/%%&@#%/       I will give you some tips in how to use this program...
           /( /(/  *.& (//,   
           .((#&(((##(##%(/,, 
            ((%%%&/%%,%((//** 
           /((%((#/,..,##/*   
            (#   *,...,/,,##((
            /#  ,*.....,,,    
            /(    #%  #(      
           *((  ##%%(###(.    
          .*(....,/......     
"""
print(smurfette)
print('This program is a contact book.')
print('It was created to connect with other smurf collectors.\n')
print('Please enter your contact details in order to participate in the network.')
print('You can entry as many contacts as you want.\n')
print('If you want to search for one of your entries and forgot your contact name, no panic!.')
print('Select the option 3 to display all your entries.\n')

contact = {}

def display_contact():
    print("=================================================")
    print("|Name                        | Number           |")
    print("=================================================")
    for key in contact:
        # format to left-align and give some spacing
        print("{}\t\t{}". format(key, contact.get(key)))
    print("=================================================")

while True:
    choice = int(input(" 1. Add new contact\n 2. Search contact\n 3. Display contact\n 4. Edit contact\n 5. Delete contact\n 6. Exit\n \nEnter your choice:\n"))
    if choice == 1:
        print('Option 1 selected!\n')
        print('Please enter contact name and surname.')
        print('Example: Philip Grant')

        name = input("\nEnter the contact name:\n")
        print(f'The data provided is {name}')
        print(' ')
        
        print('Please enter your phone number below only using numbers.')
        print('Example: 00 353 892516666\n')
        phone = input("Enter the mobile number:\n")
        print(f'The data provided is {phone}')
        print(' ')
        print('Please double check your data...')
        print(' ')

        contact[name] = phone 
        display_contact()
        print(' ')

        validate_name = input('Are you sure that name entered is correct y/n?\n')
        if validate_name == 'y' or validate_name == 'Y':
            print(' ')
            print('Validating...')
        if any(x not in ALLOWED_CHARACTERS for x in name):
            print(' ')
            print("error: invalid character\n")
            print('Sorry but you entered an invalid character.\n')
        else:
            print(' ')
            print('Contact was validated!\n')
            print(' ')

        validate_phone = input('Are you sure that phone entered is correct y/n?\n')
        if validate_phone == 'y' or validate_phone == 'Y':
            print(' ')
            print('Validating...')
        if any(x not in ALLOWED_CHARACTERS_PHONE for x in phone):
            print(' ')
            print("error: invalid character\n")
            print('please go back to the menu and delete this wrong entry.\n')
        else:
            print(' ')
            print('Name and phone were validated! :)\n')
            print(' ')

        back_menu = input('Would you like to return to the menu y/n?\n')
        if back_menu == 'y' or back_menu == 'Y':
            print(' ')
            print('Your last entry was:')
            display_contact()
            print(' ')
            print('Please select one of the following options:\n')
        else:
            print(' ')
            print('Thanks for using The Blue Contact Book.')
            print('See you soon!')
            break
        
    elif choice == 2:
        print('Option 2 selected!\n')
        search_name = input("Enter the contact name:\n")
        if search_name in contact:
            print(' ')
            print(search_name, "'s contact number is", contact[search_name])
            print(' ')
            print('Please select one of the options below to continue or type 6 to exit the program.')
            print(' ')
        else:
            print(' ')
            print("Sorry :( This name is not present in this contact book.\n")
            print('For safety reasons, you should entry the full name to access users phone number\n')
            print('You can try a new search or select one of the other options below :)\n')
            
    elif choice == 3:
        print('Option 3 selected!\n')
        if not contact:
            print(' ')
            print("Empty contact book. :(")
            print('Please add a contact selecting the option 1 below')
            print(' ')
        else:
            print('Check the contacts of the Smurfs lovers below:')
            print(' ')
            display_contact()
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.')
            print(' ')
    elif choice == 4:
        print('Option 4 selected!\n')
        print('Please enter contact exactly how it is displayed in the contact book')
        edit_contact = input("Enter the contact to be edited:\n")
        if edit_contact in contact:
            phone = input("Enter new phone number:\n")
            contact[edit_contact] = phone
            print(' ')
            print("Contact updated bellow:")
            print(' ')
            display_contact( )
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.\n')
        else:
            print("Name is not found in contact book")
            print('Please select Display contact in the menu to check the spelling.\n')
    elif choice == 5:
        print('Option 5 selected!\n')
        del_contact = input("Enter the contact to be deleted:\n")
        if del_contact in contact:
            print(' ')
            confirm = input("Do you want to delete this contact y/n?\n")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
                print('')
                print('This contact was successfully deleted.\n')
            display_contact( )
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.')
            print(' ')
        else:
            print(' ')
            print("Name is not found in contact book")
            print('Please select one of the options bellow to continue or type 6 to exit the program.')
            print(' ')
    else:
        print(' ')
        print('Thanks for using the Blue Contact Book Program.')
        print('See you soon! :)')
        break
    




    

    

                                                                                                                                                                           
  
                                                                                                                                                                           
   
                                                                                                                                                                           

