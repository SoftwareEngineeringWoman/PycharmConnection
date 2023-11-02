#2d List

# normal list= nember_grid=[1,2,3,4]

number_grid =[    #4 elements , each element is a list
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][2])  #[row][column]

#nested for loop
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid:
    print(row)

#print each number
for row in number_grid:
    for col in row:
        print(col)