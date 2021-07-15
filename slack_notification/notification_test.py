from notification import send_message,get_config_info

def main():
    r = send_message(message='This is test message',username='test user')
    print("return ", r.json())

if __name__ == "__main__":
    main()