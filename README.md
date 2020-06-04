# Todoist Automation Test Assignment
Initial framework for scalable automation tests for Todoist App

## Prerequiste 

- [Android Emulator](https://developer.android.com/studio/run/emulator)
- [Appium](http://appium.io/)
- [Python 3](https://www.python.org/) (Code developed in version 3.7)


## Setup

- Clone this repository

    `git clone git@github.com:strangeporcupine/todoist-setel.git`
- Install python dependancies

    `pip install -r requirements.txt`
    
- Launch instance of Android virtual device
- Launch appium server
- Fill in relevant config details in [config file](config.py). This includes Todoist Account Credentials and API Token

## Run Tests
Tests were written using [PyTest](https://docs.pytest.org/en/stable/). 

Run the following command from project root directory

`python -m pytest tests
`

