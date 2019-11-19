
import unittest




class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def addNode(self,data):
        node=Node(data)

        if self.next == None:
            self.next = node

        else:
            while self.next != None:
                self = self.next

            self.next = node



    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    # """

    newLL=None

    head= None
    tail= None


    while l1 != None or l2 != None:

        if l1 == None:
            num_l1=0
        else:
            num_l1=l1.data

        if l2 == None:
            num_l2=0
        else:
            num_l2=l2.data


        nodeSum = num_l1 + num_l2
        

        if newLL== None:
            newLL=Node(nodeSum)
            head=newLL
            tail=newLL

        else:

            tail.next= Node(nodeSum)
            tail = tail.next
   

        l1 = l1.next
        l2 = l2.next

    return newLL


   

l1 = Node(3, Node(2, Node(1)))
l2 = Node(4, Node(3, Node(2)))



class TestFunction(unittest.TestCase):
    def test_addll(self):
        self.assertEqual(add_linked_lists(l1,l2).as_rev_string(),"357")


if __name__=='__main__':
    unittest.main()