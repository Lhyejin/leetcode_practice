# 605. Can Place Flowers

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/can-place-flowers/

## Problem

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`s and `1`s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

**Example 1:**
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

**Example 2:**
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

## Approach

Use a greedy approach, scanning from left to right and planting a flower whenever possible.
- If the current plot is `0` and both neighbors are `0` (or out of bounds), plant a flower and increment `count`
- Return `true` if `count >= n` at the end

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
