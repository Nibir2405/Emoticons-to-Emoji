#Converting Emoticons to Emoji/Emoji to Emoticon

#Ask the user which transformation he wants.
print("Two types of Transformation this program can output.\n1.Emoticons to Emoji\n2.Emoji to Emoticons ")

number_of_function = 2

emoji_or_emoticon = int(input("Type the number of the option you want. "))

def number_print():
    #input has to be greater than 0 and less than 

    if emoji_or_emoticon == 1:
        
        text = feature_no1()

        match text:
            case ":)":
                print("🙂")
    
            case ":(":
                print("😔")

            case ":‑|":
                print("😑")

            case ">w<":
                print("😖")
    
            case ":P":
                print("😋")
    
            case ":D":
                print("😀")

            case ":O":
                print("😮")
    
            case ";)":
                print("😉")
    
            case "B|":
                print("😎")
    
            case ":/":
                print("😕")
    
            case ":'(":
                print("😢")

            case "3:)":
                print("😈")
    
            case "O:)":
                print("😇")
    
            case ":*":
                print("😘")
    
            case "<3":
                print("💙")
    
            case "-_-":
                print("😑")
    
            case ":3":
                print("🥴")

            case "(^^^)":
                print("🦈")
    
            case ":poop":
                print("💩")
    
            case "(y)":
                print("👍")
    
            case ":))":
                print("😄")

            case "X(":
                print("😡")

            case "/:)":
                print("🤨")

            case ":-&":
                print("🤮")

            case ":O)":
                print("🤡")

            case "=D>":
                print("👏")

            case ":|]":
                print("🤖")

            case ":-B":
                print("🤓")

            case "<):)":
                print("🤠")

            case ":-?":
                print("🤔")

            case "@-)":
                print("😵")

            case ">:D<":
                print("🤗")

            case "Φ_Φ":
                print("😨")

            case ":‑.":
                print("🥱")

            case "xD":
                print("😂")

            case ":$":
                print("😳")

            case "=^.^=":
                print("🐱")

            case "~_~":
                print("😴")

            case "^_~":
                print("🕺")

            case "</3":
                print("💔")

            case ">:|":
                print("🙄")

            case "-|--'":
                print("✈")
    
            case "(.V.)":
                print("👽")

            case "$_$":
                print("🤑")

            case ":->":
                print("😁")

            case "~:0":
                print("👶")

            case "(8-)":
                print("👨‍🦲")

            case "<=====<>~":
                print("🐸")

            case "(=^_^=)":
                print("🐰")

            case "@-->---":
                print("🌹")

 
    elif emoji_or_emoticon == 2:
        feature_no2 ()
    elif emoji_or_emoticon != (1,2):
        print("Try writing correct no. of the function you want")

#defining the two function i have mentioned
def feature_no1():
    return input("Write an emoticons ")
    

def feature_no2():
    return input("Write an Emoji ")
    


number_print()
 