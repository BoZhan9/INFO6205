public class NumberOfIslands {
    public int numIslands(boolean[][] grid) {
        if (grid == null) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j]) {
                    count++;
                    this.search(grid, i, j);
                }
            }
        }

        return count;
    }

    public void search(boolean[][] grid, int x, int y) {
        if (x < 0 || x > grid.length - 1 || y < 0 || y > grid[x].length - 1) {
            return;
        }

        if (!grid[x][y]) {
            return;
        }

        grid[x][y] = false;

        search(grid, x + 1, y);
        search(grid, x, y + 1);
        search(grid, x - 1, y);
        search(grid, x, y - 1);

    }

    public static void main(String[] args) {
        NumberOfIslands n = new NumberOfIslands();
        boolean[][] grid = new boolean[][]{
                {false, true, true, true, false},
                {true, true, false, false, false},
                {true, false, false, true, false},
                {false, false, false, false, true}
        };
        System.out.println(n.numIslands(grid));
    }
}
