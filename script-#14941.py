import uiautomator2 as u2
import time

d = u2.connect('10CD890ATZ0015H')  # 连接设备

d.app_start('com.ichi2.anki.debug')  # 启动应用
d.app_wait('com.ichi2.anki.debug')

d.click(0.1, 0.1)  # 点击左上角的菜单
d(text='卡片浏览器').click()  # 点击卡片浏览器
time.sleep(1)  # 等待1秒

#这个的bug复现过程的最后两步是点击菜单栏的“统计以后”，马上点击返回，由于实际情况需要的手速特别快，所以python脚本难以实现零点几秒的手速，
#和苏亭老师沟通后决定用0.2秒来代替，虽然实际情况脚本运行可能难以复现该bug。
d.click(0.1, 0.1)  # 点击左上角的菜单
d(text='统计').click()  # 点击统计
time.sleep(0.2)  # 等待0.2秒
d.press('back')  # 按下返回键
