import sys

class Link(object):

  #initialize data members of Link class
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

  #return data of current link as string
  def __str__(self):
    return str(self.data)

class CircularList(object):

  #initialize data member of CircularList class
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    newLink = Link(data)

    #if inserting into empty list, make data first link and link to itself
    if self.first == None:
      self.first = newLink
      self.first.next = self.first
      return None

    current = self.first

    #find last link, link newLink to it and to first link
    while current.next != self.first:
      current = current.next
    current.next = newLink
    newLink.next = self.first

    return None

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.first
    if current == None: return None

    while current.data != data:
      if current.next == self.first: return None
      else: current = current.next

    return current

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    current = self.first
    previous = self.first
    #if list is empty, return None
    if current == None: return None

    #if list is length 1, empty list
    if current.next == current:
      self.first = None
      return current.data

    #search for link to delete
    while current.data != data:
      if current.next == self.first: return None
      else:
        previous = current

      current = current.next

    #delete first link
    if current == self.first:
      delete = self.first
      while current.next != self.first:
        current = current.next
      self.first = self.first.next
      current.next = self.first
      return delete.data
    #delete other links
    else: previous.next = current.next

    return current.data

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    current = self.find(start)

    #countdown to n, iterate through list
    while n > 1:
      current = current.next
      n -= 1
    #delete current link
    newStart = current.next
    return self.delete(current.data), newStart

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  #create string in list format
  def __str__ ( self ):
    if self.first == None:
      return "[]"
    current = self.first
    lis = "["
    while current.next != self.first:
      lis += str(str(current))
      lis += ", "
      current = current.next
    lis += str(str(current))
    lis += "]"
    return lis

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  list=CircularList()

  for i in range(0, num_soldiers):
    list.insert(i + 1)

  #print(list.__str__())

  #eliminate first soldier
  del_data, next=list.delete_after(start_count, elim_num)
  print(del_data)
  num_soldiers -= 1

  #continue eliminating in this fashion
  while(num_soldiers > 0):
    del_data, next = list.delete_after(next.data, elim_num)
    print(del_data)
    num_soldiers -= 1


if __name__ == "__main__":
  main()
