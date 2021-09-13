#!/usr/bin/env python3

import sys

nums = []
for num in sys.stdin:
  nums.append(int(num.strip()))
print (f'Mean: {sum(nums) / len(nums):.1f}')

nums = sorted(nums)
if len(nums) % 2 != 0:
  index = len(nums) // 2
  print (f'Median: {nums[index]:.1f}')
else:
  first_i = len(nums) // 2 - 1
  sec_i = len(nums) // 2
  print (f'Median: {((nums[first_i] + nums[sec_i]) / 2):.1f}')
