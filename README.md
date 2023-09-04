# Selenium Automation for Senac Cloud Login and Navigation

## Overview

This repository contains a Selenium-based Python script for automating login and navigation tasks on the Senac Cloud platform. The script navigates to the login page, fills in the credentials, and performs various actions like selecting options from dropdowns and checking boxes. Post-authentication, it redirects to a specific educational action page.

## 📋 Requirements

- Python 3.x
- Selenium WebDriver
- Microsoft Edge WebDriver (`msedgedriver.exe`)
- `etapas_adicionais.py` for additional steps (optional)

## 💻 Installation

1. **Install Selenium package if you haven't**:
    ```bash
    pip install selenium
    ```
   
2. **Download Microsoft Edge WebDriver** that matches the version of your Edge browser.

3. **Place `msedgedriver.exe` in a known location on your system**.

## ⚙️ Configuration

- **Update the `driver_path` variable** with the path to your `msedgedriver.exe`.
  
  ```python
  driver_path = r'C:\Users\allan.silva\Desktop\webscraping\msedgedriver.exe'

Set your email and password in the campo_email.send_keys('xxxx') and campo_senha.send_keys('xxxx') lines.
🚀 How to Run
Clone the repository or download the Python script.

Run the script in your preferred IDE or terminal.

📜 License
This project is open-source and available under the MIT License.

✨ Features
Login automation for Senac Cloud
Dropdown selection and checkbox ticking
Navigating to a specific educational action page after authentication
Script loading check
