package problems;

import java.util.ArrayList;

public class Euler31 {
    /*
    Coin sums
    Problem 31

    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?
     */
    public long solution() {
        // You'll notice that this looks a lot like recursion.
        // In fact, it _is_ recursion, just to a known/fixed depth.
        //
        // We start filling the "bag" with larger coins -- as many as we can
        // fit -- and the rest must be filled with smaller coins, if possible.
        // (In this case, it's always possible, but you can easily imagine the
        // same problem, but without any 1p coins available.
        //
        // NOTE: reversing the coin order is slower, but works just as well.

        long count = 0;  // "how many ways"
        int sum = 0;

        int MAX = 200;  // pence

        for (int i_200 = 0; i_200 <= MAX/200; i_200++) {
            int sum_200 = sum + i_200 * 200;
            if (sum_200 >= MAX) { if (sum_200 == MAX) count++; break; }

            for (int i_100 = 0; i_100 <= MAX/100; i_100++) {
                int sum_100 = sum_200 + i_100 * 100;
                if (sum_100 >= MAX) { if (sum_100 == MAX) count++; break; }

                for (int i_50 = 0; i_50 <= MAX/50; i_50++) {
                    int sum_50 = sum_100 + i_50 * 50;
                    if (sum_50 >= MAX) { if (sum_50 == MAX) count++; break; }

                    for (int i_20 = 0; i_20 <= MAX/20; i_20++) {
                        int sum_20 = sum_50 + i_20 * 20;
                        if (sum_20 >= MAX) { if (sum_20 == MAX) count++; break; }

                        for (int i_10 = 0; i_10 <= MAX/10; i_10++) {
                            int sum_10 = sum_20 + i_10 * 10;
                            if (sum_10 >= MAX) { if (sum_10 == MAX) count++; break; }

                            for (int i_5 = 0; i_5 <= MAX/5; i_5++) {
                                int sum_5 = sum_10 + i_5 * 5;
                                if (sum_5 >= MAX) { if (sum_5 == MAX) count++; break; }

                                for (int i_2 = 0; i_2 <= MAX/2; i_2++) {
                                    int sum_2 = sum_5 + i_2 * 2;
                                    if (sum_2 >= MAX) { if (sum_2 == MAX) count++; break; }

                                    // We could do a loop here, like so:
                                    //
                                    // for (int i_1 = 0; i_1 <= MAX/1; i_1++) {
                                    //     int sum_1 = sum_2 + i_1 * 1;
                                    //     if (sum_1 >= MAX) { if (sum_1 == MAX) count++; break; }
                                    // }
                                    //
                                    // But it's not needed in this case, since
                                    // we can trivially fill the rest with ones.
                                    int i_1 = MAX - sum_2;
                                    count++;
                                }
                            }
                        }
                    }
                }
            }
        }
        return count;

    }

    // Here's a (somewhat slower) proper recursive solution.

    private long count = 0;
    private int coinSizes[] = {200, 100, 50, 20, 10, 5, 2, 1};

    private void recursive(int coinIndex, int capacity) {
        // In general, the base case for recursion is overshooting.
        //
        //     if (coinIndex == 8) return;
        //
        // But we have 1p coins as last. They can trivially fill out
        // the remaining space.
        if (coinIndex == 7) {
            this.count++;
            return;
        }

        int coinSize = this.coinSizes[coinIndex];

        // Try to fit in as many coins of this size as you can
        for (int i = 0; i <= capacity/coinSize; i++) {
            int remaining = capacity - i * coinSize;
            if (remaining == 0) {
                // It fits exactly, no more room.
                this.count++;
                return;
            } else {
                // There's space left; fill it with smaller coins (if possible)
                recursive(coinIndex + 1, remaining);
            }
        }
    }
}
