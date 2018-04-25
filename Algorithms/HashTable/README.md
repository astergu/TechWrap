A hash table is a data structure used to store keys, optionally, with corresponding values. Inserts, deletes and lookups run in *O(1)* time on average.

```python
# example hash function
def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)
```

## Practial Tips

- Hash tables have the **best theoretical and real-world performance** for lookup, insert and delete. Each of these operations has *O(1)* time complexity. 
- Consider using a hash code as a **signature** to enhance performance, e.g., to filter out candidates.
- Sometimes you'ill need a *multimap*, i.e., a map that contains multiple values for a single key, or a bi-directional map. If the language's stand libraries do not provide the functionality you need, learn how to implement a multimap using lists as values, or find a **third party library** that has a multimap.

### Is An Anonymous Letter Constructible?

Write a program which takes text for an anonymous letter and text for a magazine and determines if it is possible to write the anonymous letter using the magzaine. The anonymous letter can be written using the magazine if for each character in the anonymous letter, the number of times it appears in the anonymous letter is no more than the number of times it appears in the magazine.

```python
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in 
    # char_frequency_for_letter
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched.
                    return True

    # Empty char_frequency_for_letter means every char in letter_text
    # can be covered by a character in magazine_text.
    return not char_frequency_for_letter

def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))
```



## Applications

*Anagrams* are popular word play puzzles, whereby rearranging letters of one set of words, you get another set of words. For example, "eleven plus two" is an anagram for "twelve plus one". Suppose you were asked to **write a program that takes as input a set of words and returns groups of anagrams for those words. Each group must contain at least two words**. For example, if the input is "debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"
then there are three groups of anagrams: (1) "debitcard", "badcredit"; (2) "elvis", "lives", "levis"; (3) "silent", "listen".

- **Whether one word is anagram of another**.
```python
def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]
```
Time complexity *O(nmlogm)*.


