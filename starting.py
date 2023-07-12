import datetime
import os
import re
import shutil
import threading
import time
from multiprocessing import Pool
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")
url = 'https://asexbox.com/admin.php?mod=addnews&action=addnews'
folder_usefull = 'usefull'
folder = 'news'
usefull_list = ['Best_Of_Threesomes.txt', 'Black___White_Vol._20.txt', '1 Cock Aint Enough #1.txt']
folder_thres = f'{folder_usefull}/{usefull_list[0][:-4]}'
folder_white = f'{folder_usefull}/{usefull_list[1][:-4]}'
folder_cock = f'{folder_usefull}/{usefull_list[2][:-7]}'


def main_prog():
    try:
        for i in range(len(os.listdir(folder))):
            for file_txt in os.listdir(folder):
                if file_txt.endswith('.txt'):
                    if len(open(f'{folder_usefull}/{usefull_list[0]}').readlines()) == len(
                            open(f'{folder}/{file_txt}').readlines()):
                        print(f'True:{folder_usefull}/{usefull_list[0]}  - {folder}/{file_txt}')
                        if not os.path.exists(f'{folder_usefull}/{usefull_list[0][:-4]}'):
                            os.mkdir(f'{folder_usefull}/{usefull_list[0][:-4]}')
                        if os.path.exists(f'{folder_usefull}/{usefull_list[0][:-4]}'):

                            if os.path.exists(f'{folder}/{file_txt}'):
                                new_location = shutil.move(f'{folder}/{file_txt}',
                                                           f'{folder_usefull}/{usefull_list[0][:-4]}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Одинаковый txt файл перемещен с папки " f'{folder}/{file_txt} в папку ' f'{new_location}')



                    elif len(open(f'{folder_usefull}/{usefull_list[1]}').readlines()) == len(
                            open(f'{folder}/{file_txt}').readlines()):
                        print(f'True:{folder_usefull}/{usefull_list[1]}  - {folder}/{file_txt}')
                        if not os.path.exists(f'{folder_usefull}/{usefull_list[1][:-4]}'):
                            os.mkdir(f'{folder_usefull}/{usefull_list[1][:-4]}')
                        if os.path.exists(f'{folder_usefull}/{usefull_list[1][:-4]}'):

                            if os.path.exists(f'{folder}/{file_txt}'):
                                new_location = shutil.move(f'{folder}/{file_txt}',
                                                           f'{folder_usefull}/{usefull_list[1][:-4]}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Одинаковый txt файл перемещен с папки " f'{folder}/{file_txt} в папку ' f'{new_location}')


                    elif len(open(f'{folder_usefull}/{usefull_list[2]}').readlines()) == len(
                            open(f'{folder}/{file_txt}').readlines()):
                        print(f'True:{folder_usefull}/{usefull_list[2]}  - {folder}/{file_txt}')
                        if not os.path.exists(f'{folder_usefull}/{usefull_list[2][:-7]}'):
                            os.mkdir(f'{folder_usefull}/{usefull_list[2][:-7]}')
                        if os.path.exists(f'{folder_usefull}/{usefull_list[2][:-7]}'):

                            if os.path.exists(f'{folder}/{file_txt}'):
                                new_location = shutil.move(f'{folder}/{file_txt}',
                                                           f'{folder_usefull}/{usefull_list[2][:-7]}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Одинаковый txt файл перемещен с папки " f'{folder}/{file_txt} в папку ' f'{new_location}')
    except Exception as e:
        print(e)


def best_thresomes(folder_thres, url):
    try:
        for i in range(len(os.listdir(folder_thres))):

            for file_txt in os.listdir(folder_thres):
                if file_txt.endswith('.txt'):
                    print(file_txt)

                    with open('authentication.txt', "rt") as auth:
                        auth_text = auth.readline()

                        username, password = auth_text.strip().split(',')
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get(url=url)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(2) > input')[
                            0].send_keys(username)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(3) > input')[
                            0].send_keys(password)

                        driver.find_elements(By.CSS_SELECTOR,
                                             '#login_not_save')[
                            0].click()
                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(6) > button')[
                            0].click()

                        with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', 'r') as f:
                            old_data = f.read()

                        new_data = old_data.replace('[b]Download:[/b]', '[b]Download or Watch Online:[/b]').replace(
                            '[b]Download - Watch Online:[/b]', '[b]Download or Watch Online:[/b]')

                        with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', 'w') as f:
                            f.write(new_data)
                        rem = ('Ser', '[b]Ser')
                        new = []
                        with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', 'r') as inputFile:
                            for line in inputFile.readlines():

                                if not line.startswith(rem):
                                    print(line)
                                    new.append(line)
                        with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', 'w') as outputFile:
                            outputFile.writelines(new)

                        with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}') as file:
                            objects = file.readlines()
                            print(objects)

                            print(objects)
                            title = objects[10]
                            starrings = objects[5]
                            actors = starrings[16:-5]
                            starring = starrings[16:-4].split(',')
                            print(f'Starrings : {starring}')
                            posters = objects[0]
                            categories = objects[6]
                            studios = objects[7][11:-5]
                            year = objects[8][17:-5]

                            print(f'Studios: {studios}')
                            print(f'Year: {year}')
                            date = str(datetime.datetime.now())
                            print(date)
                            print(starring)
                            clear_titl = re.sub("[!+()’&#№]", "", title)[3:-14]

                            clean_title = f'{clear_titl}({year})'
                            if clean_title.endswith('()'):
                                clean_title = clean_title.replace('()', '')
                            else:
                                clean_title = f'{clear_titl}({year})'
                            print(clean_title)
                            clear_categories = re.sub("[!+()’&#]", "", categories)[15:-5]
                            print(f'Titles: {clean_title}')
                            print(f'Categories: {clear_categories}')
                            all_poster = []
                            row = posters.split('[/img]')
                            print(row)
                            for i in row[:]:
                                if i == '':
                                    row.remove(i)
                            for i in row:
                                c = i.replace('[img]', '')
                                all_poster.append(c)

                            picture_req = requests.get(f'{all_poster[0]}')
                            picture_req1 = requests.get(f'{all_poster[1]}')
                            print(picture_req)

                            if picture_req.status_code == 200:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()
                                

                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                os.mkdir(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f1:
                                    with open(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}',
                                              'wb') as f2:
                                        f1.write(picture_req.content)
                                        f2.write(picture_req1.content)

                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'

                                    image2 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}'
                                    print(f'Image1: {image1}', f'Image2: {image2}')
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                                    

                            elif picture_req1.status_code == 200:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()
                                

                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f:
                                    f.write(picture_req.content)
                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                                    

                                    print(f'Image1: {image1}')
                                    

                            elif picture_req.status_code == 404:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(3)')[
                                    0].click()
                                

                            shutil.rmtree(f'images/{all_poster[0][-8:]}')

                            
                            clean_star = [f'Free Porn Videos From {clear_titl},']
                            # News
                            
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#title')[
                                0].send_keys(clean_title)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(date)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')[
                                0].click()

                            
                            full_description = []
                            print(f'Full description: {full_description}')
                            with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', "r") as f:
                                lines = f.readlines()

                            with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', "w") as f:
                                for pos, line in enumerate(lines):
                                    if pos != 0 and pos != 5 and pos != 7 and pos != 8 and pos != 9:
                                        f.write(line)
                            with open(f'usefull/{usefull_list[0][:-4]}/{file_txt}', "r") as f:
                                lines = f.readlines()
                                for line in lines:
                                    full_description.append(line)
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#full_story')[
                                0].send_keys(full_description)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_actors-tokenfield')[
                                0].send_keys(actors)
                            

                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 'html body div.page-container div.page-content div.content-wrapper div.content div.panel.panel-default form#addnews.form-horizontal div.panel-tab-content.tab-content div#tabhome.tab-pane.active div.panel-body div#xfield_holder_category.form-group div.col-sm-10 div.tokenfield.form-control input#xf_category-tokenfield.token-input.ui-autocomplete-input')[
                                0].send_keys(clear_categories)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_studios-tokenfield')[
                                0].send_keys(studios)
                            
                            if year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys(year)

                                
                            elif not year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys('Until 2022')
                                

                            # Advanced
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '.fa-tasks')[
                                0].click()
                            
                            for star in starring:
                                # print(f'Starring: {starring}')
                                act = f'{star} Porn Movies'
                                clear_act = re.sub("[!+()’&#]", "", act)
                                clean_star.append(clear_act)
                            
                            cleand_star = ' '.join(clean_star).replace('  ', ',')

                            print(f'Cleaned star: {cleand_star}')
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tags-tokenfield')[
                                0].send_keys(cleand_star)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabextra > div:nth-child(1) > div:nth-child(10) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(f'Watch Online and Download Free Porn Movie {clean_title}')
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#autodescr')[
                                0].send_keys(f'Download porn videos from {clean_title} in HD Quality')
                            

                            driver.find_elements(By.CSS_SELECTOR,
                                                 'button.bg-teal')[
                                0].click()
                            if os.path.exists(f'usefull/{usefull_list[0][:-4]}/{file_txt}'):
                                new_location = shutil.move(f'usefull/{usefull_list[0][:-4]}/{file_txt}',
                                                           f'Done/{file_txt}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Обработанный txt файл перемещен с папку " f'usefull/{usefull_list[0][:-4]}/{file_txt} в папку ' f'{new_location}')

    except Exception as e:
        print(e)


def black_white_vol(folder_white, url):
    try:
        for i in range(len(os.listdir(folder_white))):
            for file_txt in os.listdir(folder_white):
                if file_txt.endswith('.txt'):
                    print(file_txt)

                    with open('authentication.txt', "rt") as auth:
                        auth_text = auth.readline()

                        username, password = auth_text.strip().split(',')
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get(url=url)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(2) > input')[
                            0].send_keys(username)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(3) > input')[
                            0].send_keys(password)

                        driver.find_elements(By.CSS_SELECTOR,
                                             '#login_not_save')[
                            0].click()
                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(6) > button')[
                            0].click()

                        with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', 'r') as f:
                            old_data = f.read()

                        new_data = old_data.replace('[b]Download:[/b]', '[b]Download or Watch Online:[/b]').replace(
                            '[b]Download - Watch Online:[/b]', '[b]Download or Watch Online:[/b]')

                        with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', 'w') as f:
                            f.write(new_data)
                        rem = ('Ser', '[b]Ser')
                        new = []
                        with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', 'r') as inputFile:
                            for line in inputFile.readlines():

                                if not line.startswith(rem):
                                    print(line)
                                    new.append(line)
                        with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', 'w') as outputFile:
                            outputFile.writelines(new)

                        with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}') as file:
                            objects = file.readlines()

                            print(objects)
                            title = objects[10]
                            starrings = objects[5]
                            actors = starrings[13:-5]
                            starring = starrings[13:-4].split(',')
                            print(f'Starrings : {starring}')
                            posters = objects[0]
                            categories = objects[6]
                            studios = objects[7][11:-5]
                            year = objects[8][17:-5]

                            print(f'Studios: {studios}')
                            print(f'Year: {year}')
                            date = str(datetime.datetime.now())
                            print(date)
                            print(starring)
                            clear_titl = re.sub("[!+()’&#№]", "", title)[3:-14]

                            clean_title = f'{clear_titl}({year})'
                            if clean_title.endswith('()'):
                                clean_title = clean_title.replace('()', '')
                            else:
                                clean_title = f'{clear_titl}({year})'
                            print(clean_title)
                            clear_categories = re.sub("[!+()’&#]", "", categories)[15:-5]
                            print(f'Titles: {clean_title}')
                            print(f'Categories: {clear_categories}')
                            all_poster = []
                            row = posters.split('[/img]')
                            print(row)
                            for i in row[:]:
                                if i == '':
                                    row.remove(i)
                            for i in row:
                                c = i.replace('[img]', '')
                                all_poster.append(c)

                            picture_req = requests.get(f'{all_poster[0]}')
                            picture_req1 = requests.get(f'{all_poster[1]}')
                            print(picture_req)

                            if picture_req.status_code == 200:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()
                                

                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                os.mkdir(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f1:
                                    with open(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}',
                                              'wb') as f2:
                                        f1.write(picture_req.content)
                                        f2.write(picture_req1.content)

                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'

                                    image2 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}'
                                    print(f'Image1: {image1}', f'Image2: {image2}')

                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                                    

                            elif picture_req1.status_code == 200:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()
                                

                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f:
                                    f.write(picture_req.content)
                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                                    

                                    print(f'Image1: {image1}')
                                    

                            elif picture_req.status_code == 404:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(3)')[
                                    0].click()
                                

                            shutil.rmtree(f'images/{all_poster[0][-8:]}')

                            
                            clean_star = [f'Free Porn Videos From {clear_titl},']
                            # News
                            
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#title')[
                                0].send_keys(clean_title)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(date)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')[
                                0].click()

                            
                            full_description = []
                            print(f'Full description: {full_description}')
                            with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', "r") as f:
                                lines = f.readlines()

                            with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', "w") as f:
                                for pos, line in enumerate(lines):
                                    if pos != 0 and pos != 5 and pos != 7 and pos != 8 and pos != 9:
                                        f.write(line)
                            with open(f'usefull/{usefull_list[1][:-4]}/{file_txt}', "r") as f:
                                lines = f.readlines()
                                for line in lines:
                                    full_description.append(line)
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#full_story')[
                                0].send_keys(full_description)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_actors-tokenfield')[
                                0].send_keys(actors)
                            

                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 'html body div.page-container div.page-content div.content-wrapper div.content div.panel.panel-default form#addnews.form-horizontal div.panel-tab-content.tab-content div#tabhome.tab-pane.active div.panel-body div#xfield_holder_category.form-group div.col-sm-10 div.tokenfield.form-control input#xf_category-tokenfield.token-input.ui-autocomplete-input')[
                                0].send_keys(clear_categories)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_studios-tokenfield')[
                                0].send_keys(studios)
                            
                            if year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys(year)

                                
                            elif not year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys('Until 2022')
                                

                            # Advanced
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '.fa-tasks')[
                                0].click()
                            
                            for star in starring:
                                # print(f'Starring: {starring}')
                                act = f'{star} Porn Movies'
                                clear_act = re.sub("[!+()’&#]", "", act)
                                clean_star.append(clear_act)
                            
                            cleand_star = ' '.join(clean_star).replace('  ', ',')

                            print(f'Cleaned star: {cleand_star}')
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tags-tokenfield')[
                                0].send_keys(cleand_star)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabextra > div:nth-child(1) > div:nth-child(10) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(f'Watch Online and Download Free Porn Movie {clean_title}')
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#autodescr')[
                                0].send_keys(f'Download porn videos from {clean_title} in HD Quality')
                            

                            driver.find_elements(By.CSS_SELECTOR,
                                                 'button.bg-teal')[
                                0].click()
                            if os.path.exists(f'usefull/{usefull_list[1][:-4]}/{file_txt}'):
                                new_location = shutil.move(f'usefull/{usefull_list[1][:-4]}/{file_txt}',
                                                           f'Done/{file_txt}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Обработанный txt файл перемещен с папку " f'usefull/{usefull_list[2][:-4]}/{file_txt} в папку ' f'{new_location}')

    except Exception as e:
        print(e)



def cock_aint_enough(folder_cock, url):

        for i in range(len(os.listdir(folder_cock))):

            for file_txt in os.listdir(folder_cock):
                if file_txt.endswith('.txt'):
                    print(file_txt)

                    with open('authentication.txt', "rt") as auth:
                        auth_text = auth.readline()

                        username, password = auth_text.strip().split(',')
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get(url=url)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(2) > input')[
                            0].send_keys(username)

                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(3) > input')[
                            0].send_keys(password)

                        driver.find_elements(By.CSS_SELECTOR,
                                             '#login_not_save')[
                            0].click()
                        driver.find_elements(By.CSS_SELECTOR,
                                             'body > div > div > div > div.panel.panel-default > div.panel-body > form > div:nth-child(6) > button')[
                            0].click()

                        with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', 'r') as f:
                            old_data = f.read()

                        new_data = old_data.replace('[b]Download:[/b]', '[b]Download or Watch Online:[/b]').replace(
                            '[b]Download - Watch Online:[/b]', '[b]Download or Watch Online:[/b]')

                        with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', 'w') as f:
                            f.write(new_data)
                        rem = ('Ser', '[b]Ser')
                        new = []
                        with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', 'r') as inputFile:
                            for line in inputFile.readlines():

                                if not line.startswith(rem):
                                    print(line)
                                    new.append(line)
                        with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', 'w') as outputFile:
                            outputFile.writelines(new)

                        with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}') as file:
                            objects = file.readlines()
                            print(objects)

                            print(objects)
                            title = objects[7]
                            starrings = objects[9]
                            actors = starrings[13:-5]
                            starring = starrings[13:-5].split(',')
                            print(f'Starrings : {starring}')
                            posters = objects[0]
                            categories = objects[10]
                            studios = objects[4][8:-1]
                            year = objects[6][17:-5]

                            print(f'Studios: {studios}')
                            print(f'Year: {year}')
                            date = str(datetime.datetime.now())
                            print(date)
                            print(starring)
                            clear_titl = re.sub("[!+()’&№]", "", title)[3:-14]

                            clean_title = f'{clear_titl}({year})'
                            if clean_title.endswith('()'):
                                clean_title = clean_title.replace('()', '')
                            else:
                                clean_title = f'{clear_titl}({year})'
                            print(clean_title)
                            clear_categories = re.sub("[!+()’&#]", "", categories)[15:-5]
                            print(f'Titles: {clean_title}')
                            print(f'Categories: {clear_categories}')
                            all_poster = []
                            row = posters.split('[/img]')
                            print(row)
                            for i in row[:]:
                                if i == '':
                                    row.remove(i)
                            for i in row:
                                c = i.replace('[img]', '')
                                all_poster.append(c)

                            picture_req = requests.get(f'{all_poster[0]}')
                            picture_req1 = requests.get(f'{all_poster[1]}')
                            print(picture_req)


                            if picture_req.status_code == 200:

                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()


                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()


                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                os.mkdir(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f1:
                                    with open(f'images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}',
                                              'wb') as f2:
                                        f1.write(picture_req.content)
                                        f2.write(picture_req1.content)

                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'

                                    image2 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[1][-7:]}/{all_poster[1][-7:]}'
                                    print(f'Image1: {image1}', f'Image2: {image2}')
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                            elif picture_req1.status_code == 200:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(5)')[
                                    0].click()
                                

                                os.mkdir(f'images/{all_poster[0][-8:]}')
                                with open(f'images/{all_poster[0][-8:]}/{all_poster[0][-8:]}', 'wb') as f:
                                    f.write(picture_req.content)
                                    image1 = os.getcwd() + f'/images/{all_poster[0][-8:]}/{all_poster[0][-8:]}'
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        0].send_keys(image2)
                                    time.sleep(0.1)
                                    driver.find_elements(By.XPATH, '//input[@type="file"]')[
                                        1].send_keys(image1)
                                    time.sleep(0.1)
                                    

                                    print(f'Image1: {image1}')
                                    

                            elif picture_req.status_code == 404:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#category_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)')[
                                    0].click()

                                
                                driver.find_elements(By.CSS_SELECTOR,
                                                     'li.active-result:nth-child(3)')[
                                    0].click()
                                

                            shutil.rmtree(f'images/{all_poster[0][-8:]}')

                            
                            clean_star = [f'Free Porn Videos From {clear_titl},']
                            # News


                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#title')[
                                0].send_keys(clean_title)

                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(date)

                            element = driver.find_element(By.CSS_SELECTOR,
                                                 '#tabhome > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)')
                            webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

                            full_description = []
                            print(f'Full description: {full_description}')
                            with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', "r") as f:
                                lines = f.readlines()
                                print(f'Lines:{lines}')

                            with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', "w") as f:
                                for pos, line in enumerate(lines):
                                    if pos != 0 and pos != 5:
                                        f.write(line)
                                        print(f'Writed lines: {line}')
                            with open(f'usefull/{usefull_list[2][:-7]}/{file_txt}', "r") as f:
                                lines = f.readlines()
                                for line in lines:
                                    full_description.append(line)
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#full_story')[
                                0].send_keys(full_description)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_actors-tokenfield')[
                                0].send_keys(actors)
                            

                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 'html body div.page-container div.page-content div.content-wrapper div.content div.panel.panel-default form#addnews.form-horizontal div.panel-tab-content.tab-content div#tabhome.tab-pane.active div.panel-body div#xfield_holder_category.form-group div.col-sm-10 div.tokenfield.form-control input#xf_category-tokenfield.token-input.ui-autocomplete-input')[
                                0].send_keys(clear_categories)
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#xf_studios-tokenfield')[
                                0].send_keys(studios)
                            
                            if year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys(year)

                                
                            elif not year:
                                driver.find_elements(By.CSS_SELECTOR,
                                                     '#xf_year-tokenfield')[
                                    0].send_keys('Until 2022')
                                

                            # Advanced
                            
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '.fa-tasks')[
                                0].click()
                            
                            for star in starring:
                                # print(f'Starring: {starring}')
                                act = f'{star} Porn Movies'
                                clear_act = re.sub("[!+()’&#]", "", act)
                                clean_star.append(clear_act)
                            
                            cleand_star = ' '.join(clean_star).replace('  ', ',')

                            print(f'Cleaned star: {cleand_star}')
                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tags-tokenfield')[
                                0].send_keys(cleand_star)

                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#tabextra > div:nth-child(1) > div:nth-child(10) > div:nth-child(2) > input:nth-child(1)')[
                                0].send_keys(f'Watch Online and Download Free Porn Movie {clean_title}')

                            driver.find_elements(By.CSS_SELECTOR,
                                                 '#autodescr')[
                                0].send_keys(f'Download porn videos from {clean_title} in HD Quality')


                            driver.find_elements(By.CSS_SELECTOR,
                                                 'button.bg-teal')[
                                0].click()
                            if os.path.exists(f'usefull/{usefull_list[2][:-7]}/{file_txt}'):
                                new_location = shutil.move(f'usefull/{usefull_list[2][:-7]}/{file_txt}',
                                                           f'Done/{file_txt}')
                                # print("% s перемещен в указанное место,% s" % (f'news/{file_txt}', new_location))
                                print(
                                    "Обработанный txt файл перемещен с папку " f'usefull/{usefull_list[2][:-7]}/{file_txt} в папку ' f'{new_location}')




if __name__ == "__main__":
    t1 = threading.Thread(target=main_prog())
    t2 = threading.Thread(target=best_thresomes(folder_thres, url))
    t3= threading.Thread(target=black_white_vol(folder_white, url))
    t4 = threading.Thread(target=cock_aint_enough(folder_cock,url))


    # main_prog()
    # best_thresomes(folder_thres, url)
    # black_white_vol(folder_white, url)

