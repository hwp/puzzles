#!/usr/bin/env python

import math

# test if the game will end
def test(n):
  # Daphne
  sdif = [set([(i, i + m) for i in range(1, n - m + 1)]) for m in range(0, n)]
  assert sum(map(len, sdif)) == n * (n + 1) / 2;

  # Max
  smax = [set([(i, m) for i in range(1, m + 1)]) for m in range(1, n + 1)]
  assert sum(map(len, smax)) == n * (n + 1) / 2;

  # Mindy
  smin = [set([(m, i) for i in range(m, n + 1)]) for m in range(1, n + 1)]
  assert sum(map(len, smin)) == n * (n + 1) / 2;

  # Sam
  ssum = [set([(i, m - i) for i in range(max(1, m - n), m / 2 + 1)]) for m in range(2, 2 * n + 1)]
  assert sum(map(len, ssum)) == n * (n + 1) / 2;
  
  # Tim
  spro = {}
  for i in range(1, n + 1):
    for j in range(i, n + 1):
      p = i * j;
      if p not in spro:
        spro[p] = set()
      spro[p].add((i, j))
  assert sum(map(len, spro.values())) == n * (n + 1) / 2;

  sets = sdif + smax + smin + ssum + spro.values()

  flag = True
  while len(sets) > 0:
    # the set of pairs to be removed
    torm = reduce(lambda x, y: x.union(y), [s for s in sets if len(s) == 1], set())
    if len(torm) == 0:
      # no more modification can be done
      # that means no one is 100% sure what the answer is
      flag = False
      break
    # remove the pairs from sets
    sets[:] = [s - torm for s in sets if len(s) > 1]
    # remove empty sets
    sets[:] = [s for s in sets if len(s) > 0]

  return flag

def main():
  n = 2;
  while test(n):
    n += 1
  print n

if __name__ == "__main__":
  main()

