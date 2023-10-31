Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def countSort(arr):
...     output = [0 for i in range(256)]
...     count = [0 for i in range(256)]
...     ans = ["for_in arr"]
...     for i in arr:
...         count[ord(i)] += 1
...     for i in range(256):
...         count[i] += count[i-1]
...     for i in range(len(arr)):
...         out[count[ord(arr[i])]-1] = arr[i]
...         count[ord(arr[i])] -= 1
...     for i in range(len(arr)):
...         ans[i] = output[i]
...         return ans
...     arr = "geeksforgeeks"
...     ans = countSort(arr)
...     print("Sorted character array is %s" %(".join(ans)"))
... 
...     
>>> 
