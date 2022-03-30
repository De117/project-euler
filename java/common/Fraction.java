package common;

import java.math.BigInteger;
import java.util.Objects;

public class Fraction implements Comparable<Fraction> {
    public long numerator;
    public long denominator;
    public Fraction simplified;  // the simplified version of this fraction

    public Fraction(long numerator, long denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
        if (denominator == 0) {
            throw new IllegalArgumentException("Denominator cannot be zero!");
        }

        // Simplify
        long gcd = BigInteger.valueOf(numerator).gcd(BigInteger.valueOf(denominator)).longValueExact();
        if (gcd != 1) {
            this.simplified = new Fraction(numerator / gcd, denominator / gcd);
        } else {
            this.simplified = this;
        }
    }

    public double toDouble() {
        return this.simplified.numerator / (double)this.simplified.denominator;
    }

    public int compareTo(Fraction f) {
        return Double.compare(this.toDouble(), f.toDouble());
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Fraction fraction = (Fraction) o;
        return this.simplified.numerator == fraction.simplified.numerator &&
                this.simplified.denominator == fraction.simplified.denominator;
    }

    @Override
    public int hashCode() {
        return Objects.hash(numerator, denominator);
    }

    public String toString() {
        return String.format("Fraction(numerator=%d, denominator=%d)", this.numerator, this.denominator);
    }
}