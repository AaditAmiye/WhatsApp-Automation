import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import clipboard
from selenium import webdriver
import clipboard
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui
import subprocess
import os

from pywinauto import Application, Desktop
import os
import time


def background_ctrl_c_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("❌ File does not exist.")

    file_path = os.path.abspath(file_path)

    #  Start Explorer minimized and select the file
    app = Application(backend='uia').start(
        f'explorer.exe /select,"{file_path}"',
          # Launch minimized (invisible to user)
    )

    time.sleep(2)  # Let it load the file view

    # ✅ Get the newly opened Explorer window
    windows = Desktop(backend='uia').windows(class_name="CabinetWClass")
    if not windows:
        raise RuntimeError("❌ Could not find Explorer window.")

    explorer = windows[-1]  # Get the latest (just opened) one
    explorer.set_focus()
    time.sleep(0.5)

    explorer.type_keys("^c")

    print("✅ File copied to clipboard (Ctrl+C style).")

    time.sleep(0.5)

    # ✅ Close the Explorer window
    try:
        explorer.close()
        print("✅ Explorer closed.")
    except:
        print("⚠️ Could not close Explorer (already closed?)")






def whatsappsendmsg():
            # pyautogui.hotkey("win","ctrl","o")
            # speak("Enter name whom you want to send message")
            all_names = input("Enter name whom you want to send: ").split(",")

#             speak('Enter your message')
            msg = input("Enter your message: ")
#             speak('Enter image, file or GIF path')
            filepath = input("Enter image, file or GIF path: ")
            if filepath!="":
                background_ctrl_c_file(filepath)
            else:
                clipboard.copy(msg)

            try:
                n = 1
#                 speak('Enter the Date. press enter to send now')
                c, b, a = input("Enter the Date(D/M/YYYY): ").split("/")

#                 speak("Enter the Time")
                hr, min = input("Enter the Time(HH:MM): ").split(":")

                print("Sending......")
#                 speak("sending")

                shedule_time = datetime.date(int(a), int(b), int(c))

                while n > 0:
                    if time.localtime().tm_hour == int(hr) and time.localtime().tm_min == int(
                            min) and datetime.date.today() == shedule_time:

                        options = Options()
                        options.add_argument(
                            r"user-data-dir=C:\Users\LENOVO\AppData\Local\Google\Chrome\User Data\wtts")
                        options.add_argument("profile-directory=Default")

                        # Launch browser
                        driver = webdriver.Chrome(options=options)
                        driver.get("https://web.whatsapp.com")

                        if filepath == "":
                            for name in all_names:

                                pyautogui.press("esc")
                                search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                                search_box = WebDriverWait(driver, 50000).until(
                                    EC.presence_of_element_located((By.XPATH, search_xpath))
                                )

                                search_box.clear()
                                search_box.send_keys(name)
                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)

                                pyautogui.keyDown("ctrl")
                                pyautogui.keyDown("v")
                                pyautogui.keyUp("ctrl")
                                pyautogui.keyUp("v")

                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)
                                print("Sent")
                                # speak("sent")
                        else:
                            for name in all_names:
                                pyautogui.press("esc")
                                search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                                search_box = WebDriverWait(driver, 50000).until(
                                    EC.presence_of_element_located((By.XPATH, search_xpath))
                                )

                                search_box.clear()
                                search_box.send_keys(name)
                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)

                                pyautogui.keyDown("ctrl")
                                pyautogui.keyDown("v")
                                pyautogui.keyUp("ctrl")
                                pyautogui.keyUp("v")

                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)
                            for name in all_names:
                                pyautogui.press("esc")
                                search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                                search_box = WebDriverWait(driver, 50000).until(
                                    EC.presence_of_element_located((By.XPATH, search_xpath))
                                )

                                search_box.clear()
                                search_box.send_keys(name)
                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)

                                clipboard.copy(msg)
                                pyautogui.keyDown("ctrl")
                                pyautogui.keyDown("v")
                                pyautogui.keyUp("ctrl")
                                pyautogui.keyUp("v")
                                time.sleep(1)
                                pyautogui.press("enter")
                                time.sleep(2)
                                print("Sent")


                        time.sleep(2)
                        driver.close()
                        break


            except Exception:
                print("Sending......")
                # speak("sending")

                options = Options()
                options.add_argument(r"user-data-dir=C:\Users\LENOVO\AppData\Local\Google\Chrome\User Data\wtts")
                options.add_argument("profile-directory=Default")

                # Launch browser
                driver = webdriver.Chrome(options=options)
                driver.get("https://web.whatsapp.com")

                if filepath == "":
                    for name in all_names:
                        pyautogui.press("esc")
                        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                        search_box = WebDriverWait(driver, 50000).until(
                            EC.presence_of_element_located((By.XPATH, search_xpath))
                        )

                        search_box.clear()
                        search_box.send_keys(name)
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(2)

                        pyautogui.keyDown("ctrl")
                        pyautogui.keyDown("v")
                        pyautogui.keyUp("ctrl")
                        pyautogui.keyUp("v")

                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(2)
                        print("Sent")
                        # speak("sent")
                else:
                    for name in all_names:
                        pyautogui.press("esc")
                        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                        search_box = WebDriverWait(driver, 50000).until(
                            EC.presence_of_element_located((By.XPATH, search_xpath))
                        )

                        search_box.clear()
                        search_box.send_keys(name)
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(2)

                        pyautogui.keyDown("ctrl")
                        pyautogui.keyDown("v")
                        pyautogui.keyUp("ctrl")
                        pyautogui.keyUp("v")

                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(2)
                    for name in all_names:
                            pyautogui.press("esc")
                            search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                            search_box = WebDriverWait(driver, 50000).until(
                                EC.presence_of_element_located((By.XPATH, search_xpath))
                            )

                            search_box.clear()
                            search_box.send_keys(name)
                            time.sleep(1)
                            pyautogui.press("enter")
                            time.sleep(2)

                            clipboard.copy(msg)
                            pyautogui.keyDown("ctrl")
                            pyautogui.keyDown("v")
                            pyautogui.keyUp("ctrl")
                            pyautogui.keyUp("v")
                            time.sleep(1)
                            pyautogui.press("enter")
                            time.sleep(2)
                            print("Sent")

                        # speak("sent")

                time.sleep(2)
whatsappsendmsg()


