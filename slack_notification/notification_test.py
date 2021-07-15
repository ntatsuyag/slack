from notification import send_message,get_config_info

def main():
    TOKEN,CHANNEL = get_config_info()
    r = send_message(token=TOKEN,channel=CHANNEL,message='This is test message')
    print("return ", r.json())

if __name__ == "__main__":
    main()