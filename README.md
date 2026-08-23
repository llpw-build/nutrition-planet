# Planet Nutrition

## Project title:

### Planet Nutrition

## Introduction:

Planet Nutrition is a sports equipment and supplements e-commerce website, that is targeted at users who are late teenagers onwards who have an interest in sporting goods. The website aims to be a one stop shop for all sporting needs, providing a clean and hassle free ordering system designed with simplicity in mind.

## Live Website

## Table of contents

## Project goals

### Site Owner Goals

- Have an easy to user e-commerce website that customers can easily use to purchase sporting goods and supplements.
- Allow customers to search, browse and filter the products on the website.
- Utiilise Stripe for secure payments.
- Ecourage footfall and user to then create accounts and purchase.
- Allow staff to be able to manage the products on the website.

### User Goals

- Easily purhcase sporting goods and supplements.
- Easily look through the products on the store.
- View their order and previous orders.
- Leave reviews on the products.
- Add and delete items from their bag.
- Create an account.

## User journey

1. User visits the website
2. Browses the products on offer
3. Selects the product and quantity
4. Adds it to the bag
5. Can then click into the bag
6. Can then go to checkout
7. Enters delivery and payment information.
8. Stripe processes all of the information.
9. Confirmation or rejection.
10. Order is saved to the user profile.

## Target Audience

The website aims to target users who are late teenagers onwards who have an interest in sporting goods and are able to make purhcases online.

## User Stories

- As a user, I want to be able to see all available products so I can easily choose which products I want.
- As a user, I want to be able to easily navigate around the website so that I have an easy user experience.
- As a user, I want to be able to see my bag total so that I know how many products I am purchasing.
- As a user, I want to be able to create an account so that I am able to save my information for future purchases.
- As a user, I want to be able to see whether my order was successful or not so that I can try again if it has failed.
- As a user, I want to be able to pay with Stripe so that I can safely complete my purhcase.
- As a user, I want an order number so that I can easily find my order.
- As a user, I want to be able to add numerous products to my bag so that I can order numerous items.
- As a user, I want to be able to update my products in my bag so that I can change the amount when needed before checkout.
- As a user, I want to be able to delete products from my bag for when I change my mind so that I can purchase the right amount.
- As a user, I want to be able to leave a review so that I can share my opinion with others.
- As a user, I want to be able to filter products so I can find the ones I want easily.
- As a staff user, I want to be able to add products so that we can sell more.
- As a staff user, I want to be able to edit products so that we can change prices.
- As a staff user, I want to be able to delete products so we can remove discontinued items.
- As a staff user, I want normal users to not be able to access staff sections so that we are not compromised.

## Features:

### Product Catalogue

The product catalogue provides the user with a clean and simple view utilising boot strap to design the ux with added CSS styling. Every product card has an image and useful information that the users can instantly see.

### Search 

A simple search capability was created to help the users find the products they require more easily. This was created also using bootstrap and styled to match the rest of the chosed colour pallete.

### Category filtering and sorting

Added category and sorting capabilites to the product catalogue to improve user experience.

### Product Details pages

Every product has a product detail page, which provides more indepth information about the product and also the ability to choose an amount and add the product to the users bag ready for checkout.

### Authentication/register/login

Authentication added throughout the project, users must be logged in to carry out certain actions such as leaving reviews, similarly users must also be marked as staff to carry out certain actions such as accessing the admin aspect of the project. Users are also able to register and create an account which can store their information and orders.

### User Profiles

The User Profile allows the user to store their information once they have created an account. They can also see their orders and the status of such order such as "paid" if the transaction has been successful.

### Shopping Bag

The shopping bag allows the user to store items and their quantity ready for purchase. The template then allows the user to either continue to checkout, update their product quantity or remove the product altogether.

### Checkout/ Stripe Payments

The checkout page allows the user to enter their information for the order and then also utilises stripe for any transactions that are carried out. A successful order provides the user with a success page, while a failed order will prompt the user as to what has gone wrong.

### Reviews

Basic review capability has been added to the website in order for users to be able to give their opinion on products. The user must be logged in and is then able to select a rating and leave a comment.

### Admin CRUD

Admin CRUD has been added, including being able to create brands, products, categories and edit things such as orders.

### UX/Design

For my project, I have chosen one of my favorite colourways which is baby blue and black. As these are stark contrasts I have also used white to offset the harshness that otherwise would have been off putting for the user.

### Bootstrap Responsive Layout

Bootstrap has been been used through the project in order to help design the site as "mobile first" and allow easy customisation throughout. 

### Navbar

A traditional Navbar has been added to the project, with links to seperate URLs and a logo that when clicked, redirects the user to home. Due to authentication the user will see different links whether they are logged in or out.

### Homepage

The homepage has the companies logo to grab the users attention, a short welcome message and slogan followed by a convenient button that will take the user to the product catalogue. If the user moves further down the page, they will see the short about us section prividfing a brief overview.

### Product Cards

Within the Product Catalogue, I used bootstrap to create product cards for a clean view of a selection of products that is responsive depending on what screen size the website is being viewed on.

### Mobile and tablet responsiveness

Depending on whether the user is viewing the project on either a mobile or tablet, the website adjusts its contents to be able to still be viewied in an appealing manner with a clean user interface.

## Wireframes

## Future Features

## Database Design

### Database Schema / ERD

### Models
#### Category
#### Brand
#### Product
#### Review
#### UserProfile
#### Order
#### OrderLineItem

### Model Relationships

## E-Commerce / Business Model
### Purpose of the Store
### Target Customer
### Products
### Customer Journey

### Technologies used

HTML
CSS
Django
Python 
Javascript
Bootstrap
SQLite
PostgreSQL 
Stripe
Github
Cloudinary
Heroku

## Testing

### Manaul Testing

I have carried out "smoke tests" numerous times, before deployment, during deployment and also after deployment while polishing my project. Numerous issues were found and resolved as I will list in the section beneath. I have also created a Feature Testing table to demonstrate these tests.

### Automated Testing

On django, you will see that I have added many tests to ensure the full django process is running while using a test environment and test database. Numerous times these tests failed, often due to wrong keys in settings. These tests range from Products (adding a product etc), Users (creating and logging in an a user), Checkout (being able to place an order successfully and testing behaviour based on whether the test succeeds or fails) and so on.

### Deployment Testing

While deploying my project to Heroku, I ran into numerous issues, mainly due to images not loading as I had not yet utilised Cloudinary, getting frequent server errors due to incorrect secret key and no Heroku PostgreSQL database migrations applied (no data). All of these have since been resolved. 

### Feature Testing

| Feature | Test | Expected Result | Actual Result | Pass/Fail |
| Navbar link | Taken to requested page | Right page displayed | Right page disoplayed | Pass |
| "Shop products" button | Taken to product catalogue | Product catalogue displayed | Product catalogue displayed | Pass |
| Product detail page | Taken to product detail | Right page and information displayed | Right page and information displayed | Pass |
| Change quantity and add to bag | Product added to bag | Right amount in bag | Right amount in bag | Pass |
| Review | Review is successfully shown | Review shown on product page | Review shown on product page | Pass |
| Save deatils to profile | Details are stored and displayed on profile | Details load correctly | Details load correctly | Pass |
| Checkout | Successfully checkout and place an order | Successful checkout | Successful checkout | Pass |
| Search | Search for existing product | Matching product displayed | Matching product displayed | Pass |
| Bag | Add valid quantity | Product added | Product added | Pass |
| Stock | Add more than available | Request rejected | Request rejected | Pass |

## Bugs

### Bugs Found During Development

### Bugs Fixed

### Known Bugs (Not fixed)

Bug where card images are not uniform could not be resolved. Tried to override CSS and on the template but could not get the images to be uniform.

## Security

### Environment Variables

Configuration values are stored as environment variables utilising .env and gitignore rather than being hardcoded into my project.

### Secret Keys

The same can be said for secret keys, as they are similarly not committed to Django for security reasons.

### DEBUG

DEBUG as required is set to False and disabled to stop users seeing debugging information.

### Authentication and Authorisation

Django authentication has been utilised throughout the project.

### CSRF Protection

CSRF protection has been utilised on POST forms.

### Staff Permissions

Admin actions have been limited to staff only. Normal users cannot access these.

## Deployment

### Local Development

### Heroku Deployment

### Environment Variables / Config Vars

### PostgreSQL

### Static Files / WhiteNoise

### Media Files / Cloudinary

### Stripe Configuration

### Database Migrations

### Fixtures / Product Data

## Version Control

### Git
### GitHub

## Credits

### Code
### Documentation
### Images
### Content
### Libraries / Frameworks
