
# coding: utf-8




from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse( y ):
    x = y
    list_ = []
    while( x.getPred() ):
        list_.insert( 0, x.id )
        x = x.getPred()
    if len(list_) > 0:
        list_.insert( 0, x.id )
    else:
        list_.insert( 0, 'no path' )
    return ( list_ )


def resetGraph( g ):
    for v in g:
        v.setDistance( 0 )
        v.setPred( None )
        v.setColor( 'white' )


def allPairsShortestPath( g ):
    for v in g:
        resetGraph( g )
        bfs(g, v)
        for vert in g:
            if vert != v:
                print ( 'from', v.id, 'to', vert.id, ':', traverse( vert ) )
                

def escapeMaze( g, idStart, idExit ):
    vertStart = g.getVertex( idStart )
    vertExit = g.getVertex( idExit )
    resetGraph( g )
    bfs( g, vertStart )
    print( traverse( vertExit ) )

if __name__ == "__main__":
    
    gg = Graph()
    verts = 'ABCDEFGHI'
    #verts = 'AEGDBCFHI' 
    for i in verts:
        gg.addVertex(i)
        
    print( gg.getVertices() )
    gg.addEdge('B','A')
    gg.addEdge('A','B')
    gg.addEdge('B','C')
    gg.addEdge('C','F')
    gg.addEdge('F','H')
    gg.addEdge('H','I')
    gg.addEdge('I','F')
    gg.addEdge('B','E')
    gg.addEdge('E','D')
    gg.addEdge('D','B')
    gg.addEdge('E','A')
    gg.addEdge('D','G')
    gg.addEdge('G','E')

    allPairsShortestPath( gg )
    
    escapeMaze( gg, 'D', 'A' )

