# Problem 63 (Powerful Digit Counts)
# ==================================
# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

# For all n, 10**n is an (n+1)-digit integer. 10 as a base is out, for all n.
# So are bases > 10.
# Valid bases are 1 to 9 inclusive.

# Now, consider how B**n relates to its own length.
# We can observe that every B starts a bit too short,
# then enters a zone where it's about the right length,
# then becomes too long and stays that way.

# A range of 100 turns out to be more than enough.
integers = {i**j for i in range(1,10) for j in range(100) if len(str(i**j)) == j}
print(len(integers))
