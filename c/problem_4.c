#include <stdio.h>
#include <math.h>

/**
 * Euler project
 *   problem 4 -- Largest palindrome product
 *
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

int howmany_digits(long n) {
    return ceil( log10( n ));
}

int extract_digit(long n, int index) {
    return (int)(n / pow(10, index)) % 10;
}

int is_palindrome(long n) {
    int n_digits = howmany_digits(n);
    for(int i=0; i < ceil(n_digits/2); i++) {
        if (extract_digit(n, i) != extract_digit(n, n_digits-1-i)) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int largest_palindrome = 0;
    for(int i=100; i<1000; i++) {
        for(int j=i; j<1000; j++) {
            if (is_palindrome(i*j) && i*j > largest_palindrome) {
                largest_palindrome = i*j;
            }
        }
    }
    printf("Largest palindrome that is a product of two 3-digit numbers is %d\n", largest_palindrome);
    return 0;
}
