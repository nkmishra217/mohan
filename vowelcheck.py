mo=input()
if (mo>='a' and mo<='z') or (mo>='A' and mo<='Z'):
    if mo in ('A','E','I','O','U','a','e','i','o','u'):
        print("Vowel")
    elif mo not in('A','E','I','O','U','a','e','i','o','u'):
        print("Consonant")
else:
    print("invalid")
    
    
