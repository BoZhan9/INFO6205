import java.util.*;

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 0 || prerequisites.length == 0) {
            return true;
        }

        HashMap<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new ArrayList<>());

        }

        for (int i = 0; i < prerequisites.length; i++) {
            int cur = prerequisites[i][0];
            int pre = prerequisites[i][1];
            map.get(pre).add(cur);
        }

        HashMap<Integer, Integer> degree = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            for (Integer neighbor : map.get(i)) {
                if (degree.containsKey(neighbor)) {
                    degree.put(neighbor, degree.get(neighbor) + 1);
                } else {
                    degree.put(neighbor, 1);
                }
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            if (degree.containsKey(i)) {
                queue.offer(i);
                list.add(i);
            }
        }

        while (!queue.isEmpty()) {
            Integer course = queue.poll();
            for (Integer neighbor : map.get(course)) {
                degree.put(neighbor, degree.get(neighbor) - 1);

                if (degree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                    list.add(neighbor);
                }

            }
        }
        return list.size() == numCourses;
    }

    public static void main(String[] args) {
        CourseSchedule cs = new CourseSchedule();
        int[][] prerequisites = {{1, 0}, {0, 1}};
        System.out.println(cs.canFinish(2, prerequisites));
    }
}
