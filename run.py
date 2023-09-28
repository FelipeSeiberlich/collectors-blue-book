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

contact = {}
panel = """
### ##   ####     ##  ###  ### ###            ## ##    ## ##   ###  ##  #### ##     ##     ## ##   #### ##           ### ##    ## ##    ## ##   ##  ###  
 ##  ##   ##      ##   ##   ##  ##           ##   ##  ##   ##    ## ##  # ## ##     ##    ##   ##  # ## ##            ##  ##  ##   ##  ##   ##  ##  ##   
 ##  ##   ##      ##   ##   ##               ##       ##   ##   # ## #    ##      ## ##   ##         ##               ##  ##  ##   ##  ##   ##  ## ##    
 ## ##    ##      ##   ##   ## ##            ##       ##   ##   ## ##     ##      ##  ##  ##         ##               ## ##   ##   ##  ##   ##  ## ##    
 ##  ##   ##      ##   ##   ##               ##       ##   ##   ##  ##    ##      ## ###  ##         ##               ##  ##  ##   ##  ##   ##  ## ###   
 ##  ##   ##  ##  ##   ##   ##  ##           ##   ##  ##   ##   ##  ##    ##      ##  ##  ##   ##    ##               ##  ##  ##   ##  ##   ##  ##  ##   
### ##   ### ###   ## ##   ### ###            ## ##    ## ##   ###  ##   ####    ###  ##   ## ##    ####             ### ##    ## ##    ## ##   ##  ###
"""
print(panel)
print('*********************************************     Welcome to the Smurfs collectors Contact Book     ****************************************************')
smurfette = """
                                                *//**#///**(////*   /,                           
                                                    **//*(***#/***/****(*******                       
                                                        *******/****************//*//////               
                                                        ./*///*****////*/****/******/**////**          
                                                            ,*////****///((***//********/****,        
                                                                *(((//*************************//      
                                                                    .///////**/***************/*      
                                                                    //(##(    *((((///%#////(/        
                                                                    //(#(         ,,                  
                                                                    /((((      ,.,,,..                
                                                                    /(((/     ...........             
                                                                    /(((/     ....... ....            
                                                                    ,((((    .....,,****,,,           
                                                                     ((#(   .,,,,,,,*******,,         
                                                                     /(((   ,/**///%%%&@%##*/*        
                                                                      ((((  (#((@......   %///,       
                                                                      /((( *#(///  @@.@&..#//(*,,     
                                                                       /((((#%(///(((((/##(((#(*,,,   
                                                                       /((#((########%%%@####(((/*,,  
                                                                       /(((%%%%&&&/%%%%,%#(#(///***,  
                                                                      (#(((#(((#%&/,,,...###/(///**.  
                                                                      /#(#(/#(/(#(/,,....,*###//      
                                                                    ./((/    ./,,......*/,####(/*  
                                                                    /((/  ..,,,......,*//,,(#(%##*
                                                                    /((,   /*........,,,,,.       
                                                                    /#(       #%%/..,##           
                                                                    ./((       #%%(, ###(          
                                                                    //(/    (##%%%%//((#(//.       
                                                                    *//((    ######%*(((#(((/.       
                                                                    .//(/....,..,,,*.........    The right place for Smurfs lovers!!!
"""
print(smurfette)
print('This program is a contact book.')
print('It was created to connect with other smurf collectors.\n')
print('Please enter your contact details in order to participate in the network.\n')

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
    choice = int(input(" 1. Add new contact\n 2. Search contact\n 3. Display contact\n 4. Edit contact\n 5. Delete contact\n 6. Exit\n \nEnter your choice: "))
    if choice == 1:
        print('Option 1 selected!\n')
        print('Please enter you name and surname.')
        print('Example: Philip Grant')

        name = input("\nEnter the contact name: ")
        print(f'The data provided is {name}')
        print(' ')
        
        print('Please enter your phone number bellow only using numbers.')
        print('Example: 00 353 892516666\n')
        phone = input("Enter the mobile number: ")
        print(f'The data provided is {phone}')
        print(' ')
        print('Please double check your data...')
        print(' ')

        contact[name] = phone 
        display_contact()
        print(' ')
        validate_data = input('Are you sure that data entered is correct y/n?')
        if validate_data == 'y' or validate_data == 'Y':
            print(' ')
            print('Validating...')
        allowed_characters=['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
        if any(x not in allowed_characters for x in name):
            print(' ')
            print("error: invalid character\n")
        else:
            print(' ')
            print('Contact was validated!\n')

        back_menu = input('Would you like to return to the menu y/n?')
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
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(' ')
            print(search_name, "'s contact number is", contact[search_name])
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.')
            print(' ')
        else:
            print(' ')
            print("Sorry :( This name is not present in this contact book.\n")
            print('You can try a new search or select one of the other options bellow :)\n')

    elif choice == 3:
        print('Option 3 selected!\n')
        if not contact:
            print(' ')
            print("Empty contact book. :(")
            print('Please add a contact selecting the option 1 bellow')
            print(' ')
        else:
            print('Check the contacts of the Smurfs lovers bellow:')
            print(' ')
            display_contact()
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.')
            print(' ')
    elif choice == 4:
        print('Option 4 selected!\n')
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter new phone number: ")
            contact[edit_contact] = phone
            print(' ')
            print("Contact updated bellow:")
            print(' ')
            display_contact( )
            print(' ')
            print('Please select one of the options bellow to continue or type 6 to exit the program.\n')
        else:
            print("Name is not found in contact book")
            print('Please select one of the options bellow to continue or type 6 to exit the program.\n')
    elif choice == 5:
        print('Option 5 selected!\n')
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            print(' ')
            confirm = input("Do you want to delete this contact y/n?")
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
    




    

    

                                                                                                                                                                           
  
                                                                                                                                                                           
   
                                                                                                                                                                           

