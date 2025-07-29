print ("For Loop")
for i in range(5):
    print(i)

print ("While Loop")
count = 0
while count < 5:
    print(count)
    count += 1

print ("Nested Loop")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")    

print ("Print the 2-times multiplication table from 1 to 10.")
for i in range(1, 11):
    print("2 x ", i ,"= ", 2 * i)