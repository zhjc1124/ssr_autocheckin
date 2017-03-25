import requests
def checkin():
    email = input('email: ')
    password = input('password: ')

    email = email.split('@')
    email = email[0] + '%40' + email[1]

    session = requests.session()
    login_url = 'https://www.refreshss.ml/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code=&remember_me=week'
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': 'https://www.refreshss.ml/user'
    }

    response = session.post('https://www.refreshss.ml/user/checkin', headers=headers)

while True:
    try:
        checkin()
    except Exception:
        continue
    break
