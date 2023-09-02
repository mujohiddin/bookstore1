import requests
def send_sms(phone_number, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"

    payload = {'mobile_phone': phone_number,
               'message': message,
               'from': '4546',
               'callback_url': 'http://0000.uz/test.php'}
    files = [

    ]
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ub3RpZnkuZXNraXoudXpcL2FwaVwvYXV0aFwvcmVmcmVzaCIsImlhdCI6MTY0NjIzNjEwMSwiZXhwIjoxNjQ4ODI4MzY4LCJuYmYiOjE2NDYyMzYzNjgsImp0aSI6IkVKczRmenk3SnZ0R2hjY0QiLCJzdWIiOjUsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.QBwvovGBtnMOC0WvhC4hVJr6YTYV4bX_ixTK6SQDu4s'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.status_code)
