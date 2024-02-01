class Shrink:

     def shrink(self, inputString, removeAfterNthCharacter):

        # initializing class variables  
        self.inputString = inputString
        self.removeAfterNthCharacter = removeAfterNthCharacter
        
        # initializing extractor variable that acts as empty string that replaces characters
        extractor = ''
        
        #initializing output string
        outputString = ''

        # initializing variable for increased removal of characters
        stack = 0

        #initializing variable used for resetting the stack variable with increased removal of character
        set = 0


        for x, element in enumerate(inputString):

            # the removal of characters only starts after the second character, since judging by the output in the task, that's how it works
            # but by my judgment, this would be an output bug if I didn't have an example 1 or 2, and correct would be without this feature
            # I guess it is up for discussion about specifications :)

            #in v0.2 changed from fixed to customizable character
            if x < removeAfterNthCharacter-1 :
                outputString = outputString + element
            # this acts as a skip/removal of certain characters in a string
            # this will keep happening until the stack is depleted
            elif stack > 0 :
                    outputString = outputString + extractor
                    stack -= 1
            # this appends a current character that is in iteration from inputString, also sets and increases the stack for exraction of characters    
            else :
                outputString = outputString + element
                set += 1
                stack = set
        

        # printing result
        print("Output string: " + str(outputString))
        return outputString

class Expand:

     def expand(self, inputString, removeAfterNthCharacter):
          
        # initializing class variables  
        self.inputString = inputString
        self.removeAfterNthCharacter = removeAfterNthCharacter
       
        # initializing expandor variable that acts as empty space that fills space between charcters
        expandor = ' '
        
        #initializing output string
        outputString = ''

        # initializing variable for increased expansion of characters
        stack = 0

        #initializing variable used for resetting the stack variable with increased expansion of character
        set = 0


        for x, element in enumerate(inputString):

            # the expansion of characters only starts after the second character, since judging by the output in the task, that's how it works
            # but by my judgment, this would be an output bug if I didn't have an example 1 or 2, and correct would be without this feature
            # I guess it is up for discussion about specifications :)

            #in v0.2 changed from fixed to customizable character
            if x < removeAfterNthCharacter-1 :
                outputString = outputString + element
            # this acts as an expandor of space, where space is added before a character
            # this will keep happening until the stack is depleted
            elif stack > 0 :
                    outputString = outputString + expandor
                    stack -= 1
            # this appends a current character that is in iteration from inputString, also sets and increases the stack for expansion of characters    
            else :
                outputString = outputString + element
                set += 1
                stack = set
        

        # printing result
        print("Output string: " + str(outputString))
        return outputString
          




def extract_characters_incrementally(removeAfterNthCharacter, inputString): 
    
   
    # initializing extractor variable that acts as empty string that replaces characters
    extractor = ''
    
    #initializing output string
    outputString = ''

    # initializing variable for increased removal of characters
    stack = 0

    #initializing variable used for resetting the stack variable with increased removal of character
    set = 0


    for x, element in enumerate(inputString):

        # the removal of characters only starts after the second character, since judging by the output in the task, that's how it works
        # but by my judgment, this would be an output bug if I didn't have an example 1 or 2, and correct would be without this feature
        # I guess it is up for discussion about specifications :)

        #in v0.2 changed from fixed to customizable character
        if x < removeAfterNthCharacter-1 :
            outputString = outputString + element
        # this acts as a skip/removal of certain characters in a string
        # this will keep happening until the stack is depleted
        elif stack > 0 :
                outputString = outputString + extractor 
                stack -= 1
        # this appends a current character that is in iteration from inputString, also sets and increases the stack for exraction of characters    
        else :
            outputString = outputString + element
            set += 1
            stack = set
    

    # printing result
    print("Output string: " + str(outputString))


# in v0.2 added error handling
try:
    # initializing an input string
    # in v0.2 this was changed to be outside of a function, set to be a controllable parameter before a function call
    userInputString = input("Input string: ")

    # this takes user input about when character extraction starts, added in v0.2
    characterCount = int(input("Customizable parameter 1 - After which character function starts extracting characters incrementally: "))
# possibility of parameters being incorrect, such as string in int based characterCount
except:
    print("Invalid input parameters.")

# this exception is because there is no logical sense to start with negative position or zero
if characterCount <= 0 :
    raise Exception("Not possible to start after nonexistent character (having 0 or negative numbers).")

     



# calls function
# in v0.2 modified with controllable parameters

#original function commented below
#extract_characters_incrementally(characterCount, userInputString)

# creates object for shrinking
shrinkedInput = Shrink()
shrinkedInput.shrink(userInputString, characterCount)

#creates object for expanding
expandedInput = Expand()
expandedInput.expand(userInputString, characterCount)


