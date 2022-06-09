from abc import abstractmethod
import time


class NStairs:
  def __init__(self):
    self._time_dict = {}

  @property
  def time_dict(self):
    return self._time_dict

  def solve(self, n):
    start = time.time()
    n_ways = self._solve(n)
    end = time.time()
    self._time_dict.update({n: end - start})
    #print("Algorithm '{}' found {} ways in {} seconds".format(type(self).__name__, n_ways, self._time))

  @abstractmethod
  def _solve(self, n):
    raise NotImplemented('Must implement in derived classes.')

    
class Recursive(NStairs):
  def __init__(self):
    super().__init__()
    print("Solving the N Stairs problem using recursion.")
  
  def _solve(self, n):
    if n == 0 or n == 1:
      return 1
    return self._solve(n-1) + self._solve(n-2)
  
  
class NonRecursive(NStairs):
  def __init__(self):
    super().__init__()
    print('Solving the N Stairs problem without using recursion.')

  def _solve(self, n):
    sol = [1, 1]
    for i in range(2, n + 2):
      sol.append(sol[i-1] + sol[i-2])
    return sol[n]

  
class RecursiveMemoized(NStairs):
  def __init__(self):
    super().__init__()
    print('Solving the N Stairs problem using recursion and memoization.')

  def _solve(self, n):
    sol = [1, 1] + [None] * (n - 1)
    return self._num_ways(n, sol)

  def _num_ways(self, n, sol):
    if sol[n] is None:
      sol[n] = self._num_ways(n-1, sol) + self._num_ways(n-2, sol)
    return sol[n]
