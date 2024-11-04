import sys
#Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest path tree, i.e., whose minimum distance from the source is calculated and finalized. Initially, this set is empty.
class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for c in range(vertices)] for r in range(vertices)]
    

    def prints(self,dist):
        # print 0->9 and min dist
        for n in range(self.V):
            print(n,dist[n])
    
    # Picking the min and returning
    def mindist(self,dist,sptSet):
        min =sys.maxsize
        for u in range(self.V):
            if dist[u]<min and sptSet[u]==False:
                min=dist[u]
                min_index=u
        return min_index
    

    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptSet=[False]*self.V

        for c in range(self.V):
            x=self.mindist(dist,sptSet)
            sptSet[x]=True

            for y in range(self.V):
                if self.graph[x][y]>0 and sptSet[y]==False and dist[y]>dist[x]+self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]
        self.prints(dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)