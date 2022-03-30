package problems;

import common.PrimeGenerator;

public class Euler7 {

    /*
    10001st prime
    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
     */
    public long solution() {
        PrimeGenerator primes = new PrimeGenerator();
        for(int i=0; i<10000; i++) {
            primes.nextPrime();
        }
        return primes.nextPrime();
    }
}
