package problems;

import common.PrimeDecomposition;

public class Euler23 {
    /*
    Non-abundant sums
    Problem 23

    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper limit
    cannot be reduced any further by analysis even though it is known that the
    greatest number that cannot be expressed as the sum of two abundant numbers
    is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
     */
    public long solution() {

        // Precompute abundancy
        boolean[] isAbundant = new boolean[29001];
        for (int i = 1; i <= 29000; i++) {
            isAbundant[i] =  isAbundant(i);
        }

        long sum = 0;
        for (int i = 1; i <= 28123; i++) {

            // Check all pairs of numbers that sum up to `i`
            boolean canBeWritten = false;
            for (int j = 1; j < i; j++) {
                if (isAbundant[j] && isAbundant[i-j]) {
                    canBeWritten = true;
                    break;
                }
            }

            if (!canBeWritten) {
                sum += i;
            }
        }

        return sum;
    }

    private boolean isAbundant(int n) {
        int sum = 0;
        for (long divisor : (new PrimeDecomposition(n)).getProperDivisors()) {
            sum += divisor;
        }
        return sum > n;
    }
}
