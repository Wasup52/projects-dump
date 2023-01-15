from datetime import datetime

# start_amine = "19:01:17"
# start_zwave = "20:29:48"

# # t_zvawe = "2:09:35"

# # time_zero = datetime.strptime("00:00:00", "%H:%M:%S")

# # time_zwave = str(
# #     (
# #         datetime.strptime(start_zwave, "%H:%M:%S")
# #         - time_zero
# #         + datetime.strptime(t_zvawe, "%H:%M:%S")
# #     ).time()
# # )
# # print(time_zwave)

# t = "22:39:00"

# tdelta = datetime.strptime(t, "%H:%M:%S") - datetime.strptime(
#     start_amine, "%H:%M:%S"
# )
# print("amine :", tdelta)

t1 = "20:29:48"
t2 = "19:01:17"

tdelta = datetime.strptime(t1, "%H:%M:%S") - datetime.strptime(t2, "%H:%M:%S")
print(tdelta)
