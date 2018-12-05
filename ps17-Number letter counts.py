# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


unit = ["","one","two","three","four","five","six","seven","eight","nine"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
n3 = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

sum = ""

for i in range(1,1001):
    hunDig = i//100  # i's hundreds digit
    tensDig = (i-100*hunDig)//10 # i's tens digit
    unitDig = i%10 # i's unit digit
    temp = ""
    
    if i == 1000:  # when i equals to 1000
        temp += "onethousand"
    elif i % 100 ==0: # when i is hundreds
        temp += unit[hunDig]
        temp +="hundred"
    elif i > 100:
        temp = unit[hunDig]+ "hundredand"
        if tensDig == 1 and unitDig != 0:
            temp += n3[unitDig]
        else:
            temp = temp +tens[tensDig] + unit[unitDig]
    elif i >10 and i < 20: # when i between 11~19 included
        temp += n3[unitDig]
    else:
        temp = tens[tensDig] + unit[unitDig]
        
    sum += temp

print(len(sum))
