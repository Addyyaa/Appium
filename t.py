devices = [
            {"id": "Pintura-blt-L000892", "element": '//android.widget.TextView['
                                                     f'@resource-id="com.ost.pintura:id/tv_name" and '
                                                     f'@text="Pintura-blt-L000892"]', "result": None, "second_try_result": None},
            {"id": "Pintura-blt-Ltest20", "element": '//android.widget.TextView['
                                                     f'@resource-id="com.ost.pintura:id/tv_name" and '
                                                     f'@text="Pintura-blt-Ltest20"]', "result": None, "second_try_result": None},
            {"id": "Pintura-blt-L000308", "element": '//android.widget.TextView['
                                                     f'@resource-id="com.ost.pintura:id/tv_name" and '
                                                     f'@text="Pintura-blt-L000308"]', "result": None, "second_try_result": None},
            {"id": "Pintura-blt-L000329", "element": '//android.widget.TextView['
                                                     f'@resource-id="com.ost.pintura:id/tv_name" and '
                                                     f'@text="Pintura-blt-L000329"]', "result": None, "second_try_result": None},
        ]

for device in devices:
    print(device["id"])
    with open("临时文件.txt", "a", encoding="utf-8") as f:
        f.write(f"配网：{device["id"]}-{device["result"]}\t{device["second_try_result"]}\t")