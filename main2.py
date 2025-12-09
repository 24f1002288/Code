# with open("test.txt","r") as file:
#     marker = file.readline().strip()
#     lines=file.readlines()
#     lineNew=""
#     for line in lines:
#         for char in line:
#             if char==marker:
#                 lineNew+= "\n"
#                 break
#             else:
#                 lineNew+=char
#     print (lineNew.strip())


# with open("test.txt", "r") as file:
#     marker = file.readline().strip()
#     lines = file.readlines()
#     result = []
#     for line in lines:
#       # if "#" in line:
#         line = line.split(marker)
#         result.append(line[0].rstrip())  
#     print("\n".join(result))




# with open("test.txt","r") as f:
#     lines=f.readlines()
#     l=[]
#     for i in range(len(lines)-1):
#         if lines[i]==lines[i+1]:
#             continue
#         else:
#             l.append(lines[i].strip())
#     if lines[-1].strip() != lines[-2].strip():
#         l.append(lines[-1].strip())
#     print("\n".join(l))

# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     result = []
#     previous_line = None
#     for line in lines:
#       if line != previous_line:
#         result.append(line.strip())
#       previous_line = line
#     print("\n".join(result))

# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     lines = [line.strip() for line in lines]
#     max_line = max([len(line) for line in lines])
#     u_border = "*" * (max_line + 4)
#     print(u_border)
#     for line in lines:
#         print("* " + line + " " * (max_line - len(line)) + " *")
#     print(u_border)

# with open("test.txt","r") as f:
#     lines=f.readlines()
#     #lines = [line.strip() for line in lines]
#     l=[]
#     for line in lines:
#         l.append(len(line.strip()))
#     print("*"*(max(l)+4))

#     for line in lines:
#         print(f'* {line.strip()}{" " * (max(l) - len(line.strip()))} *')

#     print("*"*(max(l)+4))
    