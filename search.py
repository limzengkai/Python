print("\t\tSpecific Coach ID.")
cnt=int(input("Are you sure to continue it?\nPress 1 to continue or Press any other number to exit.\nEnter Your Choice: "))
while (cnt==1):
    print("\t\tSpecific Coach ID.")
    coaid=str(input("Enter specific coach ID: "))
    coafile=open("coalist.txt","r")

    test = 0
    for line in coafile:
        line=line.rstrip()
        if coaid in line:
            test += 1
            print(line)
            cnt=int(input("Do you still continue it?\nPress 1 to continue or Press any other number to exit.\nEnter Your Choice:"))
            break
        
    if test==0:
        print("no found")
        
        
        

    coafile.close()

