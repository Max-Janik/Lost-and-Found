#!/usr/bin/env python

#IMPORTS

import mechanize
import sys
from bs4 import BeautifulSoup

#LISTS

    #PUNCTUATION
ptc = ["|", "<", ">", "!", "{", "[", "]", "}", "/", ",", ";", ".", ":", "-", "_", "#", "'", "+", "*", "~", "\"", "=", "&", "%", "$", "§", "?", "(", ")"]
    #EXTRAORDINARY CHARACTERS
uncommon = ["é", "ü", "ö", "ä", "ú", "ù", "á", "à"]
    #REPLACEMENT
replace = ["e", "ue", "oe", "ae", "u", "u", "a", "a"]
    #IRRELEVANT CHARACTERS
misc = ["\\xd", "\\xa", "\\x", "\\u"]
    #HTML TAGS
htmlTags = ["br", "b", "tr", "td"]
    #NUMBERS
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    #FILE-EXTENSIONS
Ext = ["jpg", "jpeg", "gif", "png", " k "]
    #ARGV - Input from Webpage
ar = sys.argv
    #FREQUENCY OF WORDS
freq = []
    #MOST COMMON WORDS
data = [0,0,0,0,0,0,0,0,0,0]


#BROWSER SETUP

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


#DEF's

#LOOKING UP THE DESIGNATED IMAGE
def ReverseImageLookup():

    
    #GET SEARCH WEBSITE
    #OPEN IMAGES.GOOGLE.COM
    br.open( "http://images.google.com" )                                         
    #SELECT FORM
    br.select_form( 'f' )                                                         
    #IMAGE URL
    br.form[ 'q' ] = 'http://casiocdn.com/casio-v2/resource/images/products/watches/large/MRGG1000D-1A_large.png' #URL TO PICTURE               
    #SUBMIT FORM
    br.submit()                                                                   
    #READ RESPONSE
    response = br.response().read()                                               
    
    
    
    #REPLACE LATIN CHARs
    for x in range(0, len(uncommon)):
        response = response.replace(uncommon[x], replace[x])
    
    #BEAUTIFUL SOUP SETUP
    soup = BeautifulSoup(response, "html.parser")
    soup_div = soup.findAll("div", {"id":"ires"})
    soup_tr = soup_div[0].findAll("tr")


    

    #DECOMPOSE a-TAGS
    for x in range(0, len(soup_tr)):
        for div in soup_tr[x].findAll("a"): 
            div.decompose()

    #DECOMPOSE cite-TAGS
    for x in range(0, len(soup_tr)):
        for div in soup_tr[x].findAll("cite"): 
            div.decompose()

    
    
    #CONVERT TO STRING
    string = str(soup_tr)

    #MAKE ALL CHARACTERS LOWERCASE
    string = string.lower()
    
    #DELETE "STYLE" HTML TAGs
    while True:
        try:
            st = string[:string.index('style')]
            rng = string[string.index('">')+1:]
            string = st+rng
        except ValueError:
            break

    #DELETE NUMBERS
    for x in range(0, len(numbers)):
        string = string.replace(numbers[x], "")

    #DELETE HTML TAGs
    for x in range(0, len(htmlTags)):
        string = string.replace(htmlTags[x], "")

    #DELETE PUNCTUATION
    for x in range(0, len(ptc)):
        string = string.replace(ptc[x], "")

    #DELETE UNNESSECARY CHARs
    for x in range(0, len(misc)):
        string = string.replace(misc[x], "")

    #DELETE FILE-EXTENSIONS
    for x in range(0, len(Ext)):
        string = string.replace(Ext[x], "")




    #SPLIT STRING INTO LIST, COMPARE FREQUENCY

    #SPLIT ARRAY BY WORDS
    split = string.split()

    #FILL FREQUENCY LIST
    for x in range(0, len(split)):
        freq.append(0)

    #GET FREQUENCY
    for x in range(0, len(split)):
        for y in range(0, len(split)):
            if split[x] == split[y]:
                freq[x] = freq[x]+1
    
    
    #ERASE REPEATING WORDS EXCEPT THE FIRST           
    for x in range(0, len(split)):
        for y in range(0, len(split)):
            if x != y:
                if split[x] == split[y]:
                    freq[y] = -1
                    split[y] = ""


    #SORT BY FREQUENCY
    c = 0
    for x in range(0, len(data)):
        for y in range(0, len(freq)):
            if freq[y] > freq[c]:
                data[x] = split[y]
                print data[x]
                c = y
        print c
        freq[c] = 0

    #FOR DEVELOPMENT ONLY 
    print split
    print freq
    print data


    #END OF DEF



    
#PROGRAMM
ReverseImageLookup()






#END
