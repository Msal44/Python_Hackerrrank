'''
split_and_join method with line argument

The line, which is the input, will be split up using .split(" ").
We will join the with a dash using "-".join(line). We then return the line.
'''
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

#provided by hackerrank
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
