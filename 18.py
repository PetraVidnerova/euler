triangle = [] 
for line in open("input18.txt"):
    triangle.append([x for x in map(int, line.split())])

for i in range(1,len(triangle)):
    # first and last member has only one parent 
    triangle[i][0] += triangle[i-1][0]
    triangle[i][len(triangle[i])-1] += triangle[i-1][len(triangle[i])-2]
    # take maximum of j-th and (j-1)-th member from previous line  
    for j in range(1,len(triangle[i])-1):
        triangle[i][j] += max([triangle[i-1][j-1], triangle[i-1][j]])
                   
# print the last line
print(triangle[len(triangle)-1])
print(max(triangle[len(triangle)-1]))
