#include<stdio.h>

long sum_of_squares(long N) {
    long sum = 0;
    for(int i=1; i<=N; i++)
        sum += i*i;
    return sum;
}

long square_of_sum(long N) {
    long sum = 0;
    for(int i=1; i<=N; i++)
        sum += i;
    return sum*sum;
}

int main() {
    printf("%ld\n", square_of_sum(100) - sum_of_squares(100));
    return 0;
}
