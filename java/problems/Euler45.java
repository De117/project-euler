package problems;

public class Euler45 {
    /*
    Triangular, pentagonal, and hexagonal
    Problem 45

    Triangle, pentagonal, and hexagonal numbers are generated
    by the following formulae:

    Triangle 	  	T_n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
    Pentagonal 	  	P_n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
    Hexagonal 	  	H_n=n(2n−1) 	  	1, 6, 15, 28, 45, ...

    It can be verified that T_285 = P_165 = H_143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.
     */
    public long solution() {
        long n = 0;
        for (int i = 286; ; i++) {
            n = triangular(i);
            if (isPentagonal(n) && isHexagonal(n)) {
                break;
            }
        }
        return n;
    }

    private long triangular(long n) {
        return n * (n + 1) / 2;
    }

    private boolean isPentagonal(long n) {
        double x = (1 + Math.sqrt(1 + 24*n)) / 6.0;  // should be an integer
        return (x - (long)x) < 1e-14;
    }

    private boolean isHexagonal(long n) {
        // n = k(2k - 1)
        // 2k² - k - n = 0
        // k₁,₂ = (1 ± √(1 + 8n))/4
        //   and the only sensible option is
        // k = (1 + √(1 + 8n))/4
        //   so
        double x = (1 + Math.sqrt(1 + 8 * n)) / 4.0;  // should be an integer
        return (x - (long)x) < 1e-14;
    }
}
