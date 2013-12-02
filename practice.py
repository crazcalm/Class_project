from bs4 import BeautifulSoup             # A web scraping tool

def parse_html_table(file_name):
    file = open(file_name, "r")
    soup = BeautifulSoup(file)           # creating a bs4 object
    tbody_tag = soup.find_all("tbody")   # creates a list of all the 'tbody'
    
    stack_2d = []                        # A list that will hold tuple of size 3
    inner_stack = []

    for i, value in enumerate(tbody_tag):
        #print i, len(value)
        if len(value)> 20:
			index = i

    #print tbody_tag[index]
   
    for string in tbody_tag[index].strings:  # Lets me interate over the string in the html
        
        inner_stack.append(string)    
        
        if len(inner_stack) == 3:
            stack_2d.append(tuple(inner_stack))  # (field name, field type, size)
            inner_stack = []
            
    return stack_2d                             #note: string are in Unicode...

def data_parser(data):
    """
    This is a sample of a parser we could use.
    The indexes between the html list and the data list
    seem to be off by 1.
    """

    file = open(data, "r").readlines(1024)     #my small computer cant handle the entire file at once...

    for index, line in enumerate(file):
        file[index] = line.split("|")

    return file

if __name__=="__main__":
    test =  parse_html_table("Report.html")
    for index, value in enumerate(test):
        print index, value
        raw_input()

    test2 = data_parser("hudson")
    for index, value in enumerate(test2[0]):
        print index + 1, value
