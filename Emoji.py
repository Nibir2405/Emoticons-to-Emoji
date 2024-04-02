#Making Emoji
text = input("")
def faces(text):
    if ":)" in text:
        print(text.strip(":)") + "🙂")
    
    elif ":(" in text:
        print(text.strip(":(") + "😔")
    
    elif ":‑|" in text:
        print(text.strip(":‑|") + "😑")
    
    elif "(>w<)" in text:
        print(text.strip("(>w<)") + "😖")
    
     
     
faces(text)