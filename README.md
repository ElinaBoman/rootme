# Contents
## Root| Me
![amIresponsive](/docs/readme/readme_images/am-i-responsive.png)
### Introduction
Root me is an e-commerce store selling plants, cuttings and other plant associated things. The initial idea for Root me was to be selling cuttings instead of a alreday planted plants. This would allow customers to buy plants at a lower cost, but most importantly grow their own plants. This projects has been developed as a project for Code Institute's full stack software development course. In this project I am using HTML, CSS, JavaScript, Django, Bootstrap and Python. This project was planned with a agile development method.

The targeted audience are people who want to grow their own plants, but also for finding the perfect gift among plant lovers.

## Table of Contents

- [General](#general)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
- [UX](#ux)
  - [Development](#development)
  - [Flowchart](#flowchart)
  - [User Stories](#user-stories)
  - [Colors and Fonts](#colors-and-fonts)
  - [Wireframes](#wireframes)
- [General Features](#general-features)
  - [Features](#features)
- [Database](#database)
- [Testing](#testing)
  - [Code Validation](#code-validation)
  - [Testing User Stories](#testing-user-stories)
  - [Manual Testing](https://github.com/ElinaBoman/the-muscle-factory/blob/main/docs/readme%20docs/README-TESTING.md)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Browser Testing](#browser-testing)
- [Future Improvements](#future-improvements)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
  - [Libraries](#libraries)
    - [Packages](#packages)
  - [Framework and Websites](#framework-and-websites)
- [Deployment](#deployment)
- [Credits](#credits)


## Overview
The purpose of this project was to create a project that satisfied the assesment criteria of Code Institutes Project 5, E-commerce module. Some of the criterias were:
- Create a functioning E-commerce store
- User can checkout their products via payment system, Stripe. 
- Have authentication system for users
- Have full CRUD functionality 
- Use search engine optimization and descriptive meta tags
- User is be able to sign up to newsletters 

The criterias required three custom made models that suited the project. The models I created were 
- Wishlist

The user can store products in a wishlist by clicking the "Add to wish" button in the products view. In the wishlist view the user can see their added wishes and remove them from the wishlist.
- Contact

The user can send messages to the company from the Q&A view. The user will then recieve a confirmation email that the form has been submitted. The message will be saved into the admin panel. 
- Product

This module was a part of Code Institute walkthrough project, but I have altered it to suit this project and added fields to make it custom made. 

##### Customer goals
This project aims to create an inviting and easy navigated website for customers. To achieve this following features has been created:
- The user can search and filter trough products
- The user can create and manage their user profile.
- The user can store products that they would like to remember in a wishlist
- The user can contact Root me via a contact form
- The user can display previously created orders inside their profile
- The user can sign up to a newsletter

#### Business goals
The main goal for Root me is to find people who want to buy plants, for themself or as a gift. As a business owner it is therefore important to be able to find these people, but also having an easy to manage inventory on the website. To achieve this following features exist on the website:
- The admin can manage the store form the live site
- Collect email addresses for newsletter
- Use a payment system called Stripe
- Adding, delete and update products via Product Management link on website

To visit live website click [here! ](https://rootme-fcab110145ab.herokuapp.com/)

To visit Facebook page click [here](https://wwww.facebook.com/profile.php?id=61556797013382)

## UX
The design of the website has been created to resemble the main product, plants. The goal was to create a design that was inspired by nature with green and calming tones.
The colors used on the website are mostly green and white. The white is to keep the overall look of the website clean and adding more focus to the product. In the beginning the main background was green, but this took away too much attention from the products as the images would not stand out from the background. 
To make the product images really pop the background was set to white, which allowed the beautiful product images to really stand out.
Green elements were instead added to buttons. This created a nice balance that still had the green nature vibe but also would bring the users attention where it should be, at the products.

The green color chosen for the project is called Reseda green, which has a calming green note. Green is a difficult color to work with because too much of it does not create an appeling look. To create a more professional look some buttons have black or white background. This created a more organized over all look on the website. 

Most of the text content is black. To be able to prioritize the content on the website, the content of higher value (ex, product information) was set to black. The content that did not need the users attention straight away (ex, footer) were set to an ashy tone.

![Color-schema](/docs/readme/readme_images/theme-color.png)

## Strategy Plane
In order to create a good user experience and also strategies how to design the project I tried to answer the following questions.

 What are the User needs?
- See prices
- Get ideas for gifts
- Information about plants
- Inspiration
- See images of the plants
- Be able to buy pots and other compliments

What Features can be provided to satisfy those needs?
- Have prices and information about the plants displayed
- Offer to wrap plants as gifts, have gift cards and small presents that can be attached to the plant
- Show the plants in environments that inspires users to buy the plants
- Have categories for plants, pots and other needs

How can I make information easy to understand?
- With clear descriptive text 
- Easy layout to navigate
- Have filters for users to navigate

How can I demonstrate expertise, authoritativeness and
trustworthiness in the content?
- Professional language
- No misspellings
- Nice looking pictures that are consistent in style
- Easy to navigate website
- Clear and informative descriptions 
- Links to social medias where users can check out the business
- Have social media platforms where previous buyers can show off their plants


How can I help users to discover other relevant parts of web application?
- Links to social medias
- Have a front end that makes users want to stay on the website
- Have features that shows similar plants as the user has been interested in earlier
- Show plants that are suitable in similar environments

## Agile Methodologies
### Canban board and MosCOW Prioritization
This project has been planned with with agile methodology. Before any code was written, issues were created for both users and store owner. The issues represents fictive requirements for users and store owner. The requirements were then briefly described with acceptance criterias. This would descipe what I would need to do in order to fullfill the issue. The there is a section called Tasks that descibes what needs to be done in order for the issue to be accepted.

The issues were then prioritzed into categories according to MosCoW prioritization. I used GitHub to create structure while planing my project. I gave all my issues labels such as, Good to have, Must have and Nice to have. The Must have were required for the assessment criterias but from a users perspective. The Good to Have were to improve user experience but not required in the finished project. The Nice to have were from my own perspective of what I would like to create if there was time. As this projects is an MVP, not all issues were not finished, but all Must have were prioritized and completed.

### User Stories
**Issue nr**|**Epic**|**User Stories: As a User**|**Label**|**Finished**
-----|----|-----|-----|-----
1|Account|As a user I can create an account so that I can save order history.|Must have |YES
2|Basket|As a user I can select and add items to the shopping cart on the website so that I can buy them.|Must have |YES
3|Account|As a user I can add shipping information and update it when needed so that I can have orders delivered to my address.|Must have |YES
4|Products|As a user I can read information about products so that I can decide if the product is suitable for me.|Must have |YES
5|Basket|As a user I can update my shopping cart so that I can manage my orders.|Must have |YES
6|Basket|As a user I can delete items in my shopping cart so I can update my orders.|Must have |YES
7||AccountAs a user I can select view shipping information so that I can make sure my order is being sent to the right address.|Must have |YES
8|Products|As a user I can filter through items on the website so that it's easy to find relevant products for me.|Must have |YES
9|Active response|As a user I can easily navigate on the website and have helpful informative messages so that I can understand if my actions on the website are not working.|Must have |YES
13|Products|As a user I can filter through categories with product needs such as light/water needs so that I can easier find products for me.|Nice to have|NO
14|Basket|As a user I can add items to the shopping cart and then leave the website and still have items inside so that I can buy them later.|Good to have|YES
15|Products|As a user I can search on the website for specific products so that I can see if the website have what I'm looking for.|Must have |YES
16|Products|As a user I can select if my order is a gift so that I can gift them with nice wrapping and a card.|Nice to have|NO
17|Products|As a user I can also buy pots and dirt that are suitable for my products. I can give the best care for my products.|Good to have|YES

**Issue nr**|**User Stories: As site owner**|**Label**|**Finished**
-----|-----|-----|-----
10|Management|As a site owner I can select an add/edit/delete products on the website so that I can manage stock information.|Must have |YES
11|User information|As a site owner I can have access to user information so that I can contact customers if necessary.|Must have |YES
12|Social media|As a site owner I can link customers to our social media platform so that I can display inspiration for gift ideas, decorations and information about products.|Must have |YES
18|Products|As a site owner I can view information and make suggestions about what compliments that are good to have together with the chosen plant so that I can increase my profit.|Good to have|NO
### Implementation of User Stories 
- 1. User is able to create an account and save order history by checking the save information box in the checkout form. The Order history can then be accessed inside the user profile.
- 2. The user can add/edit and delete products in their basket.
- 3. The user can enter shipping information in checkout form. The user can also add shipping information in My profile.
- 4. The user can read about all products in the products detail section by clicking the product image. 
- 5. The user has full CRUD functionality of their shopping basket.
- 6. The user can delete product items from the shopping basket.
- 7. The user can view shipping information after the secure checkout is finished. The user will also receive an email with related information. 
- 8. On the products page the user can filter through categories by product, price or simply search for certain products in the text input field. 
- 9. The user can easily navigate on the website by using the main navigationbar. The user will receive helpful toast messages when performing actions. The input fields will provide information on what kind of inputs that are expected if the user enters wrong information. 
- 10. The store owner have full CRUD functionallity over the products and can update, edit or delete products.
- 11. The site owner will have information about the user inside the django admin panel. 
- 12. The customers can visit Root Me's Facebook page by clicking the social media link in the footer. There are also links to instagram and youtube but there is no content related to Root Me in those links.
- 14. The users basket is stored in sessions so the user can leave the site but still have their products inside the basket. This will of course not work if the user updates cash since the session disappears. 
- 15. The user can enter text input to search for products in main navigation. 
- 17. The user is able to see what pot size the plants require and then search for suitable pots. 

## Scope plane
When I started this project I realized quickly that to be able to learn and manage new techniques such as Stripe, there would not be a lot of time to focus on Nice to Have or Good to Have issues. Even though there were some features that I was very eagre to create I had to stick with an MVP. Therefore I decided on which features would be essential for the project and just made sure I finished those first.

#### Essential Features:
- User can create account
- Payment system with Stripe
- Having a working contact form
- Create a wishlist
- Having full CRUD within user shopping basket
- Having full CRUD for admin to manage products
- Users being able to update profile
- User actions are met with corresponding toast message

## Structural Plane
This project was built from a Code Institute Walkthrough project called Boutique Ado. After having all functionality in place from Boutique Ado I started to create my own project. To make this project into my own I redesigned the front end and then had my own functions on the backend. Most of the design has been built with Bootstrap.

## Skeleton & Surface Planes
### Wireframes
For this project I created Wireframes with the Balsamiq tool. I decided to do this for pages that would need more structure depending on wireframe size. The wireframes were only a tool to plan the structure and do not represent the finished product.
<details>
<summary>Home</summary>

![Home](/docs/readme/readme_images//balsamiq-home.png)
</details>

<details>
<summary>Products</summary>

![Products](/docs/readme/readme_images/balsamiq-product.png)

</details>

<details>
<summary>Contact</summary>

![Contact](/docs/readme/readme_images/balsamic-contact.png)
</details>
### Sprints - Milestones
The issues were then categorized into sprints. I tried to create a chronological order for how all my issues would be handled in a certain timeframe. This was to make sure that I would be able to finish the project on time with all the Must Have finished. Even though I had my sprints, I was not always able to follow it for various reasons. Sometimes debugging would take a lot of time and to be able to let go of the problem and move on was one of the hardest challenges, but also a valuable lesson. Creating these sprints made me realize early in the project that I had to work on time management to make sure I would at least have an MVP in the end of the project. 

**Sprint**|**Sprint**|**Start**|**Finished**
:-----:|:-----:|:-----:|:-----:
1|Project setup|5/1-24|11/1-24
2|AllAuth and Basic Navigation|12/1-24|15/1-24
3|Products views and func.|16/1-24|20/1-24
4|Shopping basket func.|21/1-24|24/2-24
5|Setting up AWS, database and deployment|25/1-24|25/1-24
6|Contact, Q&A views and funct.|25/1-24|27/1-24
7|Wishlist view and funct.|27/1-24|1/2-24
8|Overall design, colors, fonts ets...|1/2-24|2/2-2024
9|Debugging and testing|2/2-24|6/2-24
10|Read me docs|2/2-24|11/2-24

## Marketing
#### Buisiness Module
Root Me is a business-to-consumer (B2C) company. For a B2C company it is important to know who the targeted customers are and how to reach out to them.

In this project a Facebook page was created to be able to reach out to customers. The Facebook page will allow the store owner to publish campaigns and events that will attract the targeted audience.

In this fictitious e-commerce I would imagine the audience to be people of ages between 15-60 years. They are believed to enjoy working with plants as otherwise it would be easier to buy a plant and not a cutting. The audience would be people who enjoy spending time and money on their plants. The customer would be interested in information about how to take the best care of their plants. One way to satisfy the targeted audience would be to have descriptive text of how to take care of plants. On the Facebook page the owner could publish content about how to properly cut cuttings from plants, or show how to trim certain plants. For this project a newsletter subscription is available for users. The news letter could be used to tell customers about what plants are in season or advertise new products that are available in the store.

Because this is a B2C business it is important to have an easy checkout system as the users are impulsive shoppers. Therefore it is important to design the webpage to make it as easy as possible for the customers to click on a product, add it to their basket and checkout. To create greater revenue it would be a good idea to have related products, or other shoppers also bought section right before the checkout.


#### Facebook
To promote the Root Me website a Facebook site was created. Facebook allows a cheap and easy way to promote websites and companies. The Root Me Facebook pages can be used to promote sales or events and help users to find the website. This would hopefully generate greater revenue for the Root Me company.

![Facebook](/docs/readme/readme_images/facebook.png)
#### MailChimp

Users who visit the website are asked to sign up for Root Me's newsletter via MailChimp. The newsletter subscription will pop up when website is opened. I chose to do it like this because I didn't like the design of the mailchimp input field. I wanted to keep the website clean and not have this distractive form. Doing so there is no way for the user to subscribe for the newsletter if the newsletter window has been closed. The user can of course clean cash and load website again, but for a normal user this would not be obvious. This is not optimal and would be something I would work more on in the feature. The user is not forced to sign up but in the future it would be a good idea to offer some form of discounts if users sign up to the newsletter.
![Newsletter](/docs/readme/readme_images/news-letter.png)

#### SEO
Early in the project development I started researching and planning search engine optimization. I wrote down keywords that I thought would be appropriate for an e-commerce selling plant. I tried short- and long tailed words. Some of the short tailed words were: cuttings, plants, root. A few longtailed words were: Grow plants yourself, Buy plants as presents, cuttings from plants. I used Wordtracker to filter my KEYwords and
research their relevance and compare it to similar words. When I started finishing up the project I tried implementing some of these words to improve my search optimization.

Before finishing the project a sitemap.xml and robots.txt file was created to optimize search engine results. The sitemap was created with XML Site map and placed in the root directory of the project. The robots.txt file was also placed in the root directory with instructions for search engine crawlers of what folders they were allowed inside. I choose to disallow accounts and baskets for user privacy reasons.
 
Before finishing the project a sitemap.xml and robots.txt file was created to optimize search engine results. The sitemap was created with XML Site map and placed in the root directory of the project. The robots.txt file was also placed in the root directory with instructions for search engine crawlers of what foldes they were allowed inside. I choose to diallow accounts and baskets for user privacy reasons. 

### Database Schema
Early in the project I started thinking about the models that I would need in this project. I started thinking about which models should be related to each other and what kind of table it would be. Below is an early sketch of my models. They were later modified and do not represent the finished product, but the relationship between them stayed the same. The database model sketch was created with Lucidchart.

![Database models](/docs/readme/readme_images/database-models.png)

## Existing Features
### Navbar and Footer
The navbar has a clean look with easy navigation. There is a banner encouraging users to spend more money to get free delivery. The profile Fontawsome icon will change if the user is signed in. The navbar categories will not be displayed on smaller screen sizes as they will instead be placed inside a hamburger bar. 
### Footer
The footer has some contact information describing how to get in contact with Root Me. To make it easy for users who wish to contact Root Me a link has been placed inside the contact us block. The link will direct the user to the Q&A contact form. There are also links to social media, Facebook, Instagram and Youtube. At the moment it is only the Facebook link that has been connected to store related content.
### Home 
The Home page has some made up reviews displayed from happy customers. There is also a big button for users to go directly into the product section.
### Shop
Inside the shop all products are displayed. The user is able to sort the products through a sort by field. The products are represented with image, name, price and category. If the user is signed in there is also an "Add to Wishlist" button. To make it easy for the user to navigate the products page there is a "Up to Top" button along the right hand side.
### Product Detail 
By clicking the image on the products page the user is directed to the product detail page. Here the user can read a description of the chosen product. See what stage the plant is in, If it is a cutting, or if the plant has already been planted. The user can also see what pot-size the plant needs if it has already been planted. The user can start adding products in their basket by selecting Quantity and then click the Add to basket button.
The quantity select box will be disabled if the value is too low (0) or too high (99). 
### Shopping Basket
Inside the basket the user has full CRUD functionality. The user can See, read, update and delete products. When the user is ready there is a Secure Checkout button that takes the user to the Checkout form. 
### Checkout form 
Here the user can insert information about shipping and billing. Signed in users can also choose to save information to their user profile. If the user is not signed in he/she is provided with links to create an account if they wish to save contact form information. When the form has been finished the user can enter card information. To test this use the following information, Card Number: 4242 4242 4242 4242. Add then any numbers to fill out the expiration date and CVC. To test unsuccessful card payment use, Card Number: 4000 0000 0000 0002. Add any numbers to finish the input field. If the payment has been successful the user is redirected to a success view where the order and shipping information is displayed.
### User authentication
The user can commit several different actions on the website without being a registered user. However, to be able to store information the user has to register. The registration form is easy to use and will let the user know if there is anything wrong with user inputs. When the form is finished the user will receive an email to confirm the email address. When the email address has been confirmed the user can sign in.
To then sign in and sign out is very easy. The login and logout buttons are available from my profile in the main navigation bar.
### Wishlist
A signed in user is able to store products inside a wishlist. Inside the Wishlist view the user can view the product image, name and price. The user can also choose to take out the product from the Wishlist by clicking the remove link. 
### Contact 
Inside the Q&A view the user can read about normally asked questions. If the user has a question that has not been answered within the Q&A he/she is instructed to use the contact form. 

## Future Features
There are a lot of features that I would like to add. As mentioned in my issues I would like for the user to be able to sort plants into categories such as plant needs. This would be to allow users to filter plants that suit them.

I would also like to improve the wishlist in the future so the user can email their wishlist to themselves or someone else with their wishes.

I would like to have better gift planning alternatives. Where the user can enter different kinds of packaging options, adding giftcard and similar things.

I would also like to work a bit more with adding stock numbers that will inform the user/store owner if a product is finished.


## Technologies Used
### Languages Used
- HTML
- CSS
- JavaScript
- Python
- JSON

### Framework and Programs Used:
- Bootstrap
- Django
- Django-allauth

### Libraries Used
- asgiref: ASGI (Asynchronous Server Gateway Interface) 
- boto3: Intergrating AWS
- botocore: Base for boto3
- dj-database-url:  Django framework to handle database connection URLs
- django-allauth: Django framework to handle authentication
- django-countries: Django framework to handle country field
- django-crispy-forms: Django framework to handle forms
- django-storages: Django custom storage backend 
- django-summernote: Djando text-editor
- jmespath: Query language for JSON
- oauthlib: Implementation of the OAuth protocol 
- pillow: Python Imaging Library
- psycopg2: PostgreSQL adapter, database connection and transaction
- python3-openid:  Allowing implementation of an OpenID Provider
- pytz: For working with time zones
- requests-oauthlib:  Provides OAuth support for Python's requests library
- s3transfer: Python library provided by Amazon Web Services (AWS) as part of the AWS SDK for Python, Boto3
- sqlparse: Python library that provides utilities for parsing and formatting SQL
- Stripe:  API tool to accept payments online
- urllib3: Python library for making HTTP requests

Framework and Websites
- Flake8: https://flake8.pycqa.org/en/latest/ To search for errors and unused libraries.
- chatGPT: https://chat.openai.com/ For troubleshooting and writing text content.
- Pexels: https://www.pexels.com/sv-se/ To search for images.
- Google: https://www.google.com/webhp?hl=sv&sa=X&sqi=2&pjf=1&ved=0ahUKEwjD2YDFqvmDAxW_AhAIHcSrBckQPAgJ To search for information.
- CSS validator: https://jigsaw.w3.org/css-validator/ Validate CSS.
- Html validator: https://validator.w3.org/ Validate HTML.
- Jshint: https://jshint.com/ Validate javascript.
- Code Institutes py linter: https://pep8ci.herokuapp.com/ Validate Python.
- Gitpod: https://gitpod.io/workspaces API.
- GitHub: https://github.com/ Pushing all code and creating Kanban board.
- LucidChart: https://www.lucidchart.com/ For creating flowchart and database charts.
- Balsamiq: https://balsamiq.com/ To create all wireframes.
- Google Fonts: https://fonts.google.com/ To search for and borrow fonts.
- Font Awesome: https://fontawesome.com/ For borrowing font icons.
- Bootstrap: https://getbootstrap.com/ and https://getbootstrap.com/docs/5.3/getting-started/introduction/ To create classes.
- Favicon: https://favicon.io/ To create Kettlebell image - image was taken from google and then converted to favicon.
- Amazon: https://www.amazon.se/ref=nav_bb_logo - to store images
- Google Excel: https://www.google.com/sheets/about/ To create sheets for documentation.
- Heroku: https://dashboard.heroku.com/ To deploy app.
- PostgreSQL Database.
- Stack Overflow: https://stackoverflow.com/ Troubleshooting.
- W3Schools: https://www.w3schools.com/ Readin documentation.
- Youtube: https://www.youtube.com/ Link in footer and trouble shooting.
- Coolors: https://coolors.co/ To create a color chart.
- Am I responsive: https://ui.dev/amiresponsive For testing wireframes.
- Code institute tutorials/ Walkthrough project
- Lighthouse testing Creating a lighthouse report.
- Elephant SQL: https://customer.elephantsql.com/login To handle the database.
- XML Sitemap: https://www.xml-sitemaps.com/ Generate sitemap
- Rgba Color Picker: https://rgbacolorpicker.com/ color picker
- CSS Tricks: https://css-tricks.com/snippets/css/a-guide-to-flexbox/ flex box information
-  Privacy Policy Generator https://www.privacypolicygenerator.info/ Generated policy found inside the footer

## Code Validation
All validation has been documented and can be found inside the docs/readme/. There are separete folders for html, CSS, javaScript and pep8 folders.
All testing can be found [here! ](https://github.com/ElinaBoman/rootme/blob/main/TESTING.md)

### HTML Validation
All code has been passed through W3 validation service. One error was left unsolved. This error was found in checkout.html and it is believed to occur because the element that the label belongs to is inside an If statement. So this was not considered to be an error and was left unsolved. 

<details>
<summary>basket</summary>

![basket view](/docs/readme/pep8-testing/basket-p8-1.png)
</details>

### CSS validation
All CSS has been passed trough W3 validation without errors.
### JavaScript validation

### Pep 8
All Pytohn code has been passed trough CI pytohn linter.
### Python validator
All python code was tested with flake8. Some errors were left unfixed. This was because the code that would generate these errors has not been written by me. The errors occur in migrations and make_url. Some lines too long were left inside the webhook and webhook_handler because the code would malfunction if I broke it up.

## Tests
## Lighthouse
![Lighthouse](/docs/readme/lighthouse.png)
## Manual tests

## Project Bugs and Solutions:
- Saving information to user profile
There has been an issue with saving information to user profiles. The profile is saved and contains the correct information but when the form is prefilled with information it is added as a tulpe. If the fields are not cleared the tulpe will become a tulpe inside another tulpe and so on. This problem does not occur every time so it has been really hard to find the key to this error. I have printed out the information in the terminal to see what was saved to the database and it contains the right values. I also created a new database and remigrated all models to the new database. For some reason this error will still pop up sometimes. The solution to this problem would be to further investigate the code, because there is not anything wrong with the database as I have tested to use index to get only a part of the value in the input fields. This would fetch the correct information according to the index, but the information would still be inside a tulpe.
Status: Unsolved

<details>
<summary>Bug</summary>

![Bug documentation](/docs/readme/readme_images/profile-bug.png)
</details>

- Django Countries
I have a second bug that is thought to be related to the first bug. As Django Countries only accepts 2 characters inside the field. These would create big problems while going through checkout because the intent_success function would not work because the country field is too long. Like previously mentioned it is probably related to the first bug but for the code to work I chose to take out the Country field so the information will not be saved from the form. With this code left out everything worked fine.
Status: Temporarily fix, Unsolved

## Deployment
### Create Heroku app
- Install Django and Gunicorn
- Install libraries: dj_database_url and psycopg2
- Install Cloudinary Libraries
- Create requirements.txt file
- Create a project with the command django-admin startproject rootme . (replace rootme with your project name). Do not forget the ".'' In the end, it's very important.
- Create app with command: python manage.py startapp blog (Replace 'blog' with name of your app)
- To create database models run: python manage.py makemigrations
- Then run: python manage.py migrate
### Making a clone

### Before Deployment
- Set DEBUG=False in settings.py.
- Run pip3 freeze --local > requirements.txt .
- Remove env variable in Heroku settings: DISABLE_COLLECTSTATIC.
- Make sure that you have created a file called Procfile in project root. Start up command is inside Procfile and will inform Heroku how to run the app.
- Add your created apps in settings.py under INSTALLED_APPS.
- To run a website you need to add allowed_hosts under ALLOWED_HOSTS in settings.py. You
can find the hostname if you try opening up the project with: python manage.py runserver.

### Deployment to heroku
- Create a Heroku account
- Login to Heroku account
- In the dashboard choose "Create new app". It's located in the middle of the dashboard
- Give the new app a name and choose what region you are from
- When information is entered, find the tabs to Overview, Resources, Deploy, Metrics, Activity, - Access and Settings. This should be in the upper right of the site. Click the "Settings" tab
- Find the Config Vars section and click the "Reveal Config Vars" Enter information if there is hidden information in the GitHub repository. In this project a creds.json file was entered. If you don't have any hidden information in GitHub, step over the two following sections
- Inside Create config vars, enter KEYS and VALUE. Inside KEYS enter CREDS and copy and paste information from creds.json file, into VALUE. 
- Click the "Add" button
- Add a new KEY with PORT and VALUE 8000. Click the "Add" button
- Scroll down to the Buildpacks section. Click the"Add buildpack" button
- Choose buildpack Python and "Save changes". Add another buildpack with nodjs. Save changes. It is important that the buildpacks are added in the correct order. Drag and drop buildpacks if they are in the wrong order
- When buildpacks are in order. Locate the "Deploy" tab. It's found on the left side of the "Settings" tab
- In the Deployment method section, choose GitHub to connect to the repository. Confirm request to connect to GitHub
- Search for the repo-name. This is the name of the repository. Click "Search"
- Click "Connect" to link Heroku app to GitHub repository
- Scroll down to Automatic deploy section and Manual deploy section
- Choose how the project should be deployed. If Enable Automatic Deploys, Heroku rebuilds the app every time new changes are pushed inside the working environment
- If Manual deploy is chosen the current state of the project will be deployed. For this alternative click "Deploy Branch".
When the project is deployed there will be four green circles with check marks inside. There should be a message "Your app was successfully deployed.".
- Click the "View" button to see the deployed project. If steps are followed there should be a mock terminal with a project inside of it. 
Program starts automagically
### Forking the GitHub Repository
- Log in to your GitHub account, or create a account if you don't have one
- Go to the GitHub repository that you would like to fork. To find the repository, search for the repository URL inside the search bar
- At the top of the site in the right corner of the repository page there should be a button called "Fork". Click this button
- Choose where you would like to fork the repository
GitHub will then create a clone of the repository at chosen location. By default you should be directed to forked repository inside your gitHub account
### Making a Local Clone
### Setting up your local environment
### Getting Stripe keys
### Getting email variables from gmail
### Setting AWS bucket
## Credits
All product images has been borrowed from: https://gronvaxtriket.se/
I have been in contact with Gröna Växtriket who gave me permission to use their images in this project. Thank you so much for letting me use your beautiful images!

This project is built from Code Institute walk through project, Boutique Ado :
https://github.com/Code-Institute-Solutions/boutique_ado_v1

I been inspired by this everneed project: https://github.com/amylour/everneed/tree/main?tab=readme-ov-file#libraries--frameworks  in order to create wishlist app and readme documentation.

I have used chatGPT to generate information about products and to write text content in Q&A. 

As always I want to thank my mentor Brian O'Hare, who I am really going to miss after submitting this project. Thank you so much Brian for helping me on my coding journey!

Thanks to all my colleagues on slack, it has been a pleasure getting to know all of you!

I would like to thank tutoring services at Code Institute and of course Code Institute for this course.
