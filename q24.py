#q42:
ch=input("Enter an alphabet:")
if (ch>='A' and ch<='Z')or(ch>='a' and ch<='z'):
    if ch=='a' or ch=='i' or ch=='e' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        print('Character entered is a vowel')
    else:
        print('Character entered is a consonant')
elif ch>='0' and ch<='9':
    print('Character is a digit')
else:
    print('Character is a special symbol')