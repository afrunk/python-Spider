
import win32con,win32gui,time
import win32clipboard as w #剪贴板
import time

while(1):

    windowtitle = 'yi'  # 窗口名
    hwnd = win32gui.FindWindow(None, windowtitle)


    # 设置剪贴板文本
    aString = "test"
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)

    # 测试剪贴板文本
    w.CloseClipboard()
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    print(d)

    # 发送部分
    win32gui.PostMessage(hwnd,win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容(粘贴) QQ测试可以正常发送
    time.sleep(0.3)
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 向窗口发送 回车键
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


    # 实现功能部分
    print('找到%s' % windowtitle)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 窗口获取坐标
    print(left, top, right, bottom)
    print('窗口尺寸', right - left, bottom - top)
    win32gui.MoveWindow(hwnd, 20, 20, 405, 756, True)  # 改变窗口大小
    time.sleep(6)
    win32gui.SetBkMode(hwnd, win32con.TRANSPARENT)  # 设置为后台
    time.sleep(2)