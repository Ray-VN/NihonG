


hiragana_romaji = [
    ["a",  "i",  "u",  "e",  "o"],
    ["ka", "ki", "ku", "ke", "ko"],
    ["sa", "shi","su", "se", "so"],
    ["ta", "chi","tsu","te", "to"],
    ["na", "ni", "nu", "ne", "no"],
    ["ha", "hi", "fu", "he", "ho"],
    ["ma", "mi", "mu", "me", "mo"],
    ["ya",       "yu",       "yo"],
    ["ra", "ri", "ru", "re", "ro"],
    ["wa",                   "wo"],
    ["n"]
]

for group in hiragana_romaji:
    for c in group:
        print(c)
        answer = input()