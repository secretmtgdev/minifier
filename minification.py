'''
@author  Michael Wilson 
@date    12/2/2019
@version 1.0.0
'''

# Needed for traversing through the computer files 
import os

# Needed for regex
import re 

# Set up the appropriate regex search pattern 
pattern = '(js|css)$'
rgx = re.compile(pattern)

'''
Idea: 
    For all contents of current directory:
        if content is directory:
            Search directory
        elif content is a JavaScript or CSS file:
            Extract content
            Minify content string 
            Replace content with minified string 
'''
def crawl(dir):
    # Reference the global rgx variable 
    global rgx
    for root, dirs, files in os.walk(dir):
        for fname in files:
            if rgx.search(fname) is not None:
                minifyFile(os.path.join(root, fname))

def minifyFile(fileRef):
    content = ''
    # open the file up 
    with open(fileRef, "r+") as file:
        content = file.read().replace('\n', '')
        content = "".join(content.split())

    with open(fileRef, 'w+') as file:
        file.write(content)

if __name__ == '__main__':
    path_found = False
    
    while(not path_found):
        path = raw_input("What is the relative path of the directory to search from {0}? ".format(os.path.basename(os.getcwd())))
        ans = raw_input("You said {0}, is this correct? ".format(path))
        if(ans == 'yes' or ans == 'yea'):
            path_found = True

    # switch to the directory that was specified
    print "Changing directories"
    os.chdir(path)
    crawl('.')