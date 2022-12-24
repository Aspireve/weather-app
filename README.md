
# Simple Weather App

Welcome to the **Simple Weather App**. This App provides you the Temperature, The Feel-Like Temperature and other basic temperature-related attributes like the Atmospheric Pressure, Humidity, Visibility, Wind Speed and so on.

To provide all this information this project uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch all the required information needed to be displayed. OpenWeatherMap API has been used because its free-to-use and easy to understand, esp. for beginners.

To display the GUI pyedifice has been used. This library has been used because of its well-wriiten [documentation](https://www.pyedifice.org/) and its easy to understand structure and most importantly its open-source nature. [GitHub repository of PyEdifice.](https://github.com/fding/pyedifice).

## App Description

On starting the application you will see the beginning screen that looks similar to the below image:

|![image](https://user-images.githubusercontent.com/93852415/209419553-50e003be-b13b-47ae-bd7a-e08057b1b28b.png)|
|:--:|
| starting page of application |

On starting this application all you need is to input the **city-name** in the searchbar provided on the top-right corner of the screen and press the **Search** button alongside the search text and VOILA! the required data will be updated on the page. 
The details once displayed will look similar to the below picture.

|![image](https://user-images.githubusercontent.com/93852415/209419725-4ee37597-c487-4b61-bb2e-d40300f94b99.png)|
|:--:|
| weather data display for *Mumbai* |

## Running this application

This application (at this moment) is guaranteed to run on [python 3.10.9](https://www.python.org/downloads/release/python-3109/). However any version of the series Python 3.10.x could be used.  

### 1. Installing this application

To download this application simply 
1. Fork this repository using the **Fork** button provided on the top-right section of the screen. The on the new page select your account as the owner and press the **Create Fork** button. This would create a copy of this project on your GitHub account.

2. On your device open the folder where you want to download this file (can be done using the cd command eg. ```cd /DirectoryWhereYouWantToInstall/``` ) or you could also use your file manager to navigate to the desired location and right-click on the file you want to save it in and select ```Open Git Bash Here```. (**Note:** you should previously have installed Git Bash. If not you could download it from [here](https://git-scm.com/downloads))

3. Now just type ```git clone https://github.com/<Your account name>/weather-app.git``` 

And now the application should be installed on your local device

### 2. getting the API key

This application uses an API to fetch the temperature data and hence an API key is needed

1. To create one wisit [OpenWeatherMap API](https://openweathermap.org/api/one-call-3)

2. On the screen scroll down till you see a component similar to the below picture and then press the [API key](https://home.openweathermap.org/users/sign_in). It is in orange and an hyperlink.

| ![image](https://user-images.githubusercontent.com/93852415/209420550-495fbc24-fa85-4ef0-ad9e-d1304a6c1370.png) |
|--|

3. Then you need to create an account on this website. by entering your email and password.

4. On creating an account an API key should be visible on your screen

|![image](https://user-images.githubusercontent.com/93852415/209420656-90f61813-0dd9-44e0-9748-c20e03632b82.png)|
|:--:|
|Your API key is in the highlighted area|

5. Copy that API key onto line 38 and replace it with ```"YOUR API KEY HERE"```. (**Note:** Enter your API Key in the open and closed inverted commas.)

### 3. Running the Application

Finally in your command prompt type ```python main.py``` [Note: for some devices you may need to run ```python3 main.py```]

Hope After Following these above steps you are able to run the application without any difficulties. If you do find any difficulties just tell me about it.

## Acknowledgement

Thanks for reading uptill here and I wish you the very best on your journey through Open Source Software.

If you feel anything should be added or something could be improved, create an issue and we surely can implement it soon.

## Thank You!!









