# string formatting
nums = list(range(5))
msg = "Numbers: {0} {1} {2} {3} {4}".format(nums[0],nums[1],nums[2],nums[3],nums[4])
print(msg)
print("{0}{1}{0}".format("abra","cad"))