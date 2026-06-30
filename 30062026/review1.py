# Bài 1
# In số chẵn từ 1 đến 20
# Dùng range() và if để chỉ in ra các số chẵn từ 1 đến 20.

for number in range(1,21):
    if number%2 == 0 :
        print("Số", number, "là số chẵn")
    else:
        print("Số", number, "là số lẻ")


# Bài 2 — Classic
# FizzBuzz (1 đến 30)
# In số từ 1 đến 30. Nhưng:
# • Chia hết cho 3 → in "Fizz"
# • Chia hết cho 5 → in "Buzz"
# • Chia hết cho cả 3 và 5 → in "FizzBuzz"
# • Còn lại → in số bình thường

for number in range(1,31):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)

# Bài 3
# Đếm số chẵn và lẻ
# Với các số từ 1 đến 50, đếm xem có bao nhiêu số chẵn và bao nhiêu số lẻ, rồi in kết quả ra.

count_of_odd_num = 0
count_of_even_num = 0
for number in range(1,51):
    if number%2 != 0:
        count_of_odd_num += 1
    else:
        count_of_even_num += 1
print("Số lượng các số chẵn từ 1 đến 50 là:", count_of_even_num)
print("Số lượng các số lẻ từ 1 đến 50 là:", count_of_odd_num)


# Bài 4
# Viết function tinh_tong(a, b) nhận 2 số, trả về tổng của chúng. Sau đó gọi thử với vài cặp số khác nhau.

def sum_of_two_nums(a,b):
    return a+b

print("Tổng của 2 số 65 và 29 là:", sum_of_two_nums(65,29))

# Bài 5
# Viết function fizzbuzz(n) nhận một số n, trả về:

# "FizzBuzz" nếu chia hết cho cả 3 và 5
# "Fizz" nếu chia hết cho 3
# "Buzz" nếu chia hết cho 5
# Số n nếu không có điều kiện nào

# Sau đó dùng vòng for gọi function đó với range(1, 31).
# Bài này là tổng hợp: def + if/elif/else + for + range — viết được là nắm chắc phần cơ bản rồi đó!

def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return n

for number in range(1,31):
    print(fizzbuzz(number))

# Bài 6
# Tạo list diem_so chứa 5 điểm số bất kỳ (từ 0–10). Viết function xep_loai(diem) trả về:
# "Giỏi" nếu điểm >= 8
# "Khá" nếu điểm >= 6
# "Trung bình" nếu điểm >= 4
# "Yếu" nếu dưới 4
# Sau đó dùng vòng for in ra từng điểm kèm xếp loại.

score_list = [3,7,10,8,9,4,5,1,7,6,6,3,0]

def classify_score(score):
    if score >= 8:
        return "Giỏi"
    elif score >= 6:
        return "Khá"
    elif score >= 4:
        return "Trung bình"
    else:
        return "Yếu"

for score in score_list:
    print("Xếp loại điểm", score,"là loại", classify_score(score))

# Bài 7
# Dùng score_list của bạn, viết code:
# Tính điểm trung bình
# Đếm có bao nhiêu học sinh "Giỏi" (dùng lại function classify_score)
# In ra 2 kết quả đó

score_list = [3,7,10,8,9,4,5,1,7,6,6,3,0]

def classify_score(score):
    if score >= 8:
        return "Giỏi"
    elif score >= 6:
        return "Khá"
    elif score >= 4:
        return "Trung bình"
    else:
        return "Yếu"

def average_score(score_list):
    return sum(score_list)/len(score_list)

def count_type_student(score_list, categoryStudent):
    count_type = 0
    for score in score_list:
        if(classify_score(score) == categoryStudent):
            count_type += 1
    return count_type
print("Điểm trung bình của lớp là:", average_score(score_list))
print("Số lượng học sinh Giỏi là:", count_type_student(score_list, "Giỏi"))
print("Số lượng học sinh Khá là:", count_type_student(score_list, "Khá"))
print("Số lượng học sinh Trung Bình là:", count_type_student(score_list, "Trung bình"))
print("Số lượng học sinh Yếu là:", count_type_student(score_list, "Yếu"))

