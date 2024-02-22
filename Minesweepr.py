def get_adjacent_mines(grid):
    # get the number of rows and colums in the grid
    rows = len(grid)  
    cols = len(grid[0])  
    # list to store the updated grid
    result = []  
    
    for i, row in enumerate(grid):  # loop through each row in the grid
        new_row = []  # initialize a list to store the updated row

        for j, spot in enumerate(row):  # loop through each spot in the current row
            if spot == '#':  # if the current spot is a mine
                new_row.append('#')  # append the mine symbol to the new row

            else:  # otherwise, the current spot is mine-free
                count = 0  # count variable to store the number of adjacent mines

                for x in range(max(0, i-1), min(rows, i+2)):  # loop through the neighboring rows (stopping at edges)

                    for y in range(max(0, j-1), min(cols, j+2)):  # loop through the neighboring spots in the current row (stopping at edges)

                        if grid[x][y] == '#':  # if the neighboring spot is a mine
                            count += 1  # increment the count variable
                new_row.append(str(count))  # append the count as a string to the new row
        result.append(new_row)  # append the updated row to the updated grid
    return result  # return the updated grid

# Example usage
grid = [
    ["#", "-", "#", "-", "#"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["#", "-", "#", "-", "#"]
]
result = get_adjacent_mines(grid)
print(result)
