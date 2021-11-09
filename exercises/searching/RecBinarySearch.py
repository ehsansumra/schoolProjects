
def binary_search(a_list, item, count=0):
    if len(a_list) == 0:
       return False, count
    else:
       midpoint = len(a_list) // 2
       count+=1
       if a_list[midpoint] == item:
         return True, count
       else:
         if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item, count)
         else:
            return binary_search(a_list[midpoint + 1:], item,count)

        
if __name__ == "__main__":
   myList =  [0, 1, 2, 8, 13, 17, 19, 32, 42]
   print(binary_search(myList, 3))
   print(binary_search(myList, 13))

