#Digit reversal function
def reverse(oriNum, mode):
    oriNum = str(oriNum)
    revNum = ''

    #Repeats loop until all digits have finished reversing
    i = -1 #Start from -1 which is right side item. Does not take "-" sign if negative number
    while ((i *-1) < ((len(oriNum) +1 -mode)) ):
        revNum += oriNum[i]
        i -= 1
    
    #Adds a "-" to the front after reversing a negative number
    if (mode == 1):
        revNum = '-' + str(revNum)
    
    #Sends back the reversed string
    return revNum

#String addition function
def add(string1,string2):
    #Changes strings to integers for math
    string1 = int(string1)
    string2 = int(string2)

    #Adds them together
    output = string1 + string2
    
    #Returns back the sum as a string
    return str(output)

#"Check if string is an integer" function
def isInteger(checkNum):
    #Checks if input is a number. If fails, will trigger ValueError which will return 0
    try:
        checkNum = int(checkNum)
        return 1

    except ValueError:
        return 0

#"Check if all items in list is a digit" function
def listIsDigits(checkList):
    i = 0
    failedPos = [1] #failedPos = ['continue?', 'Position 1', 'Position 2', ... 'Position n']

    #This loop will repeat until all items are checked. If item fails, it will add the positions of failures to a list failedPos
    while (i < len(checkList)):
        #Check if digit is an integer
        if( isInteger(checkList[i] ) == 1):
            #Check if digit is not a valid number (from 0 to 9)
            if (int(checkList[i]) < 0 or int(checkList[i]) > 9 or len(checkList[i]) != 1):
                failedPos[0] = 0
                failedPos.append(i)
        else:
            failedPos[0] = 0
            failedPos.append(i)
        i += 1
    return failedPos #If succeed, failedPos = [1]. If failed, failedPos = [0, 3, 5] where 3 and 5 are examples of the position of item that failed

#String to list function
def stringToList(string):
    newList = list(string.split(' ')) #Make a list assuming an item is seperated by a space
    return newList

#List to String function
def listToString(inputList):
    #Adds an item from list to the back of a string until all items in list are converted
    string = ''
    for i in inputList:
        if (i != 0):
            string += str(i)
    return string

#"adds an extra slot to left of list" function
def expand1Left(inputList):
    #Copies a list to a new one that has a bigger size ('0' automatically filled in front)
    i = 1
    outputList = ['0'] 
    while (i < (len(inputList) +1)):
        outputList.append(str(inputList[i-1]))
        i += 1
    return outputList

#"add 1 to the last item" function
def add1Right(inputList):
    #This loop will repeat until the addition is complete, then return the result
    i = -1
    while ((i *-1) < ((len(inputList) +1)) ):
        #Adds 1 to the final item
        inputList[i] = str(int(inputList[i]) +1)
        
        #Stops if the number is between 0 and 9 which causes no problem
        if (int(inputList[i]) < 10):
            return inputList
        
        #If the item becomes 10, change it to 0 and repeat(do +1 again) for the item on the left
        inputList[i] = '0'
        i -= 1
    #If all slots are used up, expands the list and +1 to the furthest left item
    inputList = expand1Left(inputList)
    inputList[0] = str(int(inputList[0]) +1)
    return inputList

#Question 1 function
def Q1():
    print('\n\n\n\n\n============================================================')
    print('This is the function for Question 1.')
    print('It will take an input number and reverse the digits.')
    print('Input [stop] instead to stop the function.')
    print('============================================================')

    #This loop repeats the Q1 function as long as the input is a number
    repeat = 1
    while (repeat == 1):
        #Asks for input number
        inputNum = input('\nInput: ')

        #Checks if input is actually a number
        if(isInteger(inputNum) == 1):
            #Checks if input is a negative
            if (int(inputNum) >= 0):
                inputNum = reverse(inputNum, 0)
                print('Output: ' + str(inputNum))
            else:
                inputNum = reverse(inputNum, 1) #Special Case: mode = 1 ignores "-" at first. Then, add "-" after reverse
                print('Output: ' + str(inputNum))
        else:
            print('The input is not a number. The function for Question 1 will now stop\n\n\n')
            repeat = 0

#Question 2 function
def Q2():
    print('\n\n\n\n\n============================================================')
    print('This is the function for Question 2.')
    print('It will take 2 input numbers (as strings) and add them.')
    print('Input [stop] instead to stop the function.')
    print('============================================================')

    #This loop repeats the Q2 function as long as "stop" is not the input
    repeat = 1
    while (repeat == 1):
        #Asks for input number 1
        inputNum1 = str(input('\nInput string 1: '))

        #Checks if the function is stopped
        if(inputNum1 == 'stop' or inputNum1 == '[stop]'):
            print('The input [stop] is received. The function for Question 2 will now stop\n\n\n')
            repeat = 0
        else:
            #Asks for input number 2
            inputNum2 = str(input('Input string 2: '))

            #Checks if the function is stopped
            if(inputNum2 == 'stop' or inputNum2 == '[stop]'):
                print('The input [stop] is received. The function for Question 2 will now stop\n\n\n')
                repeat = 0
            else:
                #Checks if both input is a number
                if(isInteger(inputNum1) == 1 and isInteger(inputNum2) == 1):
                    #Adds them together and then print
                    print('add("' + inputNum1 + '", "' + inputNum2 + '") -> "' + add(inputNum1,inputNum2) + '"')
                else:
                    print('add("' + inputNum1 + '", "' + inputNum2 + '") -> "Invalid operation"')

#Question 3 function
def Q3():
    print('\n\n\n\n\n============================================================')
    print('This is the function for Question 3.')
    print('It will take an input number and check if it\'s a palindrome')
    print('Input [stop] instead to stop the function.')
    print('============================================================')

    #This loop repeats the Q3 function as long as the input is a number
    repeat = 1
    while (repeat == 1):
        #Asks for input number
        inputNum = input('\nInput: ')

        #Checks if input is actually a number
        if(isInteger(inputNum) == 1):
            #Checks if input is a palindrome by comparing to it's reverse (mode = 0 will not ignore "-")
            if(inputNum == reverse(inputNum, 0)):
                print('Output: true')
            else:
                print('Output: false')
                print('Explanation: From left to right, it reads ' + str(inputNum))
                print('             From right to left, it reads ' + str(reverse(inputNum, 0)))
                
        else:
            print('The input is not a number. The function for Question 3 will now stop\n\n\n')
            repeat = 0

#Question 4 function
def Q4():
    print('\n\n\n\n\n============================================================')
    print('This is the function for Question 4.')
    print('It will take an input list of digits of an integers')
    print('Then, add 1 to it and output a new list')
    print('To input a list, add a space between items like so:')
    print('"2 0 7 7" will be received as list [\'2\', \'0\', \'7\', \'7\']') #Cyberpunk 2077 HAHAHHAHA
    print('Input [stop] instead to stop the function.')
    print('============================================================')

    #This loop repeats the Q4 function as long as "stop" is not the input
    repeat = 1
    while (repeat == 1):
        #Asks for input list
        inputNum = input('\nInput: ')

        #Checks if the function is stopped
        if (inputNum == 'stop' or inputNum == '[stop]'):
            print('The input [stop] is received. The function for Question 4 will now stop\n\n\n')
            repeat = 0
        else: 
            #Turns the input into a list
            inputNum = stringToList(inputNum)
            print('Input as a list: ' + str(inputNum))

            #Checks if each item on list is a digit. If not, print out all the errors
            checkedList = listIsDigits(inputNum)
            if (checkedList[0] == 1):
                arrayRep = listToString(inputNum)

                #Adds 1 to the farthest right item. If the item becomes 10, change it to 0 and repeat(+1 again) for item on the left of it
                addedList = add1Right(inputNum)
                print('Output: ' + str(addedList))

                addedInteger = listToString(addedList)
                Explanation = 'Explanation: The input array represents the integer ' + arrayRep + '.'
                print(Explanation)
                print('             After it is added by 1, it becomes ' + str(addedInteger) + '.')
            else:
                i = 1
                positions = 'The value(s)...\n'

                while (i+1 < len(checkedList)):
                    positions += '\'' + str(inputNum[ int(checkedList[i]) ]) + '\' at position [' + str(checkedList[i]) + '],\n'
                    i += 1
                positions += '\'' + str(inputNum[ int(checkedList[i]) ]) + '\' at position [' + str(checkedList[i]) + '] is not valid.'
                print(positions)
                



#Main program starts here
print('============================================================')
print(' This program is made by LZK for ')
print('         ML Task 1 which includes 4 questions.         ')

#This loop repeats the main program as long as the input is a valid number
repeat = 1
while (repeat == 1):
    #Asks what function to use
    print('============================================================')
    print('What function do you want to test? Input the number')
    print('[1] - Question 1: Digits Reversal')
    print('[2] - Question 2: Sum of Strings')
    print('[3] - Question 3: Palindrome or not?')
    print('[4] - Question 4: From Array +1, then becomes integer')
    print('[5] - Stop the program')
    print('============================================================')
    q = input('\nI want to use program: ')

    #Triggers a function to solve the corresponding question. If not a valid question, program will stop
    if (q == '1'):
        Q1()
    elif (q == '2'):
        Q2()
    elif (q == '3'):
        Q3()
    elif (q == '4'):
        Q4()
    else:
        print('The input is not a question number. The program will now stop\n')
        repeat = 0
    

