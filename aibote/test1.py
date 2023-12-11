from AiBot import AndroidBotMain


# 2. 自定义一个脚本类，继承 AiBotMain
class CustomScript(AndroidBotMain):
    # 3. 设置等待参数
    # 3.1 设置等待时间
    wait_timeout = 3
    # 3.2 设置重试间隔时长
    interval_timeout = 0.5

    # 4. 重写方法，编写脚本
    # 注意：此方法是脚本执行入口
    def script_main(self):
        # 5. API 演示
        # 注意：Python 端支持的 api 与 Nodejs 基本相同
        # 此处仅演示部分 api，更多 api 请自行查阅 AiBot 文档
        # http://www.ai-bot.net/android.html

        # 截图
        self.save_screenshot("xxx.png")
        # 获取坐标点颜色
        self.get_color((100, 100))
        # 查找图片
        self.find_image("xxx.png")
        # 点击坐标
        self.click((100, 100))
        # 滑动
        self.swipe((100, 100), (200, 200), 3)