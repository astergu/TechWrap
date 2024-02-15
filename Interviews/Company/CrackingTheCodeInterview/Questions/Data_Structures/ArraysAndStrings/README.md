Please note that array questions and string questions are often interchangable.

## Hash Tables

### Hash Table Implementation

In this simple implementation, we use an array of linked lists and a hash code function. To insert a key and value, we do the following:

1. First, compute the key's hash code, which will usually be an **int** or **long**. Note that two different keys could have the same hash code, as there may be an infinite number of keys and a finite number of ints. 
2. Then, map the hash code to an index in the array. This could be done with something like **hash(key) / array_length**. Two different hash codes could, of course, map to the same index.
3. At this index, there is a linked list of keys and values. Store the key and value in this index. We must use a linked list because of collisions: you could have two different keys with the same hash code, or two different hash codes that map to the same index. 


If the number of collisions is very high, the worse case runtime is *O(N)*, where N is the number of keys. However, we generally assume a good implementation that keeps collisions to a minimu, in which case the lookup time is *O(1)*.

Alternatively, we can implement the hash table with a balanced binary search tree. This gives us an *O(log N)* lookup time. The advantage of this is potentially using less space, since we no longer allocate a large array. We can also iterate through the keys in order, which can be useful sometimes. 

### ArrayList & Resiable Arrays

When you need an array-like data structure that offers dynamic resizing, you would usually use an ArrayList. An ArrayList is an array that resizes itself as needed while still providing *O(1)* access. A typical implementation is that when the array is full, the array doubles in size. Each doubling takes *O(n)* time, but happens so rarely that its amortized insertion time is still *O(1)*.

### StringBuilder

Imagine you were concatenating a list of strings, what would the running time of this code be?

```python
def joinWords(words):  # list of words
    sentence = ""
    for w in words:
        sentence += w
    return sentence
```

This implementation is not efficient, because on each concatenation, a new copy of the string ic created, and the two strings are copied over, character by character. The total time is *O(x + 2x + .... + nx) = O(xn<sup>2</sup>)*. In Jave, they use **StringBuffer** to avoid this problem. **StringBuffer** simply creates a resizable array of all the string, copying them back to a string only when necessary.

```java
String joinWords(String[] words) {
    StringBuilder sentence = new StringBuilder();
    for (String w: words) {
        sentence.append(w);
    }
    return sentence.toString();
}
```

Here is python verion:

```python
def joinWords(words):  # list of words
    sentence = []
    for w in words:
        sentence.append(w)
    return ' '.join(sentence)
```

A good exercise to practice string, arrays, and general data structures is to implement your own version of **StringBuilder**, **HashTable** and **ArrayList**. 

**Additional Reading**: [*Hash Table Collision Resolution*](../../AdvancedTopics/HashTableCollisionResolution.md), [*Rabin-Karp Substring Search*](../../AdvancedTopics/RabinKarpSubstringSearch.md).


## Interview Questions

1. **Is Unique**: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

2. **Check Permutation**: Given two strings, write a method to decide if one is a permutation of the other.

3. **URLify**: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

```
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
```

4. **Palindrome Permutations**: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

```
EXAMPLE
Input: Tact Coa
Output: True (permuations: "taco cat", "atco cta", etc.)
```

5. **One Away**: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

```
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
```

6. **String Compression**: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string *aabcccccaaa* would become *a2b1c5a3*. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

7. **Rotate Matrix**: Given an image represented by an *N \* N* matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

8. **Zero Matrix**: Write an algorithm such that if an element in an *M \* N* matrix is 0, its entire row and column are set to 0.

9. **String Rotation**: Assume you have a method is *Substring* which checks if one word is a substring of another. Given two strings, *s1* and *s2*, write code to check if *s2* is a rotation of *s1* using only one call to *isSubstring* (e.g., "waterbottle" is a rotation of "erbottlewat").

### Additional Questions

*Object-Oriented Design* (#7.12), *Recursion* (#8.3), *Sorting and Searching* (#10.9), *C++* (#12.11), *Moderate Problems* (#16.8, #16.17, #16.22), *Hard Problems* (#17.4, #17.7, #17.13, #17.22, #17.26).
