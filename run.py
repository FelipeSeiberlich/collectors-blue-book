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
### ##   ####     ##  ###  ### ###            ## ##    ## ##   ###  ##  #### ##    ##      ## ##   #### ##           ### ##    ## ##    ## ##   ##  ###  
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
print('Select one of the following options bellow and be connected.\n')

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
        print(' ')
        
        print('Please enter your phone number bellow only using numbers.')
        print('Example: 00 353 892516666\n')
        phone = input("Enter the mobile number: ")
        print(' ')
        print('Please double check your data...')
        print(' ')

        contact[name] = phone 
        display_contact()
        print(' ')
        print('What would you like to do now?')
        print(' ')

    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])
        else:
            print(' ')
            print("Sorry :( This name is not present in this contact book.\n")
            print('You can try a new search or select one of the other options bellow :)\n')

    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
            print(' ')
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter mobile number")
            contact[edit_contact] = phone
            print(' ')
            print("contact_updated")
            display_contact( )
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact( )
        else:
            print("Name is not found in contact book")
    else:
        break
    




    

    

                                                                                                                                                                           
  
                                                                                                                                                                           
   
                                                                                                                                                                           

