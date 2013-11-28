from bs4 import BeautifulSoup             # A web scraping tool

def parse_html_table(file_name):
    file = open(file_name, "r")
    soup = BeautifulSoup(file)           # creating a bs4 object
    tbody_tag = soup.find_all("tbody")   # creates a list of all the 'tbody'
    
    stack_2d = []                        # A list that will hold tuple of size 3
    inner_stack = []
    
    for string in tbody_tag[3].strings:  # Lets me interate over the string in the html
        
        inner_stack.append(string)    
        
        if len(inner_stack) == 3:
            stack_2d.append(tuple(inner_stack))  # (field name, field type, size)
            inner_stack = []
            
    return stack_2d                             #note: string are in Unicode...

if __name__=="__main__":
    test =  parse_html_table("Report.html")
    for index, value in enumerate(test):
        print index, value

