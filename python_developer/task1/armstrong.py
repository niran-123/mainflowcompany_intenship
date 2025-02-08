num = int(input("Enter a no: "))
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
is_armstrong = num == armstrong_sum
print(is_armstrong)
