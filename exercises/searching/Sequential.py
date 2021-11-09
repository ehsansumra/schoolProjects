def sequential_search(a_list, item):
  pos = 0
  found = False
  count = 0
  while pos < len(a_list) and not found:
    if a_list[pos] == item:
       found = True
    else:
        pos = pos+1
    count += 1
  return found, count

if __name__ == "__main__":

  myList = [1, 2, 32, 8, 17, 19, 42, 13, 0]
  print(sequential_search(myList, 3))
  print(sequential_search(myList, 13))
