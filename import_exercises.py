is_vowel = input('Enter a vowel ')
if is_vowel in ['a', 'e', 'i', 'o', 'u']:
    print ('True')
else:
    print('False')



is_consonant = input('Enter a consonant ')
if is_consonant in ['a', 'e', 'i', 'o', 'u']:
    print ('False')
else:
    print('True')

from function_exercises import calculate_tip


print(calculate_tip(83.75, .10))

print(f"Your bill's tip is: ${round(calculate_tip(83.75, .10), 2)}")

bill = float(input("How much is the bill? : "))

tip = float(input("What is the decimal tip you'd like to leave? (15% = 0.15) : "))

#print(calculate_tip(bill, tip))

print(f"Your bill's tip is: ${round(calculate_tip(bill, tip), 2)}")
