import urllib.request
from selenium import webdriver
import sys 

user_profile = input("\033[1;94m Enter user profile id (@username): \033[1;00m")
if user_profile.startswith('@'):
         user_profile = user_profile.replace('@','')

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/pg/' + user_profile + '/photos/?tab=albums')

if driver.title.startswith("Page not found"):    
    driver.quit()
    sys.exit("\033[1;91m Nothing found for your request.\n Exitting...\033[1;00m")

while 1:
    album_link = input("\033[1;94m Enter album link to get \033[1;95m@" + user_profile + "'s\033[1;94m images: \033[1;00m")
    number_of_imgs = input("\033[1;94m How many images you would like to get \033[1;91m(maximum 56 unique ones)\033[1;94m? \033[1;00m")
    album_name = input("\033[1;94m Enter the name of photos album: \033[1;00m")
    print("\033[1;92m Wait a seconds...\033[1;00m")
    try:
        int(number_of_imgs)
    except:
        print("\033[1;93m Enter the valid number. Exitting...\033[1;00m")
        sys.exit("\033[1;91m See you later...\033[1;00m")

    counter = 0
    counter2 = 0
    img_list = []
    src_list = []

    while counter <= int(number_of_imgs):
        try:    
            img_list.append(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div[' + str(counter) + ']/a/img'))
        except:
            pass
        try:
            img_list.append(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[' + str(counter) + ']/a/img'))
        except:
            pass 
        try:
            img_list.append(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[' + str(counter) + ']/a/img'))
        except:
            pass 
        try:
            img_list.append(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div[' + str(counter) + ']/a/img'))
        except:
            pass 
        counter = counter + 1

    while counter2 <= (int(number_of_imgs) - 1)*2:
        try:
            src_list.append(img_list[counter2].get_attribute('src'))
            counter2 = counter2 + 2
        except IndexError:
            break

    img_counter = 0
    try:
        for image in src_list:
            urllib.request.urlretrieve(src_list[img_counter], user_profile + '_' + album_name + '_' + str(img_counter))
            img_counter = img_counter + 1
    except IndexError:
        pass
    print("\033[1;92m Done!")
    user_input = input("\033[1;94m Any album else (y/n)? \033[1;00m")
    if user_input == 'n' or user_input == 'no' or user_input == 'No' or user_input == 'NO':
        break

driver.quit()
