# Import necessary functions and dictionary
from functions import feature_no1, feature_no2
from dict_of_emj_emt import dict_of_emoticon_emoji

# Converting Emoticons to Emoji/Emoji to Emoticon

# Ask the user which transformation they want.
print("Two types of Transformation this program can output.\n1. Emoticons to Emoji\n2. Emoji to Emoticons")

# Get the user's choice for the type of transformation
emoji_or_emoticon = int(input("Type the number of the option you want: "))

# Perform the transformation based on the user's choice
match emoji_or_emoticon:
    case 1:
        # Get the text to be transformed from feature_no1 function
        text = feature_no1()

        # Replace all emoticons in the text with their corresponding emojis
        for emoticon, emoji in dict_of_emoticon_emoji.items():
            if emoticon in text:
                text = text.replace(emoticon, emoji)
        # Print the transformed text
        print(text)

    case 2:
        # Get the text to be transformed from feature_no2 function
        text = feature_no2()

        # Replace all emojis in the text with their corresponding emoticons
        for emoticon, emoji in dict_of_emoticon_emoji.items():
            if emoji in text:
                text = text.replace(emoji, emoticon)
        # Print the transformed text
        print(text)