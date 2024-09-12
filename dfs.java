import java.util.ArrayList;
import java.util.List;

class DGS{

static void addEdge(List<List<Integer>>adj,int s,int t){
    adj.get(s).add(t);
    adj.get(t).add(s);
}



static void dfs_rec(List<List<Integer>>adj,boolean[] visited, int s){
    visited[s]=true;
    System.out.println(s);
    for (int i : adj.get(s)){
        if (!visited[i]){
            dfs_rec(adj,visited,i);


        }
    }
}
static void dfs(List<List<Integer>>adj, int sourc){
    boolean [] visited = new boolean[adj.size()];
    dfs_rec(adj,visited,sourc);
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
    dfs(adj,sourc);
}

}