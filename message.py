from tabulate import tabulate

table = [['MESSAGE', 'NAVIGATION', 'DIAGNOSTICS'], ['CREW MANIFEST', 'CARGO MANIFEST', 'SYSTEM INFO']]

def boot_screen():
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    navigation_msg = input(f'\nPROCEED\n \n')
    if navigation_msg == "message":
        start_message()
        response()

# add typewriter effect so that it appears it's being written in real time

# here we are getting the message to appear in the terminal
def start_message():
    # this prompt will display that the message is incoming
    message = input(f'\nMESSAGE INCOMING... \n \n')
    # the message will be entered, appearing as though it is incoming
    if message:
        print(f'\nTRANSMITTING MESSAGE...\n')
# we want the message to failure randomly
        # print(f'MESSAGE FAILURE')

# we want to be able to have it appear as if there is a response to the message
def response():
    message = input(f'ENTER RESPONSE... \n \n')
    if message == "exit":
         print(f'\nENDING CORRESPONDENCE')
    else: 
         print(f'\nTRANSMITTING RESPONSE...')
         start_message()
         response()

boot_screen()