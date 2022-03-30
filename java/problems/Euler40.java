package problems;

public class Euler40 {
    /*
    Champernowne's constant
    Problem 40

    An irrational decimal fraction is created by concatenating the positive integers:

        0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.
    If d_n represents the nth digit of the fractional part, find the value of the following expression.

        d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
     */
    public long solution() {
        StringBuilder champernowne = new StringBuilder();
        for (int i = 1; champernowne.length() < 1_000_000; i++) {
            champernowne.append(i);
        }

        long product = 1;
        for (int i = 0; i <= 6; i++) {
            product *= champernowne.charAt((int)Math.pow(10, i) - 1) - '0';
        }
        return product;
    }
}
