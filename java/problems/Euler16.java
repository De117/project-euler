package problems;

import java.math.BigInteger;

public class Euler16 {

    /*
    Power digit sum
    Problem 16

    2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^(1000)?
     */
    public long solution() {
        int N = 1000;
        String s = BigInteger.TWO.pow(N).toString();

        long sum = 0;
        for (char c : s.toCharArray()) {
            sum += c - '0';
        }
        return sum;
    }
}
