# 1431. Kids With the Greatest Number of Candies

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

## Problem

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `false` otherwise.

**Example 1:**
```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
```

**Example 2:**
```
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
```

**Example 3:**
```
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

## Approach

Find the maximum value in the candies array, then check if each kid can reach or exceed it after receiving `extraCandies`.
- Pre-compute the current maximum using `max(candies)`
- Use a list comprehension to check the condition for each element and return a boolean list

**Time Complexity:** O(n)  
**Space Complexity:** O(n)
