name = "Huxley"
age = 23
goal_per_month = 5000
city = "HCMC"
current_salary = 900
is_good_dev = True

# print("Tên: ", name)
# print("Tuổi: ", age)
# print("Mục tiêu thu nhập 1 tháng: ", goal_per_month)
# print("Thành phố: ", city)

# print(type(name))
# print(type(age))
# print(type(city))

# print(type(is_good_dev))
# if is_good_dev:
#     print("Có phải là một Dev tốt không ? Có")
# else:
#     print("Có phải là một Dev tốt không ? Không")


# if current_salary >= 5000:
#     print("Đạt mục tiêu!")
# elif current_salary >= 2000:
#     print("Đang trên đường, cố gắng thêm")
# else:
#     print("Cần nỗ lực nhiều hơn nữa")


# months = [1, 2, 3, 4, 5, 6]

# for month in months:
#     print("Tháng: ", month)
#     if month <= 3:
#         print("--- đang học Python")
#     else:
#         print("--- đang làm dự án mẫu")


# for month in range(1, 13):
#     if month == 12:
#         print("Tháng ", month, " là cuối năm")
#     elif month >= 10:
#         print("Tháng ", month, " là gần cuối năm")
#     elif 5 <= month <= 9:
#         print("Tháng ", month, " là giữa năm")
#     else:
#         print("Tháng ", month, " là đầu năm")


def chao_mung(name, goal_per_month):
    print("Chúc", name, "sẽ đạt được mục tiêu", goal_per_month, "USD/tháng")

# Nên viết function có return


def check_goal_salary(goal_per_month, current_salary):
    if goal_per_month <= current_salary:
        return "Đã đạt được mục tiêu lương"
    else:
        return "Chưa đạt được mục tiêu lương"

# Nếu function không có return hoặc print mà gán vào biến thì dùng result = name_function(var1, var2,...) sau đó dùng print(result) để xem kết quả


chao_mung(name, goal_per_month)
check_goal_salary(goal_per_month, current_salary)
