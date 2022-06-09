#import Recursive, NonRecursive, RecursiveMemoized
import numpy as np
import matplotlib.pyplot as plt


class TestNStairs:
  def __init__(self, limit):
    self._limit = limit
    self._test_objs = [Recursive(), NonRecursive(), RecursiveMemoized()]

  def test(self):
    for n in range(1, self._limit + 1):
      #print("\nTesting for {} stairs.".format(n))
      for obj in self._test_objs:
        obj.solve(n)

    stairs_plt = {}
    for i, obj in enumerate(self._test_objs):
      if i == 0:
        #continue
        pass
      time_dict = obj.time_dict
      x = np.array(list(time_dict.keys()))
      y = np.array(list(time_dict.values()))
      plt.plot(x, y, label=type(obj).__name__)

    plt.title('N Stairs Problem')
    plt.xlabel('N Stairs')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.show()

tester = TestNStairs(20)
tester.test()
