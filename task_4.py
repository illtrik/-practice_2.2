import requests

BASE_URL = "https://api.github.com"

def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Пользователь не найден или ошибка запроса.")
        return None
    data = response.json()
    profile = {
        'name': data.get('login'),
        'html_url': data.get('html_url'),
        'public_repos': data.get('public_repos'),
        'followers': data.get('followers'),
        'following': data.get('following'),
    }
    return profile

def get_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Ошибка при получении репозиториев.")
        return []
    repos_data = response.json()
    repos = []
    for repo in repos_data:
        repos.append({
            'name': repo['name'],
            'html_url': repo['html_url'],
            'watchers_count': repo['watchers_count'],
            'language': repo['language'],
            'private': repo['private'],
            'default_branch': repo['default_branch']
        })
    return repos

def search_repos(username, search_name):
    repos = get_repos(username)
    filtered = [r for r in repos if search_name.lower() in r['name'].lower()]
    return filtered

def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    profile = get_user_profile(username)
    if not profile:
        return
    print(f"\nПрофиль {profile['name']}:")
    print(f"Ссылка: {profile['html_url']}")
    print(f"Репозитории: {profile['public_repos']}")
    print(f"Подписчики: {profile['followers']}")
    print(f"Подписки: {profile['following']}")

    print("\nСписок репозиториев:")
    repos = get_repos(username)
    for r in repos:
        visibility = "Приватный" if r['private'] else "Публичный"
        print(f"{r['name']} ({visibility}) - {r['language']} - просмотров: {r['watchers_count']} - Ветка по умолчанию: {r['default_branch']} \n  Ссылка: {r['html_url']}")

    search = input("\nВведите часть названия репозитория для поиска (или Enter для пропуска): ").strip()
    if search:
        results = search_repos(username, search)
        print(f"Результаты поиска по '{search}':")
        for r in results:
            print(f"{r['name']} - {r['html_url']}")
    else:
        print("Поиск пропущен.")

if __name__ == "__main__":
    main()