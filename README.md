# Instagram-Follower-Bot

An automation tool built with Python and Selenium that automatically follows a set number of Instagram accounts from a curated list. The bot is designed to help users increase their engagement on Instagram by automating the process of following new accounts, making it easier to manage social media growth.

## Table of Contents
- Features

- Technologies

- Installation

- Usage

- Ethical Considerations

- Future Enhancements

## Features
- Automated Following: Follow a set number of accounts automatically from a predefined list.

- Customizable Parameters: Set limits for the number of accounts to follow each day, and customize delays between actions.

- Error Handling: Built-in error handling to avoid bot-like behavior and prevent detection.

- Simple User Interface: A basic command-line interface to input user preferences.

## Technologies
- Programming Language: Python

- Automation Library: Selenium

- Web Driver: ChromeDriver

- Version Control: Git/GitHub

## Installation
1. Clone the repository:

```
git clone https://github.com/AbbyAdj/Instagram-Follower-Bot.git
```
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```

3. Configure your Instagram credentials:

- Input your Instagram username and password in your .env file.
  ```
  INSTAGRAM_USERNAME = <Insert username>
  INSTAGRAM_PASSWORD = <Insert password>
  ```

4. Run the script:
   
```python main.py```

## Usage
- After running the script, it will log into Instagram using the credentials you provided.

- The bot will follow users from a list of Instagram handles provided in the configuration file.

- You can modify parameters like the number of accounts to follow or the delay time between actions to customize the bot’s behavior.

- Email Notification: Notify users when a set goal is reached or if there is an issue with the bot’s execution.

## Ethical Considerations
- Respect Instagram’s Terms of Service: This bot is intended for educational purposes only. Automated actions on Instagram may violate its terms and could result in account bans if misused.

- Use Responsibly: The bot is designed with safeguards to avoid detection and prevent excessive activity, but users should always be mindful of Instagram’s policies.

## Future Enhancements
- Entire code will be refactored in order to improve readablity.
  
- Account Filtering: Add functionality to filter accounts by specific criteria (e.g., hashtags, user type).

- Analytics Dashboard: Track which accounts the bot has followed, and display basic engagement metrics.


