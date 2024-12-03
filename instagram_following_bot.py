from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import random, time, re, smtplib, os
from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("GMAIL_SENDER")
SENDER_PASSWORD = os.getenv("GMAIL_PASSWORD")


class InstagramFollowerBot:
    """This is an Instagram bot...duh. It is initialized to login so keep that in mind"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.login_url = "https://www.instagram.com/accounts/login/"
        self.driver = self.initialize_driver()
        self.login()

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.get(self.login_url)
        driver.maximize_window()
        # self.driver = driver
        return driver

    def login(self):
        """This function logs the user in automatically."""
        time.sleep(3)
        allow_cookies = self.driver.find_element(By.CSS_SELECTOR, value="._a9--._ap36._a9_0")
        allow_cookies.click()
        time.sleep(3)
        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.send_keys(self.username, Keys.TAB)
        time.sleep(2)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(self.password, Keys.ENTER)
        time.sleep(2)
        try:
            allow_optional_cookies = self.driver.find_element(By.CSS_SELECTOR,
                                                              value=".x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf"
                                                                    ".x193iq5w.x1r8uery.x1iyjqo2.xs83m0k.x1y1aw1k"
                                                                    ".xwib8y2.x1e558r4.x150jy0e.xgqtt45")
        except NoSuchElementException:
            pass
        else:
            allow_optional_cookies.click()
        finally:
            time.sleep(1)
        # Use Action keys to wait for the website to finish loading.

    def navigate_to_account(self, **account_details: str):
        """Provide the account_url whose followers you want to access. Only provide either the account name or the url.
        You can provide both if you want but the url will always be used first"""
        account_url = account_details["account_url"]
        account_name = account_details["account_name"]
        if account_url in account_details.values():
            time.sleep(10)
            self.driver.get(account_url)
            print("You're logged in!")
            time.sleep(4)
            followers_list = self.driver.find_element(By.CSS_SELECTOR,
                                                      value="ul.x78zum5.x1q0g3np.xieb3on li:nth-of-type(2)")
            followers_list.click()
            time.sleep(1)

        elif account_url not in account_details.values() and account_name in account_details.values():
            pass

        else:
            # None of them was passed, this should raise an error
            # TODO: LATER: See if you can raise an exception here.
            print("You must provide either a valid url or a valid username")

    def follow_accounts(self, number: int = 30):
        """This follows the accounts in the followers list of the account provided. \
        Set the number to choose how many accounts to follow. It has been set to 3 during testing.
        It might be changed to a different number during production."""

        continue_following_process = True
        accounts_followed_so_far = 0
        while continue_following_process:
            accounts_list = self.driver.find_elements(By.CSS_SELECTOR, value=f"div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja"
                                                                             f".x1lliihq.x1iyjqo2.xs83m0k.xz65tgg"
                                                                             f".x1rife3k.x1n2onr6 div:nth-of-type(2) "
                                                                             f"div div._ap3a._aaco._aacw._aad6._aade")
            for follow_account in accounts_list:
                time.sleep(2)
                if accounts_followed_so_far == number:
                    print("Thank you for using the Instagram follower bot! ;)")
                    continue_following_process = False
                    break


                try:
                    # Two things happen when we click the follow button on the web;
                    # 1. The request goes through and the follow button greys out to 'requested'.
                    # 2. A popup appears to tell us that the request is pending.
                    # In this case, the follow button remains the same, even if we keep pressing it and closing the
                    # popup, it'll keep us in a loop. Need to exit this.
                    follow_account.click()
                    time.sleep(4)

                except ElementClickInterceptedException:
                    # When the follow button is hidden by either popups, we get the above exception.
                    try:
                        # During this, we are trying to close either of the popups.
                        close_unfollow_popup = self.driver.find_element(By.CSS_SELECTOR, value="._a9--._ap36._a9_1")
                    except NoSuchElementException:
                        close_pending_popup = self.driver.find_element(By.CSS_SELECTOR, value="._a9--._ap36._a9_1")
                        close_pending_popup.click()
                        time.sleep(2)
                        continue
                    else:
                        close_unfollow_popup.click()
                        time.sleep(2)
                        continue
                else:
                    if accounts_list.index(follow_account) == len(accounts_list) - 1:
                        close_followers_list = self.driver.find_element(By.CSS_SELECTOR, value="._abl-")
                        close_followers_list.click()
                        time.sleep(1)
                        followers_list = self.driver.find_element(By.CSS_SELECTOR,
                                                                  value="ul.x78zum5.x1q0g3np.xieb3on li:nth-of-type(2)")
                        followers_list.click()
                        time.sleep(1)
                        # TODO: Run the code without the break statement below as it seems to be redundant
                        break

                    accounts_followed_so_far += 1
                    print(f"{accounts_followed_so_far} account(s) followed")
                    continue
        self.driver.quit()

    def use_new_account(self, should_continue: bool):
        """Offers the user a chance to decide if they want to continue following from a different account.
        Pass the reply from the user as an input"""
        if not should_continue:

            print("Thank you for using the Instagram follower bot! ;)")
        elif should_continue:
            self.navigate_to_account()
            number = int(input("How many accounts do you want to follow? Type '0' if you do not want to specify\n"))
            if number:
                self.follow_accounts(number=number)
            else:
                self.follow_accounts()
        else:
            print("That was not a valid response. Please try again")

    def send_email(self, account_handle, *error, accounts_followed=30):
        time.sleep(10)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            if error:
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs="abbyadjei9@gmail.com",
                                    msg=f"Subject: Instagram Bot Job Log - Unsuccessful\n\n "
                                        f"The Instagram bot ran into a bug. It will run again in 30 minutes.\n"
                                        f"See details of the error below: \n\n\n"
                                        f"{error}"
                                    )
                print("Unsuccessful Email sent successfully")
            else:
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs="abbyadjei9@gmail.com",
                                    msg=f"Subject: Instagram Bot Job Log - Successful\n\n "
                                        f"The Instagram bot run successfully. You have followed {accounts_followed}"
                                        f" accounts from {account_handle}'s account"
                                    )
                print("Successful Email sent successfully")
