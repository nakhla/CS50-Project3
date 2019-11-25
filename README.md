# Project 2

## Web Programming with Python and JavaScript
This Project is part of Harvard CS50W course provided by edx portal

## Objective
Building a web application for handling a pizza restaurant’s online orders

## Description
This project contains:
* __Menu:__ This section displays all menu items serviced in Pinnochio’s Pizza & Subs, with all available pizza and subs and other dishes with their variations of toppings, extras and items related to them also with Small and Large sizes when it is available. I used local storage to remember the last selecteed when the page is refreshe to bring the customer to the exact the same location he left.
* __Adding Items:__ Site administartor used the admin interface of django to add all menu items with required set of selections.
* __Registration, Login, Logout:__ This is accomplished using the django built in user authentication system and crispy-form to enhance forms looking using bootstrap4 classes.
* __Shopping Cart:__ from the Menu section, logged in users should be able to Add to Cart the desired selected items with their preferences from Toppings in Pizza with the permitted limit number of toppings for each one and also Extras in Subs and I took into consideration to make this setup easy to modify for price for small and large and also exapandable to add any number of extras and these extras related to which sub. also I add a remove option from Cart bulk items remove at once. shopping cart items is saved even if browser is closed or user logged out and log back in with his username.
* __Placing an Order:__ our system checks if there is already at least one item to order, then customer is able to place an order with total price of all items displayed and redirect to my orders page.
* __Viewing Orders:__  only Staff Members have access to Orders Dashboard where they can view all submitted orders and who submitted along with date and Status of order.
* __Personal Touch:__ 
    * allowing staff member or admin to change the status of a placed order and mark it as completed, canceled or refunded.
    * allowing users to ask for password reset on the login page in case user forgot his password, and an email is sent to them with Instruction to follow.
    * ```signal.py``` to create profile automaticaly with defualt image pic.
    * allowing users to remove from Cart item by item or many items at once.


## Setup yours
 ```bash
 # clone repo via git then create virtual environment on windows
 $ py -m venv env

 # activating the virtual environment
 $ .\env\Scripts\activate

 # install all dependencies packages
 $ pip install -r requirements.txt

 # add environmental variables to enable sending password reset email instructions
 # EMAIL_USER = your email
 # EMAIL_PASS = your password
 # Enable 2-factor-authentication for that gmail account

 # make migrations and start django server
 $ python manage.py migrate
 $ python manage.py runserver
 ```


## This Project by
[Magdi Nakhla](https://fb.me/nakhla)