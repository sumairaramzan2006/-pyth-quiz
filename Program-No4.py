# text = "hello world 456"
text = input("enter text:")
vowels = "aeiouAEIOU"
vowels_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
          vowels_count += 1
        else:
            consonant_count += 1
total_alpha = vowels_count + consonant_count
print("vowels:", vowels_count)
print("consonant:", consonant_count)
print("total alphabetic character:", total_alpha)
    