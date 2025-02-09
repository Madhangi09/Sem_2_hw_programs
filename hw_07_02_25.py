#1
def number_to_words(n):
    if n == 0:
        return "Zero"
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    places = ["", "Thousand", "Million", "Billion"]
    def convert(num):
        if num < 10:
            return ones[num]
        if num < 20:
            return teens[num - 10]
        if num < 100:
            return tens[num // 10] + " " + convert(num % 10)
        return ones[num // 100] + " Hundred " + convert(num % 100)
    words = []
    i = 0
    while n > 0:
        if n % 1000:
            words.append(convert(n % 1000) + " " + places[i])
        n //= 1000
        i += 1
        return " ".join(words[::-1]).strip()
num = int(input("Enter a number: "))
print(number_to_words(num))

#2
def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
num = int(input("Enter a number: "))
print(f"Trailing zeros in {num}! : {count_trailing_zeros(num)}")
