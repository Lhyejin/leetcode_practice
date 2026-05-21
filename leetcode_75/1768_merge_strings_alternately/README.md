# 1768. Merge Strings Alternately

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/merge-strings-alternately/

## Problem

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Example 1:**
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

**Example 2:**
```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```

**Example 3:**
```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

## Approach

Use two pointers to traverse each string alternately.
- Use two pointers `i` and `j` to iterate through `word1` and `word2` simultaneously
- While both pointers are within bounds, append characters alternately
- Append the remaining characters of the longer string at the end

**Time Complexity:** O(n + m)  
**Space Complexity:** O(n + m)
