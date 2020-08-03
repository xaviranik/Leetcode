# https://leetcode.com/problems/unique-morse-code-words/

def uniqueMorse(words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
             "....","..",".---","-.-",".-..","--","-.",
             "---",".--.","--.-",".-.","...","-","..-",
             "...-",".--","-..-","-.--","--.."]
    
        alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        d={}

        for key in alpha:
            for value in MORSE:
                d[key]=value
                MORSE.remove(value)
                break


        a=''
        b=[]
        for i in words:
            for j in i:
                a=a+(d[j])
            b.append(a)
            a=''

        return(len(set(b)))