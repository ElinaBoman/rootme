# Contents
## Root| Me
Root me is an e-commerce store selling plants, cuttings and other plant associated things. The initial idea for Root me was to be selling cuttings instead of a allreday planted plants. This would allow customers to buy plants at a lower cost, but most importantly grow thir own plants. This projects has been developed as a project for Code Institute's full stack software development course. In this project I am using HTML, CSS, JavaScript, Django, Bootstrap and Python. This project was planned with a agile development method.

The targeted audience are people who wants to grow their own plants, but also for finding the perfect gift among plant lovers.


Project goals

Customer goals
This projects aims to create a inviting and easy navigated website for customers. To accive this following features has been created:
- The user can search and filter trough products
- The user can create and manage their user profle.
- The user can store products that they would like to remember in a wishlist
- The user can contact Root me via a contact form
- The user can display prevously created orders inside their profile
- The user can sign up to a newsletter

Business goals
The main goal for Root me is to find people who wants to buy plants, for them self or as a gift. As a business owner it is therefore important to be able to find theese people, but also having a easy to mange inventory on the website. To accive this following features exist on the website:
- The admin can manage the store form the live site
- Collect email addresses for newsletter
- Use a payment system called Stripe
- Adding, delete and update products via Product Management link on website

![amIresponsive](/media/readme/am-i-responsive.png)

[The live web site can be found here! ](https://rootme-fcab110145ab.herokuapp.com/)

## UX
The design of the website has been created to resemble the main product, plants. The goal was to create a design that was inspired by nature with green and calming tones.
The colors used on the website are mostly green and white. The white is to keep the overall look of the website clean and adding more focus to the product. In the begining the main background was green, but this took away too much attention from the products as the images would not stand out from the background. 
To make the product images really pop the background was set to white, which allowed the beautiful product images to really stand out.
Green elements where instead added to buttons. This created a nice balance that still had the green nature vibe but also would bring the users attention where it should be, at the products.

The green color choosen for the project is called Reseda green, which has a calming green note. Green is a difficult color to work with because to much of it does not create a appeling look. To create a more proffesional look some buttons have black or white background. This created a more organized over all look on the website. 

Most of the text content is black. To be able to prioritaze the content on the website, the content of higher value (ex, product information) was set to black. The content that did not need the users attention straight away (ex, footer) were set to a ashy tone.

![Color-schema](/media/readme/theme-color.png)

### Purpose
### User Stories
### Implementation of User Stories 
### Wireframes
## Apps
This project consist of six apps. Theese have all been planned out to create a good userexperience.
### Products app 
The user can see all products, filter them into different categories and add them into their basket. 
### Basket app
The user can store their products and also go to the secure checkout to purchase their products.
### User app - allauth
User can register, login and logout.
### Profile app
User can save profile information and update if needed.
### Wishlist app
User can add products to a wishlist. 
### Contact app
User can send a contact form, recieve confirmation email. The message will also be saved in the admin panel. 
## Agile Methodology
In the early stages of the product I started thinking about how to create a user firendly website and how create a proffesional impression. Theese are some of the ares I wrote down. 

Users needs:
- See prices
- Get ideas for gifts
- Information about plants
- Inspiration
- See images of the plants
- Be able to buy pots and other compliments

Features to provide those needs:
- Have prices and information about the plants displayed
- Offer to wrap plants as gifts, have gift cards and small presents that can be attached to the plant
- Show the plants in environments that inspires users to buy the plants
- Have category's for plants, pots and other needs

How to make information easy to understand and available for users:
- With clear descriptive text 
- Easy layout to navigate
- Have filters for users to navigate

How to demonstrate expertise, authoritativeness and
trustworthiness in content:
- Professional language
- No misspellings
- Nice looking pictures that are consistent in style
- Easy to navigate website
- Clear and informative descriptions 
- Links to social medias where users can check out the business
- Have social media platforms where previous buyers can show off their plants


Help users to discover other relevant parts of web application with:
- Links to social medias
- Have a front end that makes users want to stay on the website
- Have features that shows similar plants as the user has been interested in earlier
- Show plants that are suitable in similar environments
### Canban board and issues
This project has been planned with with agile methodology. Before any code was written, issues were created for both users and store owner. The issues represents fictive requirements for users and store owner. The issues were then prioritzed into categories. Good to have, Must have and Nice to have. All issues were not finished, but all Must have were completed.
![issues](/media/readme/issues.png)
![issues](/media/readme/issues-continiue.png)

To visit project canban board, follow this link:
[canban board](https://github.com/users/ElinaBoman/projects/6)

When I had created theese issues I started to plan the models that I would need in this project to be able to satisfy my issues. I also tried to start thinking about which models should be realted to eachother and what kind of table it would be. Below is an early sketch of my models. They were later modifyied and do not represent the finished product, but the relationship between them stayed the same.

![Database models](/media/readme/database-models.png)

#### SEO
Early in the project development I started reserching and planning search engined optimatization. I wrote down keywords that I thought would be appropriate for a e-commerce selling plants. I tried short- and longtailed words. Some of the shorttailed words were: cuttings, plants, root. A few longtailed words were: Grow plants yourself, Buy plants as presents, cuttings from plants. 
Then I tried reaserching thir relevance and compared it to similar words. When I started finishing up the project I tried implementing some of these words so imporve my search results.

![SEO](/media/readme/seo.png)
![SEO](/media/readme/seo-green.png)


### Sprints - milestones
## Existing Features
### Navbar and Footer
### Footer
### Shop
### Shoping Basket
### User authentication

## Future Features

There are a lot of features that I would like to add. As mentioned in my issues I would like for the user to be able to sort plants into categories such as plant needs. This would be to allow users to filter plants that suits them. 

I would also like to imporve the wishlist in the future so the user can email their wishlist to them self or someone else with their wishes. 

I would like to have better giftplanning alternatives. Were the user can enter different kinds of packagin options, adding giftcard and similar things. 

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
- asgiref
- boto3
- botocore
- dj-database-url
- Django
- django-allauth
- django-countries
- django-crispy-forms
- django-storages
- django-summernote
- jmespath
- oauthlib
- pillow
- psycopg2
- python3-openid
- pytz
- requests-oauthlib
- s3transfer
- sqlparse
- stripe
- urllib3

Framework and Websites
Flake8: https://flake8.pycqa.org/en/latest/ To search for errors and unused libraries.
chatGPT: https://chat.openai.com/ For troubleshooting and writing text content.
Pexels: https://www.pexels.com/sv-se/ To search for images.
Google: https://www.google.com/webhp?hl=sv&sa=X&sqi=2&pjf=1&ved=0ahUKEwjD2YDFqvmDAxW_AhAIHcSrBckQPAgJ To search for information.
CSS validator: https://jigsaw.w3.org/css-validator/ Validate CSS.
Html validator: https://validator.w3.org/ Validate HTML.
Jshint: https://jshint.com/ Validate javascript.
Code Institutes py linter: https://pep8ci.herokuapp.com/ Validate Python.
Gitpod: https://gitpod.io/workspaces API.
GitHub: https://github.com/ Pushing all code and creating Kanban board.
LucidChart: https://www.lucidchart.com/ For creating flowchart and database charts.
Balsamiq: https://balsamiq.com/ To create all wireframes.
Google Fonts: https://fonts.google.com/ To search for and borrow fonts.
Font Awesome: https://fontawesome.com/ For borrowing font icons.
Bootstrap: https://getbootstrap.com/ and https://getbootstrap.com/docs/5.3/getting-started/introduction/ To create classes.
Favicon: https://favicon.io/ To create Kettlebell image - image was taken from google and then converted to favicon.
Amazon: https://www.amazon.se/ref=nav_bb_logo - to store images
Google Excel: https://www.google.com/sheets/about/ To create sheets for documentation.
Heroku: https://dashboard.heroku.com/ To deploy app.
PostgreSQL Database.
EmailJS: https://www.emailjs.com/ Email function.
Stack Overflow: https://stackoverflow.com/ Troubleshooting.
W3Schools: https://www.w3schools.com/ Readin documentation.
Youtube: https://www.youtube.com/ Link in footer and trouble shooting.
Coolors: https://coolors.co/ To create a color chart.
Am I responsive: https://ui.dev/amiresponsive For testing wireframes.
Code institute tutorials/ Walkthrough project
Lighthouse testing Creating a lighthouse report.
Elephant SQL: https://customer.elephantsql.com/login To handle the database.

## Code Validation
### HTML valiation
### CSS validation
### JavaScript validation
### Pep 8
### Python validator
## Tests
## Lighthouse
## Manual tests

## Project Bugs and Solutions:

## Deployment
### Create Heroku app
- Install Django and Gunicorn
- Install libraries: dj_database_url and psycopg2
- Install Cloudinary Libraries
- Create requirements.txt file
- Create a project with command django-admin startproject rootme . (replace rootme with your project name). Do not forget the "." in the end, it's very important.
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
- To run website you need to add allowed hosts under ALLOWED_HOSTS in settings.py. You
can find the host name if you try opening up the project with: python manage.py runserver.

### Deployment to heroku
- Create a Heroku account
- Log in to Heroku account
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
- Go to GitHub repository that you would like to fork. To find the repository, search for the repository URL inside the search bar
- At the top of the site in the right corner of the repository page there should be a button called "Fork". Click this button
- Choose where you would like to fork the repository
GitHub will then create a clone of repository at chosen location. By default you should be directed to forked repository inside your gitHub account
### Making a Local Clone
### Setting up your local enviroment
### Getting Stripe keys
### Getting email variables from gmail
### Setting AWS bucket
## Credits
All product images has been borrowd from: https://gronvaxtriket.se/
I have been in contact with Gröna Växtriket who gave me permission to use their images in this project. Thank you so much for letting me use your beautiful images!

As always I want to thank my mentor Brian O'Hair, who I am really going to miss after submitting this project. Thank you so much Brian for helping me on my coding journey! 

Thanks to all my colleguages on slack, it has been a pleasure getting to know all of you!

I would like to thank tutering services at Code Institute and ofcourse Code Institute for this course. 



Heart button https://codemmit.com/likeBtn
https://getwaves.io/ waves creation footer
https://rgbacolorpicker.com/ color picker
https://css-tricks.com/snippets/css/a-guide-to-flexbox/ flex box information
