package problems;

public class Euler3 {
    /*
    Largest prime factor
    Problem 3

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
     */

    public long solution() {
        final long number = 600851475143L;
        final int upperBound = (int) Math.ceil(Math.sqrt(number));

        int maxFactor = 1;
        for (int i=3; i <= upperBound; i+=2) {
            if (number % i == 0 && isPrime(i)) {
                maxFactor = i;
            }
        }

        return maxFactor;
    }

    private boolean isPrime(int N) {
        int upperBound = (int)Math.ceil(Math.sqrt(N));

        if (N == 1) {
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
