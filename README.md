# TechForge
## Table of Contents 
- [Introduction to TechForge](#introduction-to-techforge)
- [Project Purpose](#project-purpose)
- [Target Audience](#target-audience)
- [MoSCoW Methodology](#moscow-methodology)
- [User Stories](#user-stories)
- [User Experience(UX)](#user-experience-ux)
- [Design and Planning](#design-and-planning)
- [Database Schema](#database-schema)

## Introduction to TechForge
TechForge is a web-based e-commerce application. This app was developed using Django framework which allows users to login to the app, browse their desired tech products, all through a simple and user-friendly browsing menu. 

### Product Categories
TechForge is designed to provide users with access to a digital shop for the most popular tech products. Those being:
* Desktop Computers
* Laptops
* Tablets
* Mobile devices 
* Consoles
* Accessories

### User Experience

When accessing the website, users will be greeted with the login page. If they do not have an account, they can do so via the link below the form. Once their account has been created, they can browse the listed categories above via the navigation menu. TechForge provides a structured, yet easy to use shopping experience, allowing users to add items to their basket, edit how many of said item they wish to purchase, and remove items they no longer wish to buy. Once they are done, they proceed through to the checkout page. 

### E-Commerce Functionality
A key feature of TechForge is the e-commerce functionality. As users can add items to their basket, review the items and make adjustments before purchasing, and complete the transaction through an online payment system. With requiring users to log into their own account, their basket, order history, and details are linked to their individual accounts, ensuring data is secure and private.

### User Profiles

TechForge has personal profiles, in which users can view their pending orders, order history, and leave reviews. 

### Full-Stack Development Features
TechForge displays CRUD functionality, database design, user authentication, form validation, payment processing, and full-stack development concepts. This is to provide a modern online tech store, all from the comfort of the Django framework.

### Primary Goal
The main goal of TechForge is to provide users with a simple, secure, and  modern tech shop, allowing them to browse tech products, manage their shopping basket, and complete transactions through an easy-to-use platform.

## Project Purpose
TechForge focuses on bringing simplicity back into online shopping. This is achieved by removing unnecessary advertisements, promotional pop-ups and complex user interfaces, leading to a terrible UX. This application allows users to simply browse through the store stress-free, as they know exactly what they are getting. 

## Target Audience

The target audience for TechForge is anyone looking to purchase tech products. The app is not designed with a specific section in mind, for example gamers. TechForge will have something for anyone, creating a diverse portfolio of customers. While other shops use heavy advertisement and promos, TechForge forgoes all of that, to create a stress-free environment. 

Whether you are a student looking for a laptop or tablet, a gamer looking for a console or gaming PC, or someone in desperate need of a printer to print out their travel insurance, TechForge has something for their needs. This means it should appeal to a broader audience regardless of their tech knowledge or prior online shopping experience.

## MoSCoW Methodology 
For this project, I used the MoSCoW methodology to prioritise certain features throughout the development of the app. This approach was split up into three sections: Must Have, Should Have, Could Have, and Won't Have. This helped ensure that functionality was completed first, before adding extra content, making the scope of the project manageable.

## User Stories

### Must Have

#### User Registration

As a: User


I want to: Create an account on the login page.

So that: I can access the rest of the shop and purchase products

Acceptance Criteria:

* User can create an account.
* Users must provide valid information such as email address, and password. 
* Once account has been created, users can login. 
* Invalid details prompts an error message.
* Authorised users have access to the TechForge store.

#### User Login
As a: User

I want to:  Log into the account I have made.

So that:  I can acccess the TechForge shop and my saved account info.

Acceptance Criteria:
* Using valid information, such as email, users can log into their account.
* If user enters incorrect information, an error message appears.
* Users that are logged in can access TechForge.
* Additionally, users that are logged in can access their personal profile.
* Users are only logged out when they click the logout button.

#### User Logout 

As a: User

I want to: Log out of my TechForge account.

So that: My TechForge account is secure when I am finished. 

Acceptance Criteria:
* Users that are logged in can successfully log out.
* After logging out, users are redirected.
* When users are logged out, they no longer have access to TechForge.
* To regain access to TechForge, users have to login again. 
* When a user logs out, they will see a confirmation message.

#### Browse Product Categories

As a: User

I want to: Browse the various product categories.

So that: I can find the products I am interesting in browsing/purchasing.

Acceptance Criteria:
* Users will be able to see all product categories.
* In the navigation bar, categories are clearly displayed.
* Selecting a category takes the users to the specific page for that category. 
* Users will have no issues quickly navigating between categories.
* Only products belonging to that category are displayed. For example, iPhone 17 only belongs to mobile devices. 

#### View Products 

As a: User

I want to: view all available products TechForge has to offer.

So that: I can browse all available products before making purchase.

Acceptance Criteria:
* Users can see every product. 
* Products display important information, such as an image, the name of the item, and its price. 
* The layout for the products is clear. 
* Users can browse products within selected category, not displaying unrelated products. 
* Users have access to additional info if required. 

#### View Product Details

As a: User

I want to: View detailed info about a product

So that: I can decide what to purchase.

Acceptance Criteria:
* Clicking on the product brings up additional information. 
* Product info includes image of product, name, the category its in, and price. 
* Product display is easy to read. 
* Users can add the product to their basket from the product page. 
* Users have an east way of navigating back to the category page. 

#### Add Product to Basket 

As a: User 

I want to: Add products to my shopping basket. 

So that: I can purchase them when its time to checkout.

Acceptance Criteria:
* Users can successfully add products to their basket.
* Users can adjust the quantity for the items in their basket. If they want more than one laptop, they can click the button to add another. 
* When products are added to the basket, they display immediately. 
* Users can see the basket total price, and basket number has increased the second they add another product. 


#### Update Basket Quantity 

As a: User

I want to: Update the quantity of a product in my basket 

So that: my order can be updated before checking out.

Acceptance Criteria:
* Users can increase the number of products in the basket.
* Users can decrease the number of products in the basket.
* No number can go below one.
* When products are increased or decreased, basket total updates immediately. 

#### Remove Product from Basket

As a: User

I want to: Remove any product I want from the basket. 

So that: the items I no longer wish to buy are removed.

Acceptance Criteria:
* Users can completely remove products from the basket. 
* Removed items no longer appears in the basket.
* The total price of the basket adjusts when an item is removed. 
* Users can continue shopping after an item has been removed. 
* Users can re-add the product later if they change their mind.

#### Checkout 

As a: User

I want to: Complete my session through the checkout page.

So that: I can place an order on the products I selected.

Acceptance Criteria:
* Users can review basket before going to checkout.
* Users must provide all required checkout information.
* Users can complete the payment process through the online payment system. 
* When a successful payment is made, an order record is created. 
* Users receive confirmation that their order has been made successfully.
* Unsucessful payments prompts an error message.

#### View Order History 

As a: User 

I want to: view my order history.

So that: I can keep track of my orders and their details.

Acceptance Criteria:
* Users can see a full historic record of their orders.
* Users can view details of a specific order.
* Users can only see orders from their account, not other people.
* Order information includes the order id, the products, their quantities, prices, and the date of order. 
* Users have access to their order history via their profile page. 

#### Leave Product Reviews

As a: User

I want to: Leave reviews of the products I purchased.

So that: I can give my input and express my thoughts on the products.

Acceptance Criteria:
* Logged in users can leave reviews.
* Users can provide a rating and a review.
* Reviews are displayed on the product page. 
* Users can edit their own reviews at any time. 
* Users can delete their reviews.
* Users do not have access to editing or deleting reviews made by others. 

### Should Have

### Could Have

### Won't Have

## User Experience (UX)
### User Journey
Below details the user journey for both a first time visitor, and a returning visitor and how they will both interact with the application. 

#### First Time User
1. Visits the login page
2. Creates an account 
3. Logs into the system 
4. Gains access to the TechForge store
5. Browses product details and prices
6. Adds chosen products to their basket
7. Proceeds to checkout to complete purchase

#### Returning User
1. Logs into their TechForge account
2. Access the TechForge store
3. Browses product details and prices 
4. Adds chosen products to their basket
5. If needed, updates basket to amend their order
6. Completes checkout 
7. Reviews order history via their profile 
8. Leaves review on previous product purchases (optional)

### UX Goals
With TechForge, the primary goal is to create a stress-free online shopping experience that allows users to browse and quickly purchase products without all of the extra distractions you often see on shopping sites. 

TechForge focusses on: 
* Simplicity: A clean and easy-to read design that is easy to navigate.
* Clarity: Products, menu buttons, images, and more are displayed clearly and are visibly organised. 
* Effiency: Users can quickly find what they are looking for, proceed to checkout, and pay for their items in a matter of minutes. 
* Trust: Users are welcomed to a transparent experience, free of advertisements, promotional pop-ups, and continuous discount messages. 

The aim of TechForge is to free the users of distractions, focussing solely on their task, which is browsing and potentially purchasing products.
### Accessibility and Usability 

Usability and simplicity was at the core when developing the TechForge application. This app focusses on a straightforward shopping experience, allowing the user to browse products without any distractions.

The interface uses a clear and consistent layout, ensuring that the users can easily nevagiate between the login page, the main menu, and the respective category pages quickly and efficiently. The navigation bar is clear and tells the user exactly what they need to know, so that they can get on with purchasing their desired product quickly. 

Validation is also a key feature of this application, with forms throughout the store, ensisting customers adhere to the rules of the validation. For example, when creating an account with TechForge, customers must use a real email address so that we can verify the user, otherwise an error message will appear, asking the user to provide a valid email. 

Have you ever shopped on a lower tier application like Temu, that is riddled with advertisements, scams, and uneccessary information that distracts the user from their objective -- who wants to spin a wheel when they are trying to shop for trainers! 

Lastly, user accounts are protected through authentication, and those accounts can only be accessed by them. The checkout system uses a secure payment system, ensuring their finances are handled with the best care. 

## Design and Planning 
During the design and planning phase on the TechForge application, I created wireframes using Figma to give me the foundations and the vision of what the store will look like. The wireframes were used to map out the layout, clear navigation, and uncluttered pages. 

Below is an image for the following wireframes: 
* Login Page
* Home Page
* Desktop PC 
* Laptop 
* Mobile Devices 
* Tablet 
* Gaming Consoles
* Accessories 
* Checkout 

![Wireframes](assets/techforgewireframes.png)

## Database Schema

### Entity Relationship Diagram

### Category Model

### Product Model

### Profile Model

### Order Model

### Order Item Model

### Review Model

### Database Relationships