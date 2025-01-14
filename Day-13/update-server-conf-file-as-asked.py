def server_conf_update(server_config_file, key_to_update, new_value):

    # open server.conf file in read mode
    with open("/home/asharma/devops/Python/python-for-devops_AV/Day-12/server.conf", "r") as file:
        conf_file = file.readlines()    # returns a list of all the lines
        #print(conf_file)

    with open("/home/asharma/devops/Python/python-for-devops_AV/Day-12/server.conf", "w") as file:
        for line in conf_file:
            if key_to_update in line:
                file.write(key_to_update+"="+new_value+"\n")
            else:
                file.write(line)

# you can take all these 3 values from user through input() function.
server_conf_update("/home/asharma/devops/Python/python-for-devops_AV/Day-12/server.conf", "MAX_CONNECTIONS", "300")