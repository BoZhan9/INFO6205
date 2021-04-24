import java.util.*;

public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        wordList.add(endWord);
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);
        Map<String, Integer> dist = new HashMap<>();
        dist.put(beginWord, 1);

        while (!queue.isEmpty()) {
            String word = queue.poll();
            if (word.equals(endWord)) {
                return dist.get(word);
            }

            for (String next: getNext(word, wordList)) {
                if (dist.containsKey(next)) {
                    continue;
                }
                queue.offer(next);
                dist.put(next, dist.get(word) + 1);
            }
        }
        return 0;

    }

    public List<String> getNext(String word, List<String> wordList) {
        List<String> words = new LinkedList<>();
        for (int i = 0; i < word.length(); i++) {
            String l = word.substring(0, i);
            String r = word.substring(i + 1);
            for (char ch = 'a'; ch <= 'z'; ch++) {
                if (word.charAt(i) == ch) {
                    continue;
                }
                String next = l + ch + r;
                if (wordList.contains(next)) {
                    words.add(next);
                }
            }
        }
        return words;
    }
    public static void main(String[] args) {
        WordLadder w = new WordLadder();
        List<String> wordList = new ArrayList<>(
            Arrays.asList("hot","dot","dog","lot","log","cog"));
        System.out.println(w.ladderLength("hit", "cog", wordList));
    }
}
