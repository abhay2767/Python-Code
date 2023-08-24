""" write a python program to translate a message into secret code language.
    use the rule below to translate normal English into secret code language 
    #Coding:
    1- If the word contains atleast 3 character, remove the first letter and append it at end
     
     
     Encoding:
        Abhay
        bhayA
        vgdbhayAder    or double nam ie: Abhay du    du: ud
     Decoding:
        ud = du 
        bhayA
        Abhay

    
    2- Now append three random characters at the starting and the end
    else:
        simply reverse the string
    
    #Decoding:
    1- if the word contains less than 3 character, reverse it.
    else:
        remove 3 random characters from start and end. Now remove the last letter and
        append it to the begining

    #Your program should ask wheather you want to code or decode
"""


st = input("Enter Message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding == "1") else False #shorthand if else
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            rnd1 = "dfe"
            rnd2= "swe"
            stnew = rnd1+ word[1:] + word[0] + rnd2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))