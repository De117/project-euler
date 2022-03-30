package problems;

public class Euler27 {
    /*
    Euler discovered the remarkable quadratic formula:

        n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
    However, when n=40, 40²+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41²+41+41
    is clearly divisible by 41.

    The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n² + an + b , where |a|<1000 and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4

    Find the product of the coefficients, a and b, for the quadratic expression that produces
    the maximum number of primes for consecutive values of n, starting with n=0.
     */
    public long solution() {
        long maxLength = 0;
        int bestA = -999;
        int bestB = -999;
        for (int a=-999; a < 1000; a++) {
            for (int b=-999; b <= 1000; b++) {
                long length = primeSequenceLength(a, b);
                if (length > maxLength) {
                    maxLength = length;
                    bestA = a;
                    bestB = b;
                }
            }
        }
        return bestA * bestB;
    }

    private long primeSequenceLength(long a, long b) {
        long counter = 0;
        for (long n=0; isPrime(n*n + a*n + b); n++) {
            counter += 1;
        }
        return counter;
    }

    private boolean isPrime(long N) {
        long upperBound = (long)Math.ceil(Math.sqrt(N));

        if (N <= 1) {
            return false;
        } else if (N <= 3) {
            return true;
        } else if (N % 2 == 0) {
            return false;
        }

        for (int i = 3; i <= upperBound; i+=2) {
            if (N % i == 0) {
                return false;
            }
        }

        return true;
    }
}
