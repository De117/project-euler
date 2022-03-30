package problems;

public class Euler28 {
    /*
    Number spiral diagonals
    Problem 28

    Starting with the number 1 and moving to the right in a
    clockwise direction a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
     */
    public long solution() {
        // The spiral above is: 1, 3, 5, 7, 9, 13, 17, 21, 25.
        // Basically, the center number, and everything on the diagonals.
        // We see that the progression of offsets is:
        // 2, 2, 2, 2, (now into the next "onion layer") 4, 4, 4, 4, (new layer again) ...
        //
        // Every new layer increases the offset between neighbouring numbers by 2.
        int N = 1001;
        int numLayers = (N - 1) / 2;


        long i = 1;     // central element
        long sum = i;
        long offset = 2;
        // So, we just go through the layers and sum the diagonal elements up.
        // The loop doesn't cover the central element, so we put it in the sum initially.
        for (int layer = 0; layer < numLayers; layer++) {
            i += offset; sum += i;
            i += offset; sum += i;
            i += offset; sum += i;
            i += offset; sum += i;
            offset += 2;
        }
        return sum;
    }
}
