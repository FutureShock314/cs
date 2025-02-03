import random, rich
from icecream import ic
from bubbleSort import bubbleSort

testList = list( range( 1, 21 ) )
random.shuffle( testList )

print('Bubble Sort: ')
bubbleSort( testList )
