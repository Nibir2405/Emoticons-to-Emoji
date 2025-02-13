# Dictionary mapping emoticons to their corresponding emojis
dict_of_emoticon_emoji = {
    ":)": "😊",
    ":(": "😔",
    ":‑|": "😑",
    ">w<": "😖",
    ":P": "😋",
    ":D": "😀",
    ":O": "😮",
    ";)": "😉",
    "B|": "😎",
    ":/": "😕",
    ":'(": "😢",
    "3:)": "😈",
    "O:)": "😇",
    ":*": "😘",
    "<3": "💙",
    "-_-": "😑",
    ":3": "🥴",
    "(^^^)": "🦈",
    ":poop": "💩",
    "(y)": "👍",
    ":))": "😄",
    "X(": "😡",
    "/:)": "🤨",
    ":-&": "🤮",
    ":O)": "🤡",
    "=D>": "👏",
    ":|]": "🤖",
    ":-B": "🤓",
    "<):)": "🤠",
    ":-?": "🤔",
    "@-)": "😵",
    ">:D<": "🤗",
    "Φ_Φ": "😨",
    ":‑.": "🥱",
    "xD": "😂",
    ":$": "😳",
    "=^.^=": "🐱",
    "~_~": "😴",
    "^_~": "🕺",
    "</3": "💔",
    ">:|": "🙄",
    "-|--'": "✈",
    "(.V.)": "👽",
    "$_$": "🤑",
    ":->": "😁",
    "~:0": "👶",
    "(8-)": "👨‍🦲",
    "<=====<>~": "🐸",
    "(=^_^=)": "🐰",
    "@-->---": "🌹"
}

# If this script is run directly, print all emoticon-emoji pairs
if __name__ == "__main__":
    for emj, emt in dict_of_emoticon_emoji.items():
        print(emj, emt)