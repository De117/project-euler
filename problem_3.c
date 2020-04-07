#include <stdio.h>
#include <math.h>

/**
 * Euler project
 *   problem 3 -- Largest prime factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */

int isprime(long n) {
    for(int i=2; i<sqrt(n); i++) {
        if (n%i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    long n = 600851475143;

    for(int factor=2; factor < sqrt(n); factor++) {
        if (n % factor == 0 && isprime(factor)) {
            printf("%d\n", factor);
        }
    }

    return 0;
}
