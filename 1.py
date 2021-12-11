class temp:
  def __init__(self, arr, n):
    self.arr = arr;
    self.n = n;
  def getMin(self, arr, n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    print(f"Minimum element of array is : {res}")
  def getMax(self, arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    print(f"Maximum element of array is : {res}")

arr = [-25, -10, -7, -3, 2, 4, 8, 10];
n = len(arr);
t = temp(arr,n);
t.getMin(arr,n);
t.getMax(arr,n);