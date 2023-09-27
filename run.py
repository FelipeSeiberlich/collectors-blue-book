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
print('This program is designed to be a contact book.')
print('Enjoy one of the following options bellow\n')



def display_contact():
    """
    Provide a contact book menu for the user.
    """
    print("Name\t\t Contact Number")
    for key in contact:
        print("{}\t\t{}". format(key, contact.get(key)))
while True:
    choice = int(input(" 1. Add new contact\n 2. Search contact\n 3. Display contact\n 4. Edit contact\n 5. Delete contact\n 6. Exit\n \nEnter your choice: "))
                                                                                                                                                                           
  
                                                                                                                                                                           
   
                                                                                                                                                                           

