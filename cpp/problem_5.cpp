#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

/**
 * Euler project
 *   problem 5 -- Smallest multiple
 *
 * 2520 is the smallest number that can be divided by each of the numbers from
 * 1 to 10 without any remainder. What is the smallest positive number that is
 * evenly divisible by all of the numbers from 1 to 20?
 */

typedef std::vector< std::pair<long, long>> PrimeDecomposition;

int isprime(long n) {
    for(int i=2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int calc_arity_of_divisor(long n, long divisor) {
    int arity = 0;
    long div = divisor;
    while (n % div == 0) {
        arity++;
        div *= divisor;
    }
    return arity;
}

auto decompose_into_prime_factors(long n) {
    std::vector< std::pair<long,long> > factors;

    if (isprime(n)) {
        factors.push_back( std::make_pair( n, 1 ));
        return factors;
    }

    for(int factor=2; factor <= ceil(n/2); factor++) {
        if ((n % factor == 0) && isprime(factor)) {
            factors.push_back( std::make_pair( factor, calc_arity_of_divisor(n, factor)));
        }
    }

    return factors;
}

/**
 * This, in fact, finds the smallest common multiple of both d1 and d2.
 */
auto add_prime_decompositions(PrimeDecomposition d1, PrimeDecomposition d2) {
    std::vector< std::pair<long,long> > result;

    for(auto &p1 : d1) {
        long factor = p1.first;
        long power = p1.second;

        // update existing ones (those in both d1 and d2)
        auto found = std::find_if(d2.begin(), d2.end(),
                        [factor] (std::pair<long,long> p) {return p.first==factor;}
                     );
        if (found != d2.end() && found->second > power) {
            power = found->second;
        }

        result.push_back(std::make_pair(factor, power));
    }

    // add in the rest (those in d2 but not in d1)
    for(auto &p2 : d2) {
        if (d1.end() == std::find_if(d1.begin(), d1.end(),
                                     [p2] (std::pair<long,long> p1)
                                          {return p1.first == p2.first;}
                                    ))
        {
            result.push_back(p2);
        }
    }

    // sort and return
    std::sort(result.begin(), result.end());

    return result;
}

int main() {

    // sum up the prime factors with their multiplicities
    PrimeDecomposition added;
    for(int i=1; i<=20; i++) {
        auto d = decompose_into_prime_factors(i);
        added = add_prime_decompositions(added, d);
    }

    // get the result
    long product = 1;
    for(auto &p : added) {
        product *= (long)pow(p.first, p.second);
    }

    printf("The smallest number evenly divisible by 1 to 20 is %ld\n", product);
    return 0;
}
