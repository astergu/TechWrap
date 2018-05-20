There is no concept of an unsigned shift in Python, since integers have infinite precision.

- Be very comfortable with the **bitwise operators**, particularly XOR.
- Know fast ways to **clear the lowermost set bit** (and set the lowermost 0, get its index, etc.)
- Understand **signedness** and its implications to **shifting**.
- Consider using a **cache** to accelerate operations by using it to brute-force small inputs.
- *x & 1*表示取数字的奇偶数。 

## Questions
- [x] The [parity of a binary word](ParityOfWord.py) is 1 if the number of 1s in the word is odd;
otherwise, it's 0. How would you compute the parity of a very large number of 64-bit words?
    - Explanation: `x & ~(x - 1)` isolates the lowest bit that is 1,  `x & (x - 1)` replaces the lowest
    bit that is 1 with 0.
    - Exercise:
        - Right propagate the rightmost set bit in x, e.g. turns (01010000) to (01011111).
        - Compute x modulo a power of two, e.g., returns 13 for 77 mod 64.
        - Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8,..., false for all other values.
