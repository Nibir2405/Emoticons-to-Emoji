#Converting Emoticons to Emoji/Emoji to Emoticon

#Ask the user which transformation he wants.
print("Two times of Transformation this program can output.\n1.Emoticons to Emoji\n2.Emoji to Emoticons ")

emoji_or_emoticon = int(input("Type the number of the option you want. "))

def number_print():
    #input has to be greater than 0 and less than 3
    if emoji_or_emoticon == 1:
        feature_no1 = input("Write an Emoticons ")
        print(feature_no1)
    elif emoji_or_emoticon == 2:
        feature_no2 = input("Write an Emoji ")
        print(feature_no2)

    else:
        print("Write the correct number of the function you want")
        

    

number_print()
    

        
        
    









 

