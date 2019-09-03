def getdate():
    import datetime
    return datetime.datetime.now()

client_list = {1: "Harry", 2: "Rajesh", 3: "Vikash"}
log_list = {1: "Exercise", 2: "Diet"}

try:
    print("Select clients name:")
    for key, value in client_list.items():
        print(f"Press {key} for {value}")
    client_name = int(input())

    print("Selected client is", client_list[client_name], "\n", end="")

    print("Press 1 for log Update")
    print('Press 2 for Retrieve')
    operation = int(input())

    if operation is 1:
        for key, value in log_list.items():
            print("Press", key, "to update log", value,"\n", end="")
        log_name = int(input())
        print("Selected Job:",log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while k is not 'n':
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[" + str(getdate()) + "]: " + mytext + "\n")
            k = input("Add More ?  y/n:")
            continue
        f.close()
    elif operation is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_name = int(input())
        print(client_list[client_name] + " -", log_list[log_name], "Report:", "\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid input!")
except Exception as e:
    print("Wrong Input!")