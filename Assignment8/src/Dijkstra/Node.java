package Dijkstra;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Node {
    private String name;
    private List<Node> shortestPath = new LinkedList<>();
    private Integer dist = Integer.MAX_VALUE;
    private final Map<Node, Integer> adjNodes = new HashMap<>();

    public void addDestination(Node destination, int dist) {
        adjNodes.put(destination, dist);
    }

    public Node(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getDist() {
        return dist;
    }

    public void setDist(int dist) {
        this.dist = dist;
    }

    public Map<Node, Integer> getAdjNodes() {
        return adjNodes;
    }

    public List<Node> getShortestPath() {
        return shortestPath;
    }

    public void setShortestPath(LinkedList<Node> shortestPath) {
        this.shortestPath = shortestPath;
    }
}

