
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

sentence = sentence.replace("!", " ")
# output: The quick brown fox jumps over the lazy dog.
print(sentence) 

sentence = sentence.upper()
# output: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
print(sentence) 

sentence = sentence[::-1]
# output: .GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT
print(sentence) 