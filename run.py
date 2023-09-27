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
    print("==========================================")
    print("|Name            | Number           |")
    print("==========================================")
    for key in contact:
        # format to left-align and give some spacing
        print("{}\t\t{}". format(key, contact.get(key)))
    print("==========================================")

while True:
    choice = int(input(" 1. Add new contact\n 2. Search contact\n 3. Display contact\n 4. Edit contact\n 5. Delete contact\n 6. Exit\n \nEnter your choice: "))
    if choice == 1:
        print('Option 1 selected')
        name = input("\nEnter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
        display_contact()




    

    

                                                                                                                                                                           
  
                                                                                                                                                                           
   
                                                                                                                                                                           

