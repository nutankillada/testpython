#1
s3_buckets = ["bucket-01", "bucket-02","bucket-03"]

print(s3_buckets)
#2
servers = ("bucket-01", "bucket-02","bucket-03","bucket-03")
first_server = servers[1]

print(type(first_server),first_server[2])
#3

servers_list = ["web-server-01","web-server-02","web-server-03"]
servers_list.remove("web-server-02")
print(servers_list)