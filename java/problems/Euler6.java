package problems;

public class Euler6 {

    /*
    Sum square difference
    Problem 6

    The sum of the squares of the first ten natural numbers is,
        1² + 2² + ... + 10² = 385

    The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)² = 55² = 3025

    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
     */
    public long solution() {
        int N = 100;
        int sum = 0;
        int sumOfSquares = 0;
        for (int i=1; i <= N; i++) {
            sum += i;
            sumOfSquares += i*i;
        }
        return (sum*sum) - sumOfSquares;
    }
}
