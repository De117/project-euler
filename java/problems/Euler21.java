package problems;

import common.PrimeDecomposition;
import common.PrimeGenerator;

public class Euler21 {

    /*
    Amicable numbers
    Problem 21

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
    and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
     */

    public long solution() {
        long sum = 0;
        for (long i=2; i < 10000; i++) {
            if (isAmicable(i)) {
                sum += i;
            }
        }
        return sum;
    }

    private boolean isAmicable(long a) {
        PrimeDecomposition p1 = new PrimeDecomposition(a);
        long b = p1.getProperDivisors().stream().reduce(0L, Long::sum);

        PrimeDecomposition p2 = new PrimeDecomposition(b);
        long sum2 = p2.getProperDivisors().stream().reduce(0L, Long::sum);

        return (a != b && a == sum2);
    }
}
