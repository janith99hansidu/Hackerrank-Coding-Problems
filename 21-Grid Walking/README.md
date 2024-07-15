---
# 1-Dimensional Grid Walking Problem

## Problem Description
You are positioned on a 1-dimensional grid at position \( x \). The grid has positions ranging from 0 to \( D-1 \). In each step, you can move one position ahead or behind. Compute the number of ways to take exactly \( m \) steps without leaving the grid.

### Example
- **Starting Position:** \( x = 2 \)
- **Grid Size:** \( D = 5 \)
- **Number of Steps:** \( m = 3 \)

## Dynamic Programming Approach

### DP Table Initialization
We use a DP table where `dp[steps][position]` represents the number of ways to reach `position` with `steps` steps.

```plaintext
        Position: 0  1  2  3  4
-------------------------------
Steps: 0    |    0  0  1  0  0
Steps: 1    |    0  1  0  1  0
Steps: 2    |    1  0  2  0  1
Steps: 3    |    0  3  0  3  0
```
---