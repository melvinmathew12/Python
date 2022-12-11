def start():
    #take user input
    y=input("-->Enter your choices: ")
    y=y.upper()
    return y
def loop():
    #show all entries
    if x=="WHOLE":
        for key, value in DICT.items():
            print(key, ' : ', value)
    #quit program
    if x=="0":
        print("you QUIT")
        return 0
    #show enquired data
    if x!="WHOLE" and x!="0":
        for key,value in DICT.items():
            if key == x:
                print(key,":",value)
    #show multiple contact enquired
    if x=="MUL":
        z=input("Enter Multiple Names with COMMA(,) whose Contact's you want to see: ").split(",")
        for i in z:
            if i.upper() in DICT:
                print(i.upper(),':',DICT.get(i.upper()))
            else:
                print(i,"is not in repository")
    #add entry
    if x=="ADD":
        p=input("ENTER THE NAME: ")
        q=int(input("ENTER THE CONTACT NUMBER: "))
        p=p.upper()
        DICT.update({p:q})
        print("REPOSITORY IS UPDATED")
#dictionary dataset of student names and contacts 
DICT={"NAME":"CONTACT NUMBER",
      "AYUSH KUMAR":    "7061977595",
      "MELVIN":         "8590970560",
      "JOMAINA AHMED":  "9687342321",}
print("______________________________________")
print("-->WELCOME TO OUR CONTACT REPOSITORY")
print("______________________________________")
print("-->ENTER THE NAME FOR THIER CONTACT INFO.")
print("-->ENTER >>WHOLE<< TO SEE WHOLE REPOSITORY")
print("-->ENTER >>>Mul<<< TO SEE MULTIPLE CONTACT FROM REPOSITORY")
print("-->PRESS >>0<< to quit")
print("____________________________________________________________")
b=1
while(b==1):
    x=start()
    a=loop()
    if a==0:
        b=0