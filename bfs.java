import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class BFS{

static void addEdge(List<List<Integer>>adj,int s,int t){
    adj.get(s).add(t);
    adj.get(t).add(s);
}



static void bfs_rec(List<List<Integer>>adj,boolean[] visited, int s){
    visited[s]=true;
    Queue<Integer> q =new LinkedList<>();
    q.offer(s);
    while( !q.isEmpty()){
        int curr=q.poll();
        System.out.println(curr);
        for (int x : adj.get(curr)){
            if (!visited[x]){
                visited[x]=true;
                q.offer(x);
            }
        }
    
    }
}
static void bfs(List<List<Integer>>adj, int sourc){
    boolean [] visited = new boolean[adj.size()];
    bfs_rec(adj,visited,sourc);
}

public static void main( String[] args)
{
    int V=5;
    List <List<Integer>> adj = new ArrayList<>(V);
    for (int i=0;i<V;i++){
        adj.add(new ArrayList<>());
    }
    int[][] edges = {
        { 1, 2 }, { 1, 0 }, { 2, 0 }, { 2, 3 }, { 2, 4 }
    };

    for (int[]e : edges){
        addEdge(adj,e[0],e[1]);
    }
    int sourc=1;
    System.out.println("Source"+sourc);
    bfs(adj,sourc);
}

}