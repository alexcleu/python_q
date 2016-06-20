from sets import Set

def question1(first_str,second_str):
  """ Given Two strings, determine whether anagram of t is a substring of
  s.

  Args:
    first_str: Primary string to check whether the substring exists in itself
    second_str: Substring to check whether it exists in the first_str

  Returns:
    Boolean for whether second_str exists within the first_str.
  """

  if first_str is None:
      return None

  if second_str in first_str:
    return True
  else:
    return False

print "This is question 1 test cases:"
assert question1("alexleu","al") == True
# Output is True.
assert question1("","df") == False
# Output is False.
assert question1(None,None) == None
# Output is None.


def question2(string):
  """ Given a string a, find the longest palindromic
  substring contained in an a

  Args:
    string: String that is orignally inserted.

  Returns:
    results(str): Longest palindromic substring.
  """

  if string == "":
      return string

  # If the length is less than or equal to two, the palindrome is the string
  # itself.
  length = len(string)
  if length <= 2:
    if length in (1, 2):
      return string
    else:
      return ""

  result = ""

  # Loop to check each combinations of strings.
  # Check the first index all the way to the end.
  for i in range(0, length):
    palindrome = SearchForPalindrome(string, i, i)
    if len(palindrome) > len(result):
      result = palindrome
    palindrome = SearchForPalindrome(string, i, i+1)
    if len(palindrome) > len(result):
      result = palindrome
  return result

def SearchForPalindrome(string, start, end):
  while (start >= 0 and end < len(string) and string[start] == string[end]):
    start -=1
    end +=1
  return string[start+1:end]

print "This is question 2 test cases:"
assert question2("HITHERE") == "ERE"
# Output is ERE.
assert question2("") == ""
# Output is ""
assert question2("LKJFOEWJOFJOWIFJOWJEJFKDLSJLF:JSFJSFLKJSLCJIOWEJFOIJFPE") == "JEJ"
# Output is JEJ.

ADJACENT_LIST_STRUCTURED = {'A':[('B',2),('C',8)],'B':[('A',2),('C',5)],'C':[('B',5), ('A', 8)]}
def question3(graph):
  """ Providing a graph, show the minimum spanning tree of the total weight.

  Args:
    graph: Dict that is a representation of the nodes connection.

  Return:
    Dict for the shortest path.
  """
  if not graph:
      return None
  if type(graph) is not dict:
      return "Input is not a dictionary."
  # Start off for the for the first indexes. Look for the shortest path of way.
  shortest_path = {}
  checked_vertex = Set()
  for vertex in graph:
    weight = None
    for adj in graph[vertex]:
      if (weight is None or adj[1] < weight) and adj[0] not in checked_vertex:
        weight = adj[1]
        shortest_path[vertex] = [adj]
        checked_vertex.add(adj[0])
  return shortest_path

print "This is question 3 test cases:"
assert question3(ADJACENT_LIST_STRUCTURED) == {'A': [('B', 2)], 'C': [('A', 8)], 'B': [('C', 5)]}
assert question3({}) == None
assert question3([1, 2, 3]) == "Input is not a dictionary."

TREE_LIST = [[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]]
ROOT_INT = 3
CHILD_1 = 1
CHILD_2 = 4

def TreeLevelOutputTuple(tree, root_integer, child, level):
    """ Return tuple for each level of the tree is in, and the value on top.

    Args:
      tree: tree: represented as matrix
      root_integer: Non negative integer
      level: The level the tree is currently in.
    """
    if root_integer == child:
        return 0, None
    i = 0
    for node in tree:
      if node[child] == 1 and i == root_integer:
        return level, i
      elif node[child] == 1:
        level += 1
        return TreeLevelOutputTuple(tree, i, child, level)
      else:
        pass
      i +=1

def question4(tree, root_integer, child_1, child_2):
  """ Find the least common ancestor between two nodes on a binary search tree,
  and find the farthest node that is common for both.
  Args:
    tree: tree represented as matrix
    root_integer: Non negative integer represents the root.
    child_1: First Node in the particular order.
    child_2: Second node that is checked by the tools.

  Returns:
    Output of the ancestral node.
  """

  if type(tree) is not list:
      return None
  child_1_level = TreeLevelOutputTuple(tree, root_integer, child_1, 1)
  child_2_level = TreeLevelOutputTuple(tree, root_integer, child_2, 1)
  # After finding out the level ground on each node, determine the common
  if child_1_level[0] <= child_2_level[0]:
      return child_1_level[1]
  else:
      return child_2_level[1]

print "This is question 4 test cases:"
assert question4(TREE_LIST, ROOT_INT, CHILD_1, CHILD_2) == 3
# Expect output 3.
assert question4(TREE_LIST, ROOT_INT, CHILD_1, CHILD_1) == 0
# Expected output 0.
assert question4([1,2,3,4], ROOT_INT, ROOT_INT, ROOT_INT) == None
# Expected output None.

  # ancestor will be the next higher up.
def question5(ll, m):
  """ Find the element in a singly linked list that's m elements from the end.
  Args:
    ll: first node of the linked list.
    m: The number of linked list it goes through

  Returns:
    Element(str) that is m elements from the end.
  """
  counter = 1
  current = ll
  while current.next is not None:
    counter += 1
    current = current.next

  if m == 1:
      return current.data

  # Counter is the total of linked elements there are. Next is to find the
  # number of position where it is mth from the end.
  reverse_m = counter - m + 1
  if reverse_m <= 0:
      raise ValueError("Please input M size that is less than the current size.")
  next_current = ll
  second_counter = 1
  while next_current.next is not None:
    if second_counter == reverse_m:
      return next_current.data
      break
    else:
      next_current = next_current.next
      second_counter += 1


class Node(object):
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList(object):
  def __init__(self, head=None):
      self.head = head

  def tophead(self):
      return self.head

  def append(self, new_element):
      current = self.head
      if self.head:
          while current.next:
              current = current.next
          current.next = new_element
      else:
          self.head = new_element

  def display(self):
      current = self.head
      while current.next:
          print current.data
          current = current.next

node = Node("Come Together")
node2 = Node("Yesterday")
node3 = Node("Blackbirds")
node4 = Node("Hey Jude")
node5 = Node("Yellow Submarine")

test = LinkedList(node)
test.append(node2)
test.append(node3)
test.append(node4)
test.append(node5)

test.tophead()

print "This is question 5 test cases:"
assert question5(test.tophead(), 4) == "Yesterday"
# Output is Yesterday.
assert question5(test.tophead(), 3) == "Blackbirds"
# Output is Blackbirds.
assert question5(test.tophead(), 0) == None
# Output is None.
