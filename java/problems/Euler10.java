package problems;

import common.PrimeGenerator;

public class Euler10 {

    /*
    Summation of primes
    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
     */
    public long solution() {
        PrimeGenerator primes = new PrimeGenerator();
        long sum = 0;
        long prime = primes.nextPrime();
        while (prime < 2000000) {
            sum += prime;
            prime = primes.nextPrime();
        }
        return sum;
    }
}
