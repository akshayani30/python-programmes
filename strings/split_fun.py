string="one,two,three"
words=string.split(",")
print(words)

text="geeks for geeks"

print(text.split()) #splits at space

word="geeks,for,geeks"
print(word.split(',')) #splits at','

words='akshayanisuman'
print(words.split('a')) #splits at 'a'


#how split() work when maxsplit is specified

words="one,two,three,four,five"
print(words.split(',',0)) #maxsplit:0
print(words.split(',',4))#maxsplit:4
print(words.split(',',2))#maxsplit:2

sentence=" * love, u, bava * "
print(sentence.split())