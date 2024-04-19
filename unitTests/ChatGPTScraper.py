import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


class ChatGpt:
    def __init__(self):
        """

        """

        self.driver = None
        self.service = None
        self.options = None
        self.PATH = "C:\\Program Files (x86)\\chromedriver.exe"

        self.url = 'https://chat.openai.com/'
        self.loginUrl = 'https://chat.openai.com/login'

        # chatbox
        self.chatbox_locator = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/textarea')
        self.chatbox_element = None

        # greyed out send button
        self.button_locator = (By.CSS_SELECTOR, '[data-testid="send-button"]')
        self.button_element = None

        # first response
        self.first_responseBox_locator = (By.CSS_SELECTOR, '[data-testid="conversation-turn-3"]')
        self.first_responseBox_element = None

        # any convestaion box
        self.responseBox_locator = None
        self.conversation_element = None

        # login button
        self.login_button_locator = (By.CSS_SELECTOR, '[data-testid="login-button"]')
        self.login_button_element = None

        # google button
        self.google_button_locator = (By.CSS_SELECTOR, '[data-provider="google"]')
        self.google_button_element = None

        # email box
        self.email_box_locator = (By.ID, 'identifierId')
        self.email_box_element = None

        # password box
        self.password_box_locator = (By.NAME, 'Passwd')
        self.password_box_element = None
        self.password = ""

        # plus model
        self.plus_model_locator = (By.PARTIAL_LINK_TEXT, 'Code Wizard')
        self.plus_model_element = None

    def openChatGpt(self):
        """

        :return:
        """
        # Selenium Web Driver setup

        self.service = Service(executable_path="../chromedriver.exe")
        self.options = uc.ChromeOptions()
        self.driver = uc.Chrome(use_subprocess=True, options=self.options)

        # opening website
        self.driver.get(self.url)

        # wait for 2 seconds to simulate human
        time.sleep(2)

    def stopScraper(self):
        """

        :return:
        """
        self.driver.close()
        self.driver.quit()

    def setConversationNumber(self, conversation_number) -> None:
        """

        :param conversation_number:
        :return:
        """
        self.responseBox_locator = (By.CSS_SELECTOR, f'[data-testid="conversation-turn-{conversation_number}"]')

    def sendFirstMessage(self, message):
        """

        :param message:
        :return:
        """

        # find the element based on pre-determined locator
        self.chatbox_element = self.driver.find_element(*self.chatbox_locator)

        # click the element to simulate human interaction
        time.sleep(2)
        self.chatbox_element.click()

        # send the message
        time.sleep(2)
        self.chatbox_element.send_keys(message)

        # hitting enter
        time.sleep(2)
        self.chatbox_element.send_keys(Keys.ENTER)

        # waiting for the grey button to appear to indicate response's completion
        try:
            WebDriverWait(self.driver, 500).until(
                EC.presence_of_element_located(self.button_locator)
            )

            print('\n Response was completed')

            time.sleep(2)

            # Wait for the response to be visible

            # debug of response box
            # responseBox_locator = (By.XPATH, "//*[contains(@class, 'markdown') and contains(@class, 'prose') and contains(@class, 'w-full') and contains(@class, 'break-words') and contains(@class, 'dark:prose-invert') and contains(@class, 'dark')]")

            # ensuring the response box completion or no weird error appears
            WebDriverWait(self.driver, 500).until(
                EC.visibility_of_element_located(self.first_responseBox_locator)
            )

            print("\n Response box is completed")

            self.first_responseBox_element = self.driver.find_element(*self.first_responseBox_locator)

            # extracts first conversation box elements
            response_elements = self.first_responseBox_element.find_elements(By.XPATH, ".//*")

            # debugger
            # for text in response_texts:
            #     print(text.text)
            #     print("\n", text)

            print("\n \n Response: \n \n ")

            # prints the response
            # print(response_elements[0].text)

            chatGptResponse = response_elements[0].text

            return chatGptResponse

        except TimeoutException:
            print("Timed out waiting for response to load")


    def sendConversationMessage(self, message, conversation_number):
        """
        Send a conversation message to the chat
        :param message: send message to chat-gpt
        :param conversation_number: the odd conversation numbers are the chat gpts response
        :return: void
        """
        # find the element based on pre-determined locator
        self.chatbox_element = self.driver.find_element(*self.chatbox_locator)

        # click the element to simulate human interaction
        time.sleep(2)
        self.chatbox_element.click()

        # send the message
        time.sleep(2)
        self.chatbox_element.send_keys(message)

        # hitting enter
        time.sleep(2)
        self.chatbox_element.send_keys(Keys.ENTER)

        # waiting for the grey button to appear to indicate response's completion
        try:
            WebDriverWait(self.driver, 500).until(
                EC.presence_of_element_located(self.button_locator)
            )



            time.sleep(2)

            # Wait for the response to be visible and setting the conversation number of the desired responce box
            self.setConversationNumber(conversation_number)
            #print(self.responseBox_locator)

            # ensuring the response box completion or no weird error appears
            WebDriverWait(self.driver, 500).until(
                EC.visibility_of_element_located(self.responseBox_locator)
            )

            # finds the correct conversation box based on the responcebox locator
            self.conversation_element = self.driver.find_element(*self.responseBox_locator)

            # extracts first conversation box elements
            response_elements = self.conversation_element.find_elements(By.XPATH, ".//*")

            print('\n Response was completed')
            # debugger
            # for text in response_texts:
            #     print(text.text)
            #     print("\n", text)

            print("\n \n Response: \n \n ")

            # prints the response (needs to be the first item in array)
            # print(response_elements[0].text)

            chatGptResponse = response_elements[0].text

            return chatGptResponse

        except TimeoutException:
            print("Timed out waiting for response to load")

    def open_ChatGpt_Login_N_Plus(self):
        """

        :return:
        """
        # Selenium Web Driver setup

        self.service = Service(executable_path="../chromedriver.exe")
        self.options = uc.ChromeOptions()
        self.driver = uc.Chrome(use_subprocess=True, options=self.options)

        # opening website
        self.driver.get("https://chat.openai.com/auth/login?sso")

        # wait for 2 seconds to simulate human
        time.sleep(2)

    def accessLogin(self):
        # find the element based on pre-determined locator
        self.login_button_element = self.driver.find_element(*self.login_button_locator)

        print(self.login_button_locator)

        print("clicking login button")

        # click the button to go to login
        time.sleep(2)
        self.login_button_element.click()

        time.sleep(5)

        # click the button to go to login
        self.google_button_element = self.driver.find_element(*self.google_button_locator)

        time.sleep(2)
        self.google_button_element.click()

        time.sleep(2)

        self.email_box_element = self.driver.find_element(*self.email_box_locator)

        time.sleep(2)
        self.email_box_element.click()
        time.sleep(3)
        self.email_box_element.send_keys("kseankostage@gmail.com")
        time.sleep(3)
        self.email_box_element.send_keys(Keys.ENTER)

        time.sleep(5)

        self.password_box_element = self.driver.find_element(*self.password_box_locator)
        time.sleep(2)
        self.password_box_element.click()
        time.sleep(2)
        self.password_box_element.send_keys(self.password)
        time.sleep(3)
        self.password_box_element.send_keys(Keys.ENTER)

        time.sleep(30)

    def access_plus_model(self):
        self.plus_model_element = self.driver.find_element(*self.plus_model_locator)

        time.sleep(2)

        self.plus_model_element.click()

        time.sleep(2)

