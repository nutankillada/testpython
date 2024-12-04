# for loop example
fruits = ["apple","banana","cherry"]
for fru in fruits:
    print(fru)

# while loop example
count = 0
while count < 3:
    print(count)
    count+=1

# loop control statements(break)
students_in_room = [1,2,3, 4,5]
for number in students_in_room:
    if number ==3:
        break
    print(number)

# loop control statements(continue)
numbers = [1,2,3,4,5]
for number in numbers:
    if number ==3:
        continue
    print(number)

# Automation log file analysis

log_file = [
    "INFO: Operation successful",
    "ERROR: File not found",
    "DEBUG: Connection established",
    "ERROR: Database Connection failed",
]
for line in log_file:
    if "ERROR" in line:
        print(line)

# for Loops
# servers=("server1" "server2" "server3")
# for server in "${servers[@]}":
#     configure_monitoring_agent "$server"
# done

# servers=("server1" "server2" "server3")
# for server in "${servers[@]}":
#     configure_monitoring_agent "$servers"
# done

# **Deploying Configurations to Multiple Environments:**

