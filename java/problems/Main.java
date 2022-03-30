package problems;

import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        long euler_1 = new Euler1().solution(); System.out.printf("Euler 1: %d\n", euler_1); assert euler_1 == 233168L;
        long euler_2 = new Euler2().solution(); System.out.printf("Euler 2: %d\n", euler_2); assert euler_2 == 4613732L;
        long euler_3 = new Euler3().solution(); System.out.printf("Euler 3: %d\n", euler_3); assert euler_3 == 6857L;
        long euler_4 = new Euler4().solution(); System.out.printf("Euler 4: %d\n", euler_4); assert euler_4 == 906609L;
        long euler_5 = new Euler5().solution(); System.out.printf("Euler 5: %d\n", euler_5); assert euler_5 == 232792560L;
        long euler_6 = new Euler6().solution(); System.out.printf("Euler 6: %d\n", euler_6); assert euler_6 == 25164150L;
        long euler_7 = new Euler7().solution(); System.out.printf("Euler 7: %d\n", euler_7); assert euler_7 == 104743L;
        long euler_8 = new Euler8().solution(); System.out.printf("Euler 8: %d\n", euler_8); assert euler_8 == 23514624000L;
        long euler_9 = new Euler9().solution(); System.out.printf("Euler 9: %d\n", euler_9); assert euler_9 == 31875000L;
        long euler_10 = new Euler10().solution(); System.out.printf("Euler 10: %d\n", euler_10); assert euler_10 == 142913828922L;
        long euler_11 = new Euler11().solution(); System.out.printf("Euler 11: %d\n", euler_11); assert euler_11 == 70600674L;
        long euler_12 = new Euler12().solution(); System.out.printf("Euler 12: %d\n", euler_12); assert euler_12 == 76576500L;
        long euler_13 = new Euler13().solution(); System.out.printf("Euler 13: %d\n", euler_13); assert euler_13 == 5537376230L;
        long euler_14 = new Euler14().solution(); System.out.printf("Euler 14: %d\n", euler_14); assert euler_14 == 837799L;
        long euler_15 = new Euler15().solution(); System.out.printf("Euler 15: %d\n", euler_15); assert euler_15 == 137846528820L;
        long euler_16 = new Euler16().solution(); System.out.printf("Euler 16: %d\n", euler_16); assert euler_16 == 1366L;
        long euler_17 = new Euler17().solution(); System.out.printf("Euler 17: %d\n", euler_17); assert euler_17 == 21124L;
        long euler_18 = new Euler18().solution(); System.out.printf("Euler 18: %d\n", euler_18); assert euler_18 == 1074L;
        long euler_19 = new Euler19().solution(); System.out.printf("Euler 19: %d\n", euler_19); assert euler_19 == 171L;
        long euler_20 = new Euler20().solution(); System.out.printf("Euler 20: %d\n", euler_20); assert euler_20 == 648L;
        long euler_21 = new Euler21().solution(); System.out.printf("Euler 21: %d\n", euler_21); assert euler_21 == 31626L;
        long euler_22 = new Euler22().solution(); System.out.printf("Euler 22: %d\n", euler_22); assert euler_22 == 871198282L;
        long euler_23 = new Euler23().solution(); System.out.printf("Euler 23: %d\n", euler_23); assert euler_23 == 4179871L;
        long euler_24 = new Euler24().solution(); System.out.printf("Euler 24: %d\n", euler_24); assert euler_24 == 2783915460L;
        long euler_25 = new Euler25().solution(); System.out.printf("Euler 25: %d\n", euler_25); assert euler_25 == 4782L;
        long euler_26 = new Euler26().solution(); System.out.printf("Euler 26: %d\n", euler_26); assert euler_26 == 983L;
        long euler_27 = new Euler27().solution(); System.out.printf("Euler 27: %d\n", euler_27); assert euler_27 == -59231L;
        long euler_28 = new Euler28().solution(); System.out.printf("Euler 28: %d\n", euler_28); assert euler_28 == 669171001;
        long euler_29 = new Euler29().solution(); System.out.printf("Euler 29: %d\n", euler_29); assert euler_29 == 9183L;
        long euler_30 = new Euler30().solution(); System.out.printf("Euler 30: %d\n", euler_30); assert euler_30 == 443839L;
        long euler_31 = new Euler31().solution(); System.out.printf("Euler 31: %d\n", euler_31); assert euler_31 == 73682L;
        long euler_32 = new Euler32().solution(); System.out.printf("Euler 32: %d\n", euler_32); assert euler_32 == 45228L;
        long euler_33 = new Euler33().solution(); System.out.printf("Euler 33: %d\n", euler_33); assert euler_33 == 100L;
        long euler_34 = new Euler34().solution(); System.out.printf("Euler 34: %d\n", euler_34); assert euler_34 == 40730L;
        long euler_35 = new Euler35().solution(); System.out.printf("Euler 35: %d\n", euler_35); assert euler_35 == 55L;
        long euler_36 = new Euler36().solution(); System.out.printf("Euler 36: %d\n", euler_36); assert euler_36 == 872187L;
        long euler_37 = new Euler37().solution(); System.out.printf("Euler 37: %d\n", euler_37); assert euler_37 == 748317L;
        long euler_38 = new Euler38().solution(); System.out.printf("Euler 38: %d\n", euler_38); assert euler_38 == 932718654L;
        long euler_39 = new Euler39().solution(); System.out.printf("Euler 39: %d\n", euler_39); assert euler_39 == 840L;
        long euler_40 = new Euler40().solution(); System.out.printf("Euler 40: %d\n", euler_40); assert euler_40 == 210L;
        long euler_41 = new Euler41().solution(); System.out.printf("Euler 41: %d\n", euler_41); assert euler_41 == 7652413L;
        long euler_42 = new Euler42().solution(); System.out.printf("Euler 42: %d\n", euler_42); assert euler_42 == 162L;
        long euler_43 = new Euler43().solution(); System.out.printf("Euler 43: %d\n", euler_43); assert euler_43 == 16695334890L;
        long euler_44 = new Euler44().solution(); System.out.printf("Euler 44: %d\n", euler_44); assert euler_44 == 5482660L;
        long euler_45 = new Euler45().solution(); System.out.printf("Euler 45: %d\n", euler_45); assert euler_45 == 1533776805L;
        long euler_46 = new Euler46().solution(); System.out.printf("Euler 46: %d\n", euler_46); assert euler_46 == 5777L;
        long euler_47 = new Euler47().solution(); System.out.printf("Euler 47: %d\n", euler_47); assert euler_47 == 134043L;
        long euler_48 = new Euler48().solution(); System.out.printf("Euler 48: %d\n", euler_48); assert euler_48 == 9110846700L;
        long euler_49 = new Euler49().solution(); System.out.printf("Euler 49: %d\n", euler_49); assert euler_49 == 296962999629L;
        long euler_50 = new Euler50().solution(); System.out.printf("Euler 50: %d\n", euler_50); assert euler_50 == 997651L;

        // long startTime = System.nanoTime();
        // int N = 1;
        // for (int i=0; i<N; i++) {
        //     long e44 = (new Euler44()).solution();
        // }
        // long endTime = System.nanoTime();
        // double duration = (endTime - startTime) / 1e3 / N;
        // System.out.printf("%f microseconds per iteration\n", duration);
    }
}
