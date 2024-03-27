# Problem 63 (Powerful Digit Counts)
# ==================================
# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

# For all n, 10**n is an (n+1)-digit integer. 10 as a base is out, for all n.
# So are bases > 10.
# Valid bases are 1 to 9 inclusive.
#
# Now, consider how B**n relates to its own length.
#
# For all bases, B**1 will have one digit, which satisfies the property.
# The number of digits -- or rather, the base-10 logarithm of the number, which
# we round up to get the number of digits -- grows, but at a slower rate than 1
# every iteration, and thus falls behind the growth of n, forever.
#
# So for every base, we start at n=1, and once the property stops holding, we quit.

from math import ceil, log10

integers = {1}  # ceil(log10(1**n)) = 0, so it's not covered below

for i in (2,3,4,5,6,7,8,9):
    j = 0
    while True:
        j += 1
        number_of_digits = ceil(log10(i**j))
        if number_of_digits == j:
            integers.add(i**j)
        if number_of_digits < j:
            break

print(len(integers))
