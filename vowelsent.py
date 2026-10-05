sent=input("Enter a sentence:")
count=0
for ch in sent:
    if ch.lower() in "aeiou":
        count+=1
print("Number of vowels:",count)

