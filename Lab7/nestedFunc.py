def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier
multiplywith5 = multiplier_of(5)
print(multiplywith5)
print(multiplywith5(9))