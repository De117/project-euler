package problems;

public class Euler30 {
    /*
    Digit fifth powers
    Problem 30

    Surprisingly there are only three numbers that can be written
    as the sum of fourth powers of their digits:

        1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
        8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
        9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

    As 1 = 1⁴ is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written
    as the sum of fifth powers of their digits.
     */
    public long solution() {
        // We must have an upper bound.
        //
        // Note: adding another digit increases the number by a factor of 10,
        // but the sum is increased by at most 9⁵, which is equal to 59049.
        //
        // After some point, all numbers will be less than the sum of fifth
        // powers of their digits, and this difference will only increase.
        //
        // We see that the largest possible sum for 6-digit numbers is 354294,
        // but for 7-digit numbers it's 413343. Therefore we can take 354294
        // as an upper bound.
        long sum = 0;
        for (long i = 2; i <= 354294; i++) {
            if (isSumOfDigits(i)) {
                sum += i;
            }
        }
        return sum;
    }

    private boolean isSumOfDigits(long n) {
        long sum = 0;
        for (char c : Long.valueOf(n).toString().toCharArray()) {
            int digit = c - '0';
            sum += digit * digit * digit * digit * digit;
        }
        return n == sum;
    }
}
