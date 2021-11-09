def ordered_sequential_search(a_list, item):
  pos = 0
  found = False
  stop = False
  count = 0
  while pos < len(a_list) and not found and not stop:
    if a_list[pos] == item:
       found = True
    else:
       if a_list[pos] > item:
        stop = True
       else:
        pos = pos+1
    count += 1
  return found, count

if __name__ == "__main__":
  myList=  [0, 1, 2, 8, 13, 17, 19, 32, 42]
  print(ordered_sequential_search(myList, 3))
  print(ordered_sequential_search(myList, 13))
