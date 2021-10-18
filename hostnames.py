def show_menu():            # displays menu when in interactive mode 
    # Function purpose: display menu options 
    # Function parameters: none 
    # Function return: none
    # Function body: display menu
    print("~ Hostnames Menu: ~")
    print("\tD - Display hosts")
    print("\tS - Search hosts")
    print("\tA - Add hosts")
    print("\tQ - Quit")
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
    host_information = input(prompt).lower()

    while (len(host_information.split("\t")) != 2):
        print("Input error: 2 arguments required.")
        host_information = input(prompt).lower()

    return host_information 
    
def qualify_hostname(hostname, domain="cst8245.lab"):     # fully qualifies hostname with default domain 
    # Function purpose: fully qualify hostname 
    # Function parameters: hostname, default domain 
    # Function return: fully qualified domain name
    # Function body: if the hostname is not qualified (it does not contain a period in the name) append the default domain name "cst8245.lab".
    if hostname.split("\t")[0].find(".") <0:
        hostname = hostname.split("\t")[0] + "." + domain + " " + hostname.split("\t")[1]
    
    return hostname
    
def get_search_string(prompt):    # prompts user for search string 
    # Function purpose: prompt user for search string 
    # Function parameters: prompt 
    # Function return: search string 
    # Function body: prompt user for search string

    reqest = input(prompt)
    return reqest
 
def show_hosts(file_handle):           # displays all hosts  
    # Function purpose: display all hosts recorded in host file 
    # Function parameters: file handle 
    # Function return: none 
    # Function body: display all hosts recorded in file
    
    print(file_handle.read())
    
def search_hosts(file_handle, search_string ):         # displays matching hosts based on search string 
    # Function purpose: display matching hosts recorded in host file based on search string 
    # Function parameters: file handle, search string 
    # Function return: True if matching hosts found, else False  
    # Function body: match each host in the hosts file with the search string and  display all matching hosts 
    results = False

    for line in file_handle:
        if line.find(search_string) >= 0:
            print(line)
            results=True
    
    return results
    
def add_host(file_handle, host_information):             # writes host information to hosts file 
    # Function purpose: write host information to hosts file 
    # Function parameters: file handle, host information 
    # Function return: none

    file_handle.write("\n" + host_information)
    file_handle.close()

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
        file_handle = open(filename,"w+")
        file_handle.close()
        raise  

    else:
        file_handle = open(filename, "r")
    
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
        file_handle = open(filename,"w+")
        file_handle.close()
        raise   
    
    else:
        file_handle = open(filename, "a")
    
    return file_handle 


if __name__ == "__main__" :
    filename = "hostnames.txt"
    # Display menu 
    show_menu()

    # Get menu option 
    reqest = get_menu_option("Enter menu selection: ")
    
    # While menu option not quit 
    while (reqest !="q"):
        # If menu option display 
        if reqest == "d":
            # Open file in read mode 
            file_handle = open_read(filename)
    
            # Display all hosts 
            show_hosts(file_handle)
    
        # Else if menu option search  
        elif reqest == "s":
            # Open file in read mode 
            file_handle = open_read(filename)

            # Get search string 
            search_string = get_search_string("Enter a search string: ")
            results = ""
            
            # If match found: 
            if search_hosts(file_handle,search_string) == False:
                # Display message 
                print("No matching hosts found")
        
        # Else if menu option add 
        elif reqest == "a":
            # Open file in append mode 
            file_handle = open_append(filename)
            
            # Get host information 
            host_information = get_hostinfo("Enter hostname & IP address: ")
            
            # Fully qualify hostname 
            host_information = qualify_hostname(host_information)

            # Add host information to host file 
            add_host(file_handle,host_information)

        else:
            # Display wrong menu option 
            print("Wrong menu option")

        # Display menu 
        show_menu()

        # Get menu option
        reqest = get_menu_option("Enter menu option: ")

