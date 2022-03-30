package problems;


import common.PrimeDecomposition;

public class Euler5 {
    /*
    Smallest multiple
    Problem 5

    2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
     */
    public long solution() {
        PrimeDecomposition d = new PrimeDecomposition(1);
        for (int i=2; i <= 20; i++) {
            PrimeDecomposition o = new PrimeDecomposition(i);
            d = d.union(o);
        }
        return d.toNumber();

    }
}
