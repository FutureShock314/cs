def bubbleSort( inList ) -> list:
    '''
    Sorts a list using the bubble sort algorithm
    '''

    outList = inList.copy()

    for i in range( len( inList ) - 1 ):
        for j in range( len( inList ) - 1 ):
            if outList[ j ] > outList[ j + 1 ]:
                outList[ j ], outList[ j + 1 ] = outList[ j + 1 ], outList[ j ]

            print( outList )        