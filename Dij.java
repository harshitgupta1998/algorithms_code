import java.io.*;
import java.lang.*;
import java.util.*;

public class Dij{
    static final int V = 9;

    public void prints (int dist[])
    {
        for (int i = 0; i < V; i++)
            System.out.println(i + " \t\t " + dist[i]); 
    }
    int mindist(int dist[],Boolean spt[]){
        int min=Integer.MAX_VALUE;
        int min_index=-1;
        for (int v=0;v<V;v++){
            if(spt[v]==false && dist[v]<=min){
                min=dist[v];
                min_index=v;
            }
        }
        return min_index;
    }
    void dijkstra(int graph[][], int src){
        int dist[]= new int[V];
        Boolean spt[] = new Boolean[V];
        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
            spt[i] = false;
        }
        dist[src]=0;
        for (int count = 0; count < V - 1; count++) {
            //get the min dist for the current vertex
            int u=mindist(dist, spt);
            spt[u]=true;

            for (int v=0;v<v;v++){
                if(!spt[v] && graph[u][v]!=0 && dist[u] !=Integer.MAX_VALUE && dist[u]+graph[u][v]<dist[v]){
                    dist[v]=dist[u]+graph[u][v];
                }

            }


        }
        prints(dist);
    }

    public static void main(String[] args)
    {
        /* Let us create the example graph discussed above
        */
        int graph[][]
            = new int[][] { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
                            { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                            { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
                            { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                            { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                            { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                            { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                            { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                            { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };
        Dij t = new Dij();

        // Function call
        t.dijkstra(graph, 0);
    }
    

}