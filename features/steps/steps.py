from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@step('I open the browser')
def open_browser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options)
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

@step('I open "{url}"')
def open_url(context, url):
    context.driver.get(url)

@when('I type "{NovelName}" in the search box')
def searching(context, NovelName):
    search_box = context.driver.find_element(By.XPATH,"""//*[(@id = "searchinput")]""")
    search_box.clear()
    search_box.send_keys(NovelName)
    search_box.submit()

@then('I should {state} "{text}" as one of search results')
def search_result(context, state, text):
    results = context.driver.find_elements(By.XPATH, """//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a""")
    exists = True if text in [i.text for i in results] else False
    if state == "see":
        assert exists
    else: #state == "NOT see"
        assert not exists



@step('I should {state} myself logged in as "{user_name}"')
def logged_in(context, state, user_name):
    login_btn = context.driver.find_element(By.XPATH,"""//*[(@id = "loginbtn")]""")

    hov = ActionChains(context.driver).move_to_element(login_btn)
    hov.perform()

    temp = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "name", " " ))]//a""")
    if state == "see":
        assert True if len(temp) == 1 else False
    else: #state == "NOT see"
        assert False if len(temp) == 1 else True

@when('I bookmark it as {state}')
def bookmarking(context, state):
    bookmark_btn = context.driver.find_element(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "bookmark--trigger", " " ))]""")
    hov = ActionChains(context.driver).move_to_element(bookmark_btn)
    hov.perform()

    target_btns = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "bookmark__popup-list__item system active", " " ))]""")
    for i in target_btns:
        if i.text == state:
            target_btn = i
            break
    hov = ActionChains(context.driver).move_to_element(target_btn)
    hov.perform()

@then('I should see "{novelname}" bookmarked as {state}')
def check_bookmark(context, novelname, state):
    tab = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "system", " " ))]""")
    for i in tab:
        if state in i.text:
            i.click()
            break

    exists = False
    novels = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "fav_story_title", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ellipses", " " ))]""")
    for novel in novels:
        if novel.text == novelname:
            exists = True
            break

    assert exists

@then('I should remove "{novelname}" bookmark as {state}')
def remove_bookmark(context, novelname, state):
    exists = False
    novels = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "fav_story_title", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ellipses", " " ))]""")
    btns = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "bookmark--trigger", " " ))]""")

    for i in range(len(novels)):
        novel = novels[i]
        if novel.text == novelname:
            exists = True
            hov = ActionChains(context.driver).move_to_element(btns[i])
            hov.perform()
            break

    if exists:
        state_list = context.driver.find_elements(By.XPATH,"""//*[contains(concat( " ", @class, " " ), concat( " ", "bookmark__popup-list__item system active", " " ))]""")
        for state_btn in state_list:
            if state_btn.text == state:
                hov = ActionChains(context.driver).move_to_element(state_btn)
                hov.perform()
                break

    assert exists


@step('I try to log in with "{user_name}" and "{password}"')
def try_login(context, user_name, password):
    login_btn = context.driver.find_element(By.XPATH,"""//*[(@id = "loginbtn")]""")
    login_btn.click()

    user_box = context.driver.find_element(By.XPATH,"""//*[(@id = "login_name")]""")
    user_box.clear()
    user_box.send_keys(user_name)

    password_box = context.driver.find_element(By.XPATH,"""//*[(@id = "login_password")]""")
    password_box.clear()
    password_box.send_keys(password)

    password_box.submit()