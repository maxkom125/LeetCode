from typing import List
# Write any import statements here
def getMaxBetweenDinersCount(line_len: int, K: int) -> int:
  parts = line_len // (K + 1)
  #calculated only left gap -> mb need to add right
  if (line_len % (K + 1) < K) and (parts != 0):
      parts -= 1
  return parts

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  maxAdditionalDinersCount = 0
  S = sorted(S)
  
  maxAdditionalDinersCount += (S[0] - 1) // (K + 1)
  for i in range(len(S) - 1):
      maxAdditionalDinersCount += getMaxBetweenDinersCount(S[i+1] - S[i] - 1, K)
      
  maxAdditionalDinersCount += (N - S[-1]) // (K + 1)
  return maxAdditionalDinersCount