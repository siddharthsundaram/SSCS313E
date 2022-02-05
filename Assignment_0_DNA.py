# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
  listSub = []
  longest = 0
  for i in range(len(s1)):
    for j in range(len(s1)+1):
      if s1[i:j+1] in s2:
        listSub.append(s1[i:j+1])

  for k in range(len(listSub)):
    if len(listSub[k]) > longest:
        longest = len(listSub[k])
  newList = []
  for l in range(len(listSub)):
    if len(listSub[l]) == longest:
      newList.append(listSub[l])
  final = list(set(newList))
  final.sort()
  if len(final[0]) > 0:
    for q in final:
      if "\n" not in q:
        print(q)
      else:
        print("No Common Sequence Found")
  else:
    print("No Common Sequence Found")
  print()

def main():
  m = int(input())
  for y in range(0, m):
    str1 = input()
    str2 = input()
    longest_subsequence(str1, str2)

if __name__ == "__main__":
  main()