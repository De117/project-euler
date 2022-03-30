package problems;

public class Euler39 {
    /*
    Integer right triangles
    Problem 39

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
     */
    public long solution() {
        long bestP = 0;
        long maxNumSolutions = 0;

        for (long p = 1; p <= 1000; p++) {
            long numSolutions = 0;

            // Due to triangle inequality, c < a + b.
            for (long c = 1; c <= 2*p/3; c++) {

                // Since c is the hypotenuse, a < c and b < c.
                for (long b = 1; b < c; b++) {

                    // What's left over is a.
                    long a = p - b - c;

                    // To prevent duplicate solutions and illegal values of a,
                    // we enforce 1 ≤ a ≤ b < c.
                    if (a < 1 || a > b) continue;

                    if (a*a + b*b == c*c) {
                        numSolutions++;
                    }
                }
            }

            if (numSolutions > maxNumSolutions) {
                bestP = p;
                maxNumSolutions = numSolutions;
            }
        }
        return bestP;
    }
}
