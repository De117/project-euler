package problems;

import java.math.BigInteger;

public class Euler20 {

    /*
    Factorial digit sum
    Problem 20

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    */

    public long solution() {
        String s = factorial(100).toString();

        long sum = 0;
        for (char c : s.toCharArray()) {
            sum += (c - '0');
        }
        return sum;
    }

    private BigInteger factorial(long N) {
        if (N <= 1) {
            return BigInteger.ONE;
        }
        return factorial(N-1).multiply(BigInteger.valueOf(N));
    }
}
