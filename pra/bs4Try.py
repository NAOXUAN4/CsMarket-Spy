import asyncio
import time

import re


def extract_numbers(s):
    return re.findall(r'\d+', s)


import pyppeteer
from bs4 import BeautifulSoup
from pyppeteer import launch
from SqlPart.SQLprac import writeInto


async def main():
    sysErr = 0
    executable_path = "E:\local-chromium\\1181205\chrome-win\chrome-win\chrome.exe"
    browser = await launch({'executablePath': executable_path})
    page = await browser.newPage() # 新建一个页面

    for num in range(42530,42596):  #蝴蝶刀： （42530~42596）

        try:
            await page.goto(f"https://buff.163.com/goods/{num}?from=market#tab=selling") # 访问目标网页
            html = await page.content()

            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(html, 'html.parser')
            #print(soup)

            priceSteam = soup.find_all("strong",attrs = {"class":"f_Strong"})
            priceBUFF =  soup.find_all("a",attrs = {"class":"i_Btn i_Btn_trans_bule active"})[0].text.split()
            name =  soup.find_all("h1")


            print(name[0].text.strip())

            steamP = extract_numbers(priceSteam[0].text)[0]
            uuP = extract_numbers(priceBUFF[2])[0]


            print("Steam: ",priceSteam[0].text)
            print("BUFF: ",priceBUFF[1] + priceBUFF[2])
            #print("Steam: ",steamP,'UU: ',uuP)


            writeInto(name[0].text.strip(),int(steamP),int(uuP))
            time.sleep(1)


        except:
            sysErr +=1


        print("\n")



    await browser.close()
    print("error: ", sysErr)



asyncio.get_event_loop().run_until_complete(main())
