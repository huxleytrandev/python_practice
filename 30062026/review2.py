# Bài 1
# Tạo list chứa 4 dictionary, mỗi cái là thông tin một học sinh gồm "ten", "diem", và "lop". Sau đó:
# In ra tên và xếp loại của từng học sinh (dùng lại classify_score)
# Tính điểm trung bình cả lớp
# In ra tên học sinh có điểm cao nhất

# list_student = [
#     {
#         "name": "Huxley",
#         "score": 7,
#         "class": "12A6"
#     },
#     {
#         "name": "Trang Thu",
#         "score": 10,
#         "class": "12A6"
#     },
#     {
#         "name": "Chau Pham",
#         "score": 9,
#         "class": "12A6"
#     },
#     {
#         "name": "Linh Tran",
#         "score": 6,
#         "class": "12A6"
#     },
#     {
#         "name": "Trang Nguyen",
#         "score": 10,
#         "class": "12A6"
#     },
#     {
#         "name": "Dang Khoa",
#         "score": 5,
#         "class": "12A6"
#     },
#     {
#         "name": "Quang Hoang",
#         "score": 6,
#         "class": "12A6"
#     },
#     {
#         "name": "Quan Bach",
#         "score": 4,
#         "class": "12A6"
#     }
# ]

# def classify_score(score):
#     if score >= 8:
#         return "Giỏi"
#     elif score >= 6:
#         return "Khá"
#     elif score >= 4:
#         return "Trung bình"
#     else:
#         return "Yếu"

# def average_score(list_student):
#     sum_score = 0
#     for student in list_student:
#         sum_score += student["score"]
#     return sum_score/len(list_student)

# def find_best_student(list_student):
#     max_score = max(student["score"] for student in list_student)
#     list_best_student = [s for s in list_student if s["score"] == max_score]
#     if len(list_best_student) > 1:
#         print(f"Có {len(list_best_student)} học sinh điểm cao nhất:")
#         for s in list_best_student:
#             print(f"  {s['name']} — {s['score']} điểm")
#     else:
#         print(f"Học sinh giỏi nhất: {list_best_student[0]['name']} — {max_score} điểm")

# print("Danh sách lớp 12A6 và xếp hạng:")
# for student in list_student:
#     print("Học sinh", student["name"], "xếp loại", classify_score(student["score"]))
# print("Điểm trung bình của lớp là:", average_score(list_student))
# find_best_student(list_student)


# Bài 2
# Viết code:
# Kiểm tra status — nếu không phải "success" thì print "Lỗi API" và dừng
# Lấy list students từ trong api_response ra
# Dùng lại classify_score và find_best_student với data đã cho 

api_response = {
    "status": "False",
    "data": {
        "class": "12A6",
        "students": [
            {"name": "Huxley", "score": 7},
            {"name": "Trang Thu", "score": 10},
            {"name": "Chau Pham", "score": 9},
            {"name": "Linh Tran", "score": 6}
        ]
    },
    "total": 4
}

def check_status(status):
    if status == "success":
        return True
    else:
        return False

def get_list_student_from_data(data):
    list_student = data["students"]
    return list_student

def find_best_student(list_student):
    max_score = max(student["score"] for student in list_student)
    list_best_student = [student for student in list_student if student["score"] == max_score]
    if len(list_best_student) > 1:
        print(f"Có {len(list_best_student)} học sinh đạt điểm cao nhất lớp")
        for student in list_best_student:
            print(f"{student['name']} --- {student['score']} điểm")
    else:
        print(f"Học sinh có điểm cao nhất là {list_best_student[0]['name']} --- {list_best_student[0]['score']} điểm")

def classify_score(score):
    if score >= 8:
        return "Giỏi"
    elif score >= 6:
        return "Khá"
    elif score >= 4:
        return "Trung bình"
    else:
        return "Yếu"

if check_status(api_response["status"]) == False:
    raise Exception("Lỗi api")

print(f"Danh sách học sinh lớp {api_response['data']['class']}:")

list_student_from_api = get_list_student_from_data(api_response["data"])

for student in list_student_from_api:
    print(f"{student['name']} --- {student['score']} điểm --- xếp loại {classify_score(student['score'])}")

find_best_student(list_student_from_api)