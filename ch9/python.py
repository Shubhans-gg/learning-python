with open("harry python\ch9\python.txt") as f:
    content=f.readlines()

line_no=1
for line in content:
    if "Python" in line:
        print(f"Python is present in line {line_no}\n{line}\n")
        line_no=line_no+1
    
    else:
        line_no=line_no+1
