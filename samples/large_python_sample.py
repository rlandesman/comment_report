# ----------------< Module Imports >-----------------
import unittest
import os.path
import array_list
from linked_list import *
from huffman_bits_io import *

# ----------------< Class for Leaf >-----------------
class Leaf:
    def __init__(self,ordinal,count):
        self.ordinal = ordinal
        self.count = count

    def __eq__(self, other):
        return type(other) == Leaf and self.ordinal == other.ordinal and self.count == other.count

# ----------------< Class for Node >-----------------
class Node:
    def __init__(self,count,left,right):
        self.ordinal = None
        self.count = count
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (type(other) == Node and self.left == other.left and self.right == other.right and self.count == other.count)

# ----------------< Class for Leaf Nodes >-----------------
#Root is either leaf or Node
class HuffmanTree:
    def __init__(self,root):
        self.root = root
    def __eq__(self, other):
        return type(other) == HuffmanTree and self.root == other.root
    def __repr__(self):
        return "Tree({!r})".format(self.root.count) #Using count because that will never be empty when initializing

#String -> ArrayList
#Returns an array in which the begginning positions are filled with the charachters from the text file
def txt_to_freq(inputFile):
    f=  open(inputFile, 'r')
    allLines = f.read()

    newList = array_list.empty_list()
    newList.array = [0] * 256
    newList.capacity = 256

    for x in allLines:
        temp = ord(x)
        newList.array[temp-1] += 1
        newList.size += 1
    f.close()
    return newList



# LinkedList, EmptyLinked -> LinkedList
# Returns an Array containing characters of all leaf nodes in tree
def leaf_to_string(inputTree):
   myList = inputTree
   if myList is not Node:
        yield from iterate_htree(myList.left)
        yield from iterate_htree(myList.right)

# Huffman Tree Huffman Tree -> Boolean
# A huffman node is either a Leaf or Node Object
# Compares the count of each node and returns True if a is less than b
# If the two are tied, this function returns the smaller ASCII value of the two nodes
def comes_before(a,b):
    if a.root.count < b.root.count:
        return True
    elif a.root.count > b.root.count:
        return False
    else:
        if a.root.ordinal < b.root.ordinal:
            return True #TEST
        else:
            return False

def array_to_sortedList(inputArray):
    return_list = empty_list()
    idx = 0
    for x in range(inputArray.capacity):
        idx += 1
        if inputArray.array[x] != 0:
            occurence = inputArray.array[x]
            newLeaf = Leaf(idx,occurence)
            newTree = HuffmanTree(newLeaf)
            return_list = insert_sorted(return_list,newTree,comes_before)

    return return_list

#Tree -> LinkedList (With one element as tree)
def build_tree(inputTree):
    myList = inputTree.root

    while myList.rest is not None:
        left = myList.first.root
        myList = myList.rest
        right = myList.first.root
        myList = myList.rest

        addedCount = left.count + right.count
        newNode = HuffmanTree(Node(addedCount,left,right))

        if left.ordinal > right.ordinal:
            newNode.root.ordinal = right.ordinal
        else:
            newNode.root.ordinal = left.ordinal
        myList = insert_sorted(myList,newNode,comes_before)
    return myList.first


# ----------------< Artifacts of my "Deep" Debugging >-----------------
# # print(txt_to_array())
# list_with_frequency = count_frequency(txt_to_array()) #also used for testing
# # print(list_with_frequency)
# #
# myList = array_to_sortedList(list_with_frequency)
# my_tree = HuffmanTree(myList)
# #
# print(myList)
# print(myList.first.root.ordinal)
# print(myList.rest.first.root.ordinal)
# print(myList.rest.rest.first.root.ordinal)
# print(myList.rest.rest.rest.first.root.ordinal)
# print(myList.rest.rest.rest.rest.first.root.ordinal)

#LinkedList -> Generator Obj
def iterate_htree(my_tree,string = ""):
   if my_tree is not None:
       if isinstance(my_tree,Leaf):
           yield (chr(my_tree.ordinal), string)
       else:
           yield from iterate_htree(my_tree.left, string + "0")
           yield from iterate_htree(my_tree.right, string + "1")

def generator_to_string(tree):
    temp = iterate_htree(tree.root,"")
    return [i for i in temp]

#Tuple, Tuple -> Boolean
#Comes before function used for comparing the count in tuples
def comes_before_tuple(a,b):
    if ord(a[0]) < ord(b[0]):
        return True
    else:
        return False

# Returns a linkedList that contains tuples as values
# Basically used so the insert_sorted function can be run on this
def sort_final_array(inputArray):
    newlist = empty_list()
    returnlist = empty_list()
    for x in inputArray:
        newlist = add(newlist,0,x)

    while newlist is not None:
        returnlist = insert_sorted(returnlist,newlist.first,comes_before_tuple)
        newlist = newlist.rest
    return returnlist

#inputArray is a frequency array
def final_array(inputArray,inputList):
    newArray = array_list.empty_list()
    newArray.capacity = 256
    newArray.array = [None] * 256
    for x in range(length(inputList)):
        temp = ord(inputList.first[0])
        for x in range(inputArray.capacity):
            if x == temp:
                temp2 = inputArray.array[x-1]
                newArray.array[x] = (inputList.first[1],temp2)
                newArray.size += 1
        inputList = inputList.rest
    return newArray


#-------------------------< Main Encode Function >----------------------------------
def huffman_encode(inputFile,outputFile):
    if os.path.exists(inputFile) is False:
        raise IOError

    hb_writer = HuffmanBitsWriter(outputFile)
    freqArray = txt_to_freq(inputFile)
    totalOccurence = freqArray.size
    print(totalOccurence)

    if totalOccurence == 0: #Encoding an empty file
        hb_writer.write_byte(totalOccurence)
        hb_writer.close()
        return ""

    elif totalOccurence == 1:
        myChar = (array_to_sortedList(freqArray).first.root.ordinal)
        hb_writer.write_byte(totalOccurence)
        hb_writer.write_byte(myChar)
        hb_writer.write_int(array_to_sortedList(freqArray).first.root.count)
        hb_writer.close()
        return(chr(myChar))

    elif totalOccurence > 1:
        sortedList = array_to_sortedList(freqArray)
        listTree = HuffmanTree(sortedList)

        myTree = build_tree(listTree)
        sortedLinkedList = sort_final_array(generator_to_string(myTree))
        finalArray = final_array(freqArray, sortedLinkedList)
        compareTemp = (sortedList.first.root.ordinal)
        allSame = True
        while sortedList != None:
            if sortedList.first.root.ordinal != compareTemp:
                allSame = False
            sortedList = sortedList.rest

        if allSame:
            totalSize = finalArray.size
            ordChr = (ord(sortedLinkedList.first[0]))
            repeatTime = (finalArray.array[ordChr][1])
            hb_writer.write_byte(totalSize)
            hb_writer.write_byte(ordChr)
            hb_writer.write_int(repeatTime)
            hb_writer.close()
            return sortedLinkedList.first[0]

        else:
            sortedList = array_to_sortedList(freqArray)
            listTree = HuffmanTree(sortedList)

            myTree = build_tree(listTree)
            sortedLinkedList = sort_final_array(generator_to_string(myTree))
            finalArray = final_array(freqArray,sortedLinkedList)

            totalOccurence = length(sortedLinkedList)
            hb_writer.write_byte(totalOccurence)

            for x in range(finalArray.capacity):
                if finalArray.array[x] is not None:
                    hb_writer.write_byte(x)
                    hb_writer.write_int(finalArray.array[x][1])

            emptyString = ""
            f = open(inputFile, 'r')
            allLines = f.read()
            for x in allLines:
                temp = ord(x)
                emptyString += finalArray.array[temp][0]
            hb_writer.write_code(emptyString)

            tupleList = leaf_to_string(build_tree(HuffmanTree(array_to_sortedList(txt_to_freq(inputFile)))).root)
            chrList = ([i[0] for i in tupleList])
            finalString = ""
            for x in chrList:
                finalString += x


            f.close()
            hb_writer.close()
            return finalString

#-------------------------< Main Decode Function >----------------------------------

def huffman_decode(inFile,outFile):

    f = open(outFile, "w")
    hb_reader = HuffmanBitsReader(inFile)
    finalString = ""
    try:
        totalOccurence = hb_reader.read_byte()

        newArray = array_list.empty_list()
        newArray.capacity = 256
        newArray.array = [0] * 256
        for x in range(0, totalOccurence):
            myCount = hb_reader.read_byte()
            newFreak = hb_reader.read_int()
            newArray.array[myCount - 1] = newFreak
        Dtree = build_tree(HuffmanTree(array_to_sortedList(newArray)))
        totalChr = Dtree.root.count
        ogTree = Dtree.root
        current = Dtree.root
        while totalChr != 0:
            if type(current) == Leaf:
                finalString += chr(current.ordinal)
                totalChr -= 1
                current = ogTree

            else:
                oneBit = hb_reader.read_bit()
                if oneBit is True:
                    current = current.right
                else:
                    current = current.left

        f.write(finalString)
        hb_reader.close()
        f.close()
        return None

    except: #isempty
        f.close()
        hb_reader.close()
        return None

#-------------------------< Testing Units >----------------------------------
class TestCases(unittest.TestCase):
    # def test_decode(self):
    #     self.assertEqual(huffman_decode("output.bin","sample.txt"),None) #abcd abc ab a
    #
    # def test_decode2(self):
    #     self.assertEqual(huffman_decode("output2.bin","sample2.txt"),None) #Decode empty file
    #
    # def test_decode3(self):
    #     self.assertEqual(huffman_decode("output_empty.bin", "empty.txt"), None)  # Decode empty file
    #
    # def test_decode4(self):
    #     self.assertEqual(huffman_decode("output_empty2.bin", "code.txt"), None)  # Decode empty file
    #
    # def test_decode5(self):
    #     self.assertEqual(huffman_decode("code.bin", "cool.txt"), None)  # Decode empty file
    #
    def test_encode_full(self):
        self.assertEqual(huffman_encode("sample.txt", "output.bin"), 'lnos abce')  # abcd abc ab a

    # def test_encode_fl(self):
    #     self.assertEqual(huffman_encode("sample2.txt", "output2.bin"), 'a')  # aaaa
    #
    # def test_encode_empty(self):
    #     self.assertEqual(huffman_encode("empty.txt", "output_empty.bin"), '')  # empty
    #
    # def test_encode_empty2(self):
    #     self.assertEqual(huffman_encode("code.txt", "output_empty2.bin"), 'a')  # a
    #
    # def test_encode_more(self):
    #     self.assertEqual(huffman_encode("cool.txt", "code.bin"),'ehlnaFMINjpbytorE!?GJLPRzHT\'OUYi,kv\nwAg cC".msdu-SWBDf')  # a
    #
    # def test_encode_IOerror(self):
    #     with self.assertRaises(OSError):
    #         (huffman_encode("text$file.txt","textfile_encoded.bin"))
    #
    # def test_eq(self):
    #     myList = empty_list()
    #     secondList = empty_list()
    #     self.assertEqual(myList, secondList)
    #
    # def test_empty(self):
    #     myList = array_list.empty_list()
    #     newArray = array_list.empty_list()
    #     self.assertEqual(myList, newArray)
    #
    # def test_pair_repr(self):
    #     myPair = Pair(5,None)
    #     self.assertEqual(myPair.__repr__(),"Pair(5, None)")

    def test_array_repr(self):
        myPair = array_list.empty_list()
        self.assertEqual(myPair.__repr__(),"Array([None, None, None, None, None, None, None, None, None, None], Size 0)")

    def test_add_IE2(self):
        with self.assertRaises(IndexError):
            add(empty_list(),-5,99)

    def test_length1(self):
        myList = array_list.empty_list()
        self.assertEqual(array_list.length(myList),0)

    def test_add_IE3(self):
        with self.assertRaises(IndexError):
            array_list.add(array_list.empty_list(),-5,99)

    def test_add_mid(self):
        myList = array_list.empty_list()
        myList.size = 3
        myList.array[0] = 1
        myList.array[1] = 2
        myList.array[2] = 3
        compareList = array_list.empty_list()
        compareList.size = 4
        compareList.array[0] = 1
        compareList.array[1] = 2
        compareList.array[2] = 99
        compareList.array[3] = 3
        self.assertEqual(array_list.add(myList,2,99),compareList)

    def test_eq_leaf(self):
        myLeaf = Leaf(54,2)
        secondLeaf = Leaf(54,2)
        self.assertEqual(myLeaf == secondLeaf,True)

    def test_eq_node(self):
        myLeaf = Node(54,2,None)
        secondLeaf = Node(54,2,None)
        self.assertEqual(myLeaf == secondLeaf,True)

    def test_eq_huffT(self):
        myTree = HuffmanTree(Leaf(54    ,2))
        secondTree = HuffmanTree(Leaf(54,2))
        self.assertEqual(myTree == secondTree, True)

    def test_repr_huffT(self):
        myTree = HuffmanTree(Leaf(54,2))
        self.assertEqual(myTree.__repr__(),"Tree(2)")

    def test_comes_before_edge(self):
        tree1 = HuffmanTree(Leaf(53,2))
        tree2 = HuffmanTree(Leaf(52,2))
        self.assertEqual(comes_before(tree2,tree1),True)

    def test_comes_before_edge2(self):
        tree1 = HuffmanTree(Leaf(53,2))
        tree2 = HuffmanTree(Leaf(52,2))
        self.assertEqual(comes_before(tree1,tree2),False)


if __name__ == "__main__":
    unittest.main()
