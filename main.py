# with open("test.txt","r") as f:
#     # words = [word.strip("\n")for word in f.readline().split(",")]
#     words = f.readline().strip("\n").split(",")
#     text = f.read()
#     # a = "abc\n"[:-1]
#     # print(a == "abc")
#     for word in words:
#         text = text.replace(word,"*"*len(word))
#     print(text)

# with open("test.txt","r") as f:
#     lines  = [line.strip() for line in f.readlines()]
#     print(lines)
#     counter = 0
#     for line in lines:
#         if line != "" :
#             counter += 1
#             print(f"{counter}. {line}")

# with open("test.txt","r") as f:
#     lines = f.readlines()
#     max_len = max([len(line.strip("\n")) for line in lines])
#     print("*"*(max_len+4))
#     for line in lines:
#         print(f"* {line.strip("\n")}{" "*(max_len - len(line.strip("\n")))} *")
#     print("*"*(max_len+4))


l = list(range(100))

modified_list = [elem ** 2 if elem % 2 == 0 else elem ** 3 for elem in l ]
print(modified_list)
