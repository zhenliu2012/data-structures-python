
# coding: utf-8



from pythonds.graphs import Graph, Vertex

class DFSGraph( Graph ):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self, print_=0):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)            
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex, print_)

    def dfsvisit(self,startVertex,print_=0):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex, print_)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        if print_ != 0:
            print(startVertex.id, startVertex.disc, startVertex.fin)
        
    def dfs_topoSort(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
        finList = []
        for aVertex in self:
            finList.append( aVertex )
        for v in (sorted(finList, key = lambda x: x.fin , reverse = True)): 
            print( v.id, v.disc, v.fin )

    def transposeGraph( self ):
    #create a new graph w/o edges
        g_T = DFSGraph()
        for i in self.getVertices():
            g_T.addVertex(i);
    #for each edge in original graph, add reversed edge to the new graph    
        for v in self:
            for w in v.getConnections():
                g_T.vertices[w.id].addNeighbor( g_T.vertices[v.id], weight =  v.getWeight(w) )            
        return g_T

    def getSCC( self ):
    #call dfs to compute finish time
        self.dfs(1)    
    #compute g-transpose gT
        g_T = self.transposeGraph()    
    #call dfs for gT
        for aVertex in g_T:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        l = sorted(self, key = lambda x: x.fin, reverse = True)
        for v in l:
            aVertex = g_T.vertices[v.id]
            if aVertex.getColor() == 'white':
                print( "SCC in this tree:")
                g_T.dfsvisit(aVertex, 1)     
                
if __name__ == "__main__":
    #test1
    g = DFSGraph()
    pancake = ['milk','griddle','egg','oil','mix','pour','turn','eat','syrup']
    for i in pancake:
        g.addVertex(i)
    
    g.addEdge('milk','mix')
    g.addEdge('egg','mix')
    g.addEdge('oil','mix')
    g.addEdge('mix','pour')
    g.addEdge('griddle','pour')
    g.addEdge('pour','turn')
    g.addEdge('turn','eat')
    g.addEdge('mix','syrup')
    g.addEdge('syrup','eat')

    print( g.getVertices() )
    
    g.dfs_topoSort()

    for v in g:
        for w in v.getConnections():
            print( v.id, w.id )

    #test transpose
    g_T = g.transposeGraph()
    for v in g_T:
        for w in v.getConnections():
            print( v.id, w.id )

    #test2
    gg = DFSGraph()
    verts = 'ABCDEFGHI'
    #verts = 'AEGDBCFHI' 
    for i in verts:
        gg.addVertex(i)
        
    print( gg.getVertices() )

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

    for v in gg:
        for w in v.getConnections():
            print( v.id, w.id )
        
    gg.getSCC()


