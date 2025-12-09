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


# l = list(range(100))

# modified_list = [elem ** 2 if elem % 2 == 0 else elem ** 3 for elem in l ]
# print(modified_list)

# def process_call_logs(call_logs, task):
#     call_counts = {}
#     total_durations = {}

#     # Build counts and durations
#     for log in call_logs:
#         name = log["name"]
#         duration = log["duration"]

#         call_counts[name] = call_counts.get(name, 0) + 1
#         total_durations[name] = total_durations.get(name, 0) + duration

#     # Task 1
#     if task == "get_call_counts":
#         return call_counts

#     # Task 2
#     if task == "get_total_call_durations":
#         return total_durations

#     # Task 3
#     if task == "most_frequent_caller":
#         if not call_logs:
#             return ""

#         # Highest call count
#         max_count = max(call_counts.values())

#         # callers that match max count
#         top_callers = [name for name in call_counts if call_counts[name] == max_count]

#         # Only one → return it
#         if len(top_callers) == 1:
#             return top_callers[0]

#         # Tie → break by duration
#         best = top_callers[0]
#         for name in top_callers:
#             if total_durations[name] > total_durations[best]:
#                 best = name
#         return best

#     # Invalid task
#     return None

# b = process_call_logs(
#         [
#             {"name": "Alice", "duration": 300},
#             {"name": "Bob", "duration": 200},
#             {"name": "Alice", "duration": 100},
#             {"name": "Bob", "duration": 400}
#         ],
#         "get_total_call_durations"
#     )
# print(b)

# toggle_lower = True
# out = ""
# with open("test.txt","r") as file:
#     text = file.read()
#     for  char in text:
#         if char == "^":
#             toggle_lower = not toggle_lower
#             continue
#         if toggle_lower:
#             out += char.lower()
#         else:
#             out += char.upper()
# print(out)

# with open("test.txt","r") as f:
#     lines=f.readlines()
#     for line in lines:
#         sum_=0
#         for word in line.split():
#             if word.isdigit():
#                 sum_+=int(word)
#         print(sum_)


# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:  
#         sum_ = 0
#         for _ in line.split(" "):
#             print
#             if _.isdigit():
#                 sum_ += int(_)
#         print(sum_)


# with open("test.txt","r") as f:
#     num=int(f.readline())
#         lines=f.readlines()
#             for line in lines:
#                     if num>len(line.split()):
#                                 print("NULL")
#                                         else:
#                                                     print(line.split()[num-1])



# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     n = int(lines[0])
#     for line in lines[1:]:
#         result = ""
#         if len(line.split()) < n:
#             result = "NULL"
#         else:
#             result = line.split()[n-1]

# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#       print(line[::-1])

# with open("test.txt","r") as f:
#     lines=f.readlines()
#     for line in lines:
#         out_list = []
#         for word in line.split():
#             out_list.append(word[::-1])
#         print(" ".join(out_list))

with open("test.txt", "r") as file:
    text = file.read()
    words = text.split(" ")
    out = ""
    for i in range(len(words)-1):
        out += words[i] + str(i+1)
    out += words[-1]
    print(out)



