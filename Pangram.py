Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> def pangram():
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = input()
    s = s.replace(' ','').lower()
    s= sorted(s)
    
    count = {}
    missing =[]
    
    for letter in s:
        if letter in count:
            continue
        else:
            count[letter] = 1
  
    for letter in alphabet:
        if letter in count:
            count[letter]+=1            
        else:
            count[letter] = 0
    for letter in count:
        if count[letter]== 0:
            missing.append(letter)
    if len(missing)==0:
        print('Null')
    else:
        print(missing)
