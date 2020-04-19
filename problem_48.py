# Problem 48 (Self powers)
#
# The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
#
# Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
if __name__ == "__main__":
    print(str(sum(i**i for i in range(1, 1001)))[-10:])
