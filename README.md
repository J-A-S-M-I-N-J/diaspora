# Diaspora
Diaspora is a webpage for and by the creative collective 'Diaspora' who are a group of artists/musicians/DJ's in Stockholm active in the nightlife scene. 
On the site you can find our music, buy our merchandise read about events and contact us through a booking page. 

You can find the live site [here](https://diaspora-webpage.herokuapp.com/)

![Main site image](docs/readme-header-image.PNG)

---
---
# Contents
  + [Design](#design)
    + [Overall Feel](#overall-feel)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
  + [Wireframes and Initial Design](#wireframes-and-initial-design)
    + [Wireframes](#wireframes)
    + [Design Mock Up](#design-mock-up)
+ [Features](#features)
  + [Current Features](#current-features)
  + [Possible Future Features](#possible-future-features)
  + [Defensive Design Features](#defensive-design-features)
+ [Database](#database)
+ [Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Frameworks and Libraries](#frameworks-and-libraries)
  + [All Others](#all-others)
+ [Testing](#testing)
+ [Deployment](#deployment)
  + [Heroku Deployment](#heroku-deployment)
  + [Set up AWS](#set-up-aws)
  + [Set up Emails](#set-up-emails)
  + [Forking the Repository](#forking-the-repository)
  + [Making a Local Clone](#making-a-local-clone)
+ [Credits](#credits)
  + [Content](#content)
  + [Media](#media)
  + [Acknowledgements](#acknowledgements)
---
---

## Design
### Overall Feel & Colors

The webpage follows our graphic profile made by one of the members of the collective. Minimalistic with black and white elements that makes it easy to read and the color purple makes appearances on some links/borders since that is our signature color for when we host events. 


### Typography
I chose the [Syne](https://fonts.google.com/specimen/Syne) font for the text headers throughout the site. We usually use Druk for our content so this one was the closest I could find to it for free. 

I chose the [Alata](https://www.dafont.com/milestone-outline.font) to go with it, since they seemed to match very well with Syne. 

### Imagery

The imagery throughout the site will be primarily dictated by the products for sale. These are photos that we have shot ourselves with the different products and some of the close friends that we have. 

We have also had the opportunity to take some photos on ourselves that we use for the index page as image-links. And one of our crew-members also brought some of our merch with them to Gambia and that photo is on the about page. 

Our custom logo is also seen at the top left of the page on desktop views.

## Wireframes and Initial Design

[Initial wireframes here](https://drive.google.com/file/d/1ODMEJtHFIueQqgr1Jqb_9lwYfMesSUnF/view?usp=sharing)

All Wireframes were designed for laptop/computer, iPad/tablet and phone display:

As the project progressed, some element placement were tweaked and updated. However, I think that the layout changes were not so drastic that they warrented new wireframes to be designed. 

---
---

# Features
## Current Features
### **Navigation menu and header displayed across all pages**

The header buttons under My Account update depending on whether a user is logged in or not, and whether that user is the admin:

Admins/Superusers have the possibility to manage products whilst others don't. If you're logged in or not it will display Register or Login, or logout/my profile. 

The navigation menu will help the user move easily across all pages. It has all the links to the different pages. On desktop it stretches by the lenght of the page but on mobile it becomes a hamburger-menu with a drop-down function. 

### **User registration not required**

I think not giving people 'extra-steps' to do whilst shopping online increase the probability of a purchase, therefore even people without registration can purchase our merch. 

Even if a user doesn't have an account, they are still able to purchase, input a delivery address and have a confirmation email sent to them when they have completed a purchase. 

### **User profile creation**

A user has an option to create an account if they want to. 
Registration process:

+ Username
   + A user can choose a username as long as it hasn't already been taken
   + The user will receive an error notification immediately if their username has already been taken

+ Email address
   + A user needs to sign up using an email address
   + The email has to be inputted twice to avoid typo issues
   + This triggers an automatic email to be sent to the user to confirm the email address as correct and set up the account. 

+ Password
   + The password has to be inputted twice to avoid typo issues

With a user profile: 
+ the user can like blog-content. 
+ order history is saved & displayed in their profile.
+ Save default delivery information to their profile from the checkout page.
+ Update default delivery information to their profile from their profile page.

---

### **Products Page**

All users can browse through the available products.
Products can be sorted by:
+ Price
+ Name

If a user wants to know more about a product, they can click it and open the product detail page.

---

### **Product Details Page**

From the product detail page, the user can view:
+ Product name
+ Product price 
+ Product description 

The user can can then either go back to the products page, add a single item to ther bag or adjust the quantity to add to the bag

---

### **Artists Page**

All users can browse through the artists. Where small bio-text is provided about them the page provides a link to the 'latest music' they have dropped. 

---

### **Latest Music Page**

From the latest music page, the user can view:
+ Track names
+ Track Lenghts
+ Other info about the song/EP.

At the bottom of the artist specific songs/EPs is an external link (usually to bandcamp, soundcloud or spotify.)

---

### **About Page**

This is a page where we explain who we are and what our purpose here is. 

---

### **Blog**

On the blog page the user can read about events or things related to music/culture that we or some of our guest writers will be writing about. 
This page is a landing page where you can furhter click on specific blog posts you would like to read about.

---

### **Blog Detail Page**

This is where the user can actually read about the different topics, and if you're logged in you can like the posts. 
Admins can delete / edit any of these and there is a possbility for future implementation to create 'writer-accounts' who would have that same functionality. 

---

### **Admin CRUD functionality**

As well as all of the abpve features(read), the admin can add, edit and delete products, artists and classes from the site - they don't have to visit the admin panel for this. 
+ Add(*Create*): 
From the 'My Account' dropdown, the admin can choose 'Product Management' This allows them to create the item by filling in the form.

+ Edit(*Update*): 
From the item detail page, the admin has an edit button that will direct them to the edit page. All of the form fields will be populated with the item information that can then be updated and saved. 

+ Delete(*Delete*)
From the item detail page, the admin has a delete button that will trigger a confirmation modal. Once the admin confirms deletion, the item will be removed from the database

This functionality exists for both the blog pages and the product pages, although the blog posts can't be edited from the 'My Account' view, and is instead done on the blog and blog_detail views. 

---

### **Bag**

A user can open the bag page at any point and see what items thay have in there. 

From here a user can update product quantities, remove items from the bag or access the checkout page. 

Currently there is a bug on the quantity-updating where the decrement/increment buttons don't work. 

---

### **Checkout**

The checkout page allows the user to:
+ use their default delivery address(if they have an account, are logged in and have saved those details)
+ input new delivery information if needed or are checking out as a guest
+ update their profile with the inputted edlivery information(if they have an account and are logged in)
+ Pay via Stripe for secure payments
+ A loading screen will appear when a payment is being processed to stop the user clicking away
+ If the payment form doesn't submit properly or the user closes the browser during the wait animation, Stripe will still create the order for the user. 
+ An email wil be sent to the user with their order confirmation

---

### **Booking page**

The user can fill out a contact form and send a message to the site admin. This will send an email directly to the admin's email rather than to the admin console. 

---

### **Contact page**

The user can browse through the Contact page where you can find out where to reach us, sign up to the newsletter, read our Terms & Conditions and then also some external links that might be of interest. 

---

### **Footer **

The footer has links to our facebook page and our instagram-page. It also has a link to newsletter-signup and our Terms & Conditions.

---

### **Terms & Conditions **

This page has a accordion-drop-down-function that keeps all the different paragraphs regarding our terms & conditions to use / purchase from the site. 

---

### **Emails**

The site will send real emails when needed:

+ New customer registration
+ Order confirmation
+ User submits a query through the booking page
---

### **Toasts**

There are four types of toasts that are displayed to the user when specific actions happen. This keeps the user informed about what is happening when it happens. The toasts are:

+ Success
   + When a user sucessfuly signs in/signs out
   + When a user adds a product to a bag
   + When an admin adds/edits items
+ Info
   + When a user is viewing previous order details
+ Warning
   + Stripe key not found 
+ Error
   + When an admin's CRUD action fails


---

## Possible Future Features
+ A artist profile page where you can see all of the music they have and links to external sites like instagram etc. 
+ Ability to 'star' products to a users own account to refer back to.
+ Donate page to help fund events/music.
+ Featured content on Index page, like 'latest blog post' or 'latest song release'. 

## Defensive Design Features

Below are the steps that I have taken with regards to defensive design:

+ Form validation:
   + If incorrect data is added to a form, the form won't submit and a warning will appear to the user
   + Image files are vefified by Django's ImageField

+ Adding products to bag:
   + A user cannot add more than the amount of quantity there is on an item. This is a model, and quantity is added through admin.
   + A user cannot add 0 quantity of a product

+ Default images:
   + The images have been set to required but if for any reason this fails, there is a default image that will take it's place

+ Custom error pages:
   + A 404 error page will show if the user treis to visit a page that doesn't exist. There are buttons on the page for the user to redirect themselves
   + A 500 error page will show if an internal server error occurs on the site.

+ Authenticated vs unauthenticated user pages:
   + The @login_required decorator has been used to make sure that secure pages stay off limites to unauthenticated users

---

---

# Database

Two relational databases were used to create this site - during production SQLite was used and then ElephantSQL was used for the deployed Heroku version. 
Below is an image of how the database models relate to each other:

## Products

+ This model stores the product details that the user can buy from the site
+ This model sends information to the OrderLineItem model to create the purchase

## Inventory

+ This model keeps track of the quantity of products in order to determine if items are out of stock and stops users from purchasing more products than we have.

## Artists

+ This model stores the artist details that the user can browse through

## OrderLineItem

+ This model stores a product that has been added to the users bag
+ This model pulls information from the products model to add them to the users order
+ This model sends information to the Order model to update the order information

## Order

+ This model stores the full order information
+ This model pulls information from the OrderLineItem model to add products to the order
+ This model pulls information from the UserProfile model to attach the order to their profile

## UserProfile

+ This model stores the users delivery and order information
+ This model pulls information from the User model to create the profile
+ This model sends information to the Order model to attach the order to their profile

## User

+ This model stores the user registration information
+ This model sends information to the UserProfile model to create the profile

# Deployment

## Apps / Programs

This project was deployed through Heroku.
It uses AWS for media files. 
Elephant SQL for database. 
Stripe used for the payments system.

---
---

# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](https://github.com/AmyOShea/MS4-ARTstop/blob/master/TESTING.md). 

## Bugs


---
---

---
---

# Credits
## Code

+ The initial site functionality was made using the [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) walkthrough by [Chris Zielinski](https://github.com/ckz8780) via Code Institute. The code was adapted for what I needed.

+ I used [Bootstrap Page](https://getbootstrap.com/docs/4.0/utilities/flex/) to better understand designing the pages.

---
---

# Technologies Used
## Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python3](https://www.python.org/)

## Frameworks and Libraries
+ [Django](https://www.djangoproject.com/)
+ [Pip3](https://pip.pypa.io/en/stable/)
+ [jQuery](https://jquery.com/)
+ [FontAwesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/)
+ [Bootstrap](https://getbootstrap.com/)

## All Others
+ [Heroku](https://www.heroku.com/) used to deploy live site.
+ [Stripe](https://stripe.com/en-ie) used for the payments system.
+ [AWS](https://aws.amazon.com/) used for file storage.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version control.
+ [ResizeImage.net](https://resizeimage.net/) used to cut and re-size site images. 
+ [Balsamiq](https://balsamiq.com/) used to create wireframes.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [Responsinator](https://www.responsinator.com/) used to check site was responsive on different screen sizes.
+ [Am I Responsive](http://ami.responsivedesign.is/) used to generate README intro image.
+ [favicon.io](https://favicon.io/) used to create a site favicon.

## Content

+ All photos and graphic design on the page is our own. 

+ All bios and text/blog posts have been written by me. 

## Acknowledgements

+ My mentor Antonio Rodriguez for for his help at the different stages of the project.


