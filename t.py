import Config


def virtural_keyboard_input(data):
    keys = Config.Config.key
    is_complete = False
    for key, value in keys.items():
        if key == data:
            print(f"press_keycode({value})")
            print(key)
            is_complete = True
            break
    if not is_complete:
        data = list(data)
        print(data)
        for i in data:
            if i in keys:
                key_code = keys[i]
                print(keys[i])
                print(f"press_keycode({key_code})")
            else:
                print("输入值没有对应的字典")






virtural_keyboard_input("USA")