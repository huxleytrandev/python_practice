import requests

# response = requests.get("https://api.github.com/users/torvalds")

# if response.status_code == 200:
#     data = response.json()
#     print("Tên:", data["name"])
#     print("Followers:", data["followers"])
# else:
#     print("Lỗi:", response.status_code)


# Bài 1:
# Viết function get_github_user(username) nhận username, gọi API, và trả về dictionary gồm name, followers, public_repos. 
# Nếu lỗi (status không phải 200), trả về None.

def get_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "followers": data["followers"],
            "public_repos": data["public_repos"],
            "repos_url": data["repos_url"]
        }
    else:
        return None

print(get_github_user("torvalds"))
print(get_github_user("huxleytrandev"))
print(get_github_user("abc"))
