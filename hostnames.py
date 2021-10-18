def show_menu():            # displays menu when in interactive mode 
    # Function purpose: display menu options 
    # Function parameters: none 
    # Function return: none
    # Function body: display menu
    print("D - Display hosts\nS - Search hosts \nA - Add hosts\nQ - Quit")
    pass

def get_menu_option(prompt):      # prompts user for menu selection 
    # Function purpose: get menu option 
    # Function parameters: prompt 
    # Function return: user-selected menu option 
    # Function body: prompt user for menu option
    reqest = input(prompt)
    return reqest
    
def get_hostinfo(prompt):         # prompts user for host-related data 
        
    # Function purpose: prompt user for host information 
    # Function parameters: prompt
    # Function return: host information, a list with two elements, in all lower case or the quit symbol 
    # Function body:
    # •	Prompt user for hostname and IP address.
    # •	Validate that two arguments have been entered.
    # •	Re-prompt when necessary.
    pass
    
def qualify_hostname(hostname, domain="cst8245.lab"):     # fully qualifies hostname with default domain 
    # Function purpose: fully qualify hostname 
    # Function parameters: hostname, default domain 
    # Function return: fully qualified domain name
    # Function body: if the hostname is not qualified (it does not contain a period in the name) append the default domain name "cst8245.lab".
    pass
    
def get_search_string(prompt):    # prompts user for search string 
    # Function purpose: prompt user for search string 
    # Function parameters: prompt 
    # Function return: search string 
    # Function body: prompt user for search string
    pass
 
def show_hosts(file_handle ):           # displays all hosts  
    # Function purpose: display all hosts recorded in host file 
    # Function parameters: file handle 
    # Function return: none 
    # Function body: display all hosts recorded in file
    with file_handle:
        print(file_handle)
    pass
    
def search_hosts(file_handle, search_string ):         # displays matching hosts based on search string 
    # Function purpose: display matching hosts recorded in host file based on search string 
    # Function parameters: file handle, search string 
    # Function return: True if matching hosts found, else False  
    # Function body: match each host in the hosts file with the search string and  display all matching hosts 
    pass
    
def add_host(file_handle, host_information):             # writes host information to hosts file 
    # Function purpose: write host information to hosts file 
    # Function parameters: file handle, host information 
    # Function return: none
    pass
    
def open_read(filename):            # open file in read mode 
    # Function purpose: open file in read mode 
    # Function parameters: filename 
    # Function return: file handle 
    # Function body: open file in read mode with exception handling and return file handle or raise exception
    try: 
        file_handle = open(filename, "r")
    # we want to catch all possible exceptions  
    except Exception:  
        # re-raise exception & handle in calling function 
        print(Exception)
        raise   
    else: 
       return file_handle 
    
def open_append(filename):          # open file in append mode
    # Function purpose: open file in append mode 
    # Function parameters: filename 
    # Function return: file handle 
    # Function body: open file in append mode with exception handling and return file handle or raise exception
    try: 
        file_handle = open(filename, "a")
    # we want to catch all possible exceptions  
    except Exception:  
        # re-raise exception & handle in calling function 
        print(Exception)
        raise   
    else: 
       return file_handle 


if __name__ == "__main__" :
    print("main")

    # Display menu 
    show_menu()
    # Get menu option 
    reqest = get_menu_option("Enter menu selection:")
    # While menu option not quit 
    while (reqest !="q"):
        # If menu option display 
        if reqest == "d":
            # Open file in read mode 
            open_read()
            # Display all hosts 
            show_hosts()
        # Else if menu option search  
        elif reqest == "s":
            # Open file in read mode 
            open_read()

            # Get search string 
            keyword = get_search_string()
            # If match found: 
            if len(keyword) > 0:
                # Display all matched hosts 
                pass

            # Else: 
            else:
                # Display message 
                pass
        # Else if menu option add 
        elif reqest == "a":
            # Open file in append mode 
            open_append()
            # Get host information 
            # Fully qualify hostname 
            # Add host information to host file 
        # Else: 
        else:
            # Display wrong menu option 
            pass

        # Display menu 
        show_menu()

        # Get menu option
        reqest = get_menu_option("Enter menu option:")

