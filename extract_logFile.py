# date & time, kind of error [INFO, WARNING, ERROR], description

# {'INFO': [], 'WARNING': [], ERROR: []}


# from datetime import datetime
# def get_log(log_file):
#   try:
# 	file = None
# 	INFO_list = []
# 	WARNING_list = []
# 	ERROR_list = None
# 	with open(log_file,'r') as f:
# 		f = file
# 	for I in file:
# 	    if I == "INFO":
# 		INFO_list = I
# 	    if I == "kind of error":
# 		WARNING_list = I
# 	    if I == "description":
# 	      ERROR_list = []
# 	return {'INFO':INFO_list, 'WARNING': WARNING_list, ERROR: ERROR_list}	
#   except Exception as ex:
# 	print(ex)







logs = [
    "2025-07-11 10:01:00, INFO, System boot completed",
    "2025-07-11 10:05:00, WARNING, High memory usage detected",
    "2025-07-11 10:10:00, ERROR, Failed to connect to database",
    "2025-07-11 10:15:00, INFO, Scheduled task executed",
    "2025-07-11 10:20:00, ERROR, Disk not found"
]




log_dict = {'INFO': [], 'WARNING': [], 'ERROR': []}


with open("log_file.txt","r") as f:
    for line in f:
        parts = line.split(", ")
        if len(parts) == 3:
            _, log_type, message = parts
            if log_type in log_dict:
                log_dict[log_type].append(message)


# print(log_dict)

a,b,c = ["2025-07-11 10:01:00", "INFO", "System boot completed"]
print(a)
