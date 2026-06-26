# TechForge Testing 

This testing document outlines the manual testing done for the TechForge project. 

This file was created for the sole purpose of verifying the validity of my application, ensuring everything works as planned. For example:

* Browse various products.
* Register an account.
* Add products to a shopping basket.
* Remove items from their basket.
* Navigate to various pages.
* Add more of the same items while on the basket page.
* Successfully check out, with a working form, and Stripe model to guarantee safe payment.
* Order confirmation page, with a unique number, including the user's details they just typed on the basket page.

Below is the testing that follows the user journey. Starting with the home page, where users have the option of creating their own account for the TechForge website. 

## Testing Environment 

Testing for TechForge was carried out on the following platforms and devices:
#### Devices
The device I designed, developed, and deployed on was my Windows Desktop PC
#### Browsers
* Google Chrome
* Mozilla Firefox
#### Screen sizes
* Desktop (1920x1080)
* iPad Pro (1020x1366) (Chrome Dev Tools)
* iPhone (430x932) (Chrome Dev Tools)

## Functionality Testing 
| Test  | Expected Result | Actual Result | Pass/Fail | 
|-------------|-----------------|---------------|-----------|
| Home Page Loads | Home Page loads successfully | The page loaded successfully | Pass | 
| Register Account | Users registered an account, additionally, verified their account via email | Successfully created an account, and verified it via email | Pass | 
| Login | Registered users can login | Users successfully logged into their account | Pass | 
| Logout | Registered users can successfully logout | Users were able to successfully logout of their account | Pass | 
| Browse products | Users can view all product pages, with products displayed correctly | All products were visible on their respective pages | Pass | 
| View product details | Users can see product details when they click on a product | Product detail pages loaded, showcasing price, category, rating, and image | Pass | 
| Add product to basket | Users can add a product to basket | Users successfully added products to their basket | Pass | 
| Update basket | Users can adjust the quantity of items | Basket was adjusted based on the quantity of the items selected | Pass | 
| Remove item from basket | Items can be successfully removed | Users were able to remove items from the basket | Pass | 
| Checkout | The checkout form accepts valid information, not allowing users to proceed without it | Users could successfully check out | Pass |
| Stripe payment system | Test payment process succesfully |  Payment completed successfully | Pass | 
| Order confirmation | Order confirmation page displayed | Users could see their order comfirmation | Pass | 

## Usability Testing 
| Test  | Expected Result | Actual Result | Pass/Fail | 
|-------------|-----------------|---------------|-----------|
| Navigation Menu | Users could access each page | Navigation to pages successful | Pass | 
| Form validation | Error message prompts when incorrect information entered | An error message appeared with invalid phone number | Pass | 
| Error messages displayed | Error messages displayed correctly, for example, invalid card number for Stripe | Users prompted to enter valid card number | Pass | 
| Buttons and hyperlinks | Buttons and links are clearly labelled and work correctly | All buttons on application worked | Pass | 
| Interface | Layout is clear and easy to follow | Interface remained consistent throughout the application | Pass | 

## Responsiveness Testing 
| Test  | Expected Result | Actual Result | Pass/Fail | 
|-------------|-----------------|---------------|-----------|
| Desktop - Chrome (1920x1080) | Website displays correctly with all features working | All features of the website worked and displayed properly | Pass | 
| Desktop - Mozilla Firefox (1920x1080) | Website displays correctly with all features working | All features of the website worked and displayed properly | Pass | 
| iPad Pro (1024x1366) | Layout adjusts correctly for tablet screens | Layout adjusted correctly for tablet | Pass | 
| iPhone (430x932) | Layout adjusts correctly for iPhone | Layout adjusted correctly for tablet | Pass | 






