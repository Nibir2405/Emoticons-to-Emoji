#Making Emoji
text = input("")
def faces(text):
    if ":)" in text:
        print(text.strip(":)") + "🙂")
    
    if ":(" in text:
        print(text.strip(":(") + "😔")
    
    if ":‑|" in text:
        print(text.strip(":‑|") + "😑")
    
    if "(>w<)" in text:
        print(text.strip("(>w<)") + "😖")
    

    
     
faces(text)