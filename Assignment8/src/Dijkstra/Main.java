package Dijkstra;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

public class Main {

    public static Graph calShortestPathFromSource(Graph graph, Node source) {
        source.setDist(0);

        Set<Node> settled = new HashSet<>();
        Set<Node> unsettled = new HashSet<>();

        unsettled.add(source);

        while (unsettled.size() != 0) {
            Node currNode = getNearestNode(unsettled);

            unsettled.remove(currNode);
            for (Map.Entry<Node, Integer> adjPair:
                    currNode.getAdjNodes().entrySet()) {
                Node adjNode = adjPair.getKey();
                Integer edgeWeight = adjPair.getValue();
                if (!settled.contains(adjNode)) {
                    sumMinDist(adjNode, edgeWeight, currNode);
                    unsettled.add(adjNode);
                }
            }
            settled.add(currNode);
        }
        return graph;
    }

    private static Node getNearestNode(Set<Node> unsettled) {
        Node nearestNode = null;
        int nearestDist = Integer.MAX_VALUE;
        for (Node node: unsettled) {
            int nodeDist= node.getDist();
            if (nodeDist < nearestDist) {
                nearestDist = nodeDist;
                nearestNode = node;
            }
        }
        return nearestNode;
    }

    private static void sumMinDist(Node evaluationNode, Integer edgeWeigh, Node sourceNode) {
        Integer sourceDistance = sourceNode.getDist();
        if (sourceDistance + edgeWeigh < evaluationNode.getDist()) {
            evaluationNode.setDist(sourceDistance + edgeWeigh);
            LinkedList<Node> shortestPath = new LinkedList<>(sourceNode.getShortestPath());
            shortestPath.add(sourceNode);
            evaluationNode.setShortestPath(shortestPath);
        }
    }

    public static void main(String[] args) {

        Node nodeA = new Node("a");
        Node nodeB = new Node("b");
        Node nodeC = new Node("c");
        Node nodeD = new Node("d");
        Node nodeE = new Node("e");

        nodeA.addDestination(nodeB, 3);
        nodeA.addDestination(nodeD, 7);
        nodeB.addDestination(nodeC, 2);
        nodeC.addDestination(nodeE, 4);
        nodeD.addDestination(nodeE, 8);

        Graph graph = new Graph();

        graph.addNode(nodeA);
        graph.addNode(nodeB);
        graph.addNode(nodeC);
        graph.addNode(nodeD);
        graph.addNode(nodeE);

        System.out.println(calShortestPathFromSource(graph, nodeB));

    }
}

