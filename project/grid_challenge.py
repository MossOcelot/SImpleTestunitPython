def gridChallenge(n,grid):
    # Write your code here
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(n-1):
        for j in range(n):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"   
    
if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(n,grid)

        print(result)