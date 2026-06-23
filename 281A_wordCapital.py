'''
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Output
Output the given word after capitalization.

Examples
InputCopy
ApPLe
OutputCopy
ApPLe
InputCopy
konjac
OutputCopy
Konjac
'''

def wordCapital(n: str) -> str:
    newW = n[0] if n[0].isupper() else n[0].upper()
    if len(n)>1:
        newW = f"{newW}{n[1:]}"
    return newW

n = input()
print(wordCapital(n))
