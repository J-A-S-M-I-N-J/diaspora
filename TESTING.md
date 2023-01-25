# Full Testing
---
---
## Validator Testing
### **HTML**

I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)

Mostly fixed stray-end tags and some unclosed <span> elements. 

The validator does react to every single template-tag though. Not sure if this is a real 'error'. See below.

[Image]

Errors found & fixed: 

### **CSS**

I had two CSS files that were checked using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

### **JavaScript**

I checked the all the JavaScript files using [JSHint](https://jshint.com/)

There were a few missing semicolons and ES6 version issues but they were easy fixes. 

One error that I found that I was in the checkout javascript file:

![JS valiadation error](docs/bugs-and-fixes/js-validation-error.PNG)

Because the code comes from Stripe itself, I don't want to touch this and am happy to leave it alone. 

### **Python**
I checked the Py files using [PEP8 online](http://pep8online.com/)

The code passed all checks.

---
---

## Lighthouse Testing

After getting the bulk of the site in place, I ran it through Chrome Lighthouse. While all of the elements were in green, I wanted to improve them:


### **Performance**

I made no changes to the performance score. 

### **Accessibility**

I changed the footer ``<h5>`` elements to ``<p>`` elements which improved the score.

### **Best Practices**

I added ``rel="noopener"`` to the footer Facebook link

### **SEO**

I added a meta decription to the base template. 

### Final Lighthouse Score:

![Lighthouse score](docs/lighthouse-desktop.PNG)

---
---

## Known Bugs

---

### Bag Quantity

Editing quantities in bag doesen't work. The "buttons" don't do anything, however you can still change the amount with the 'arrows'. 

---

### Blog

At seemingly random times the blog would give an internal server error, usually on creating the fourth or sixth post, however, sometimes I remove those posts and make new ones, and it seems to work. I first thought that is was an error with images, and then with blog titles being to similar, but since the defensive code in place to not be able to post the same title twice it shouldn't be the reason. Whenever I try to recreate the error to figure it out, it's not replicable, however it has shown up 4-5 times during the creation of this project. 

---

### Images on Music page

One image seems to randomly rescale on XL media queries, which is strange because the images are the same size and dimensions and the artists are created from the same model. 

---

## Fixed Bugs

---
---

### Email @ Booking

Email from booking page didn't initially work, this was due to there being two email-backends, this was solved by deleteing one of them. 

---

### Links in NAV

For the longest time the links in NAV didn't work, this was due to a 'data-toggle' class, started working when this was removed. 

---

### Database Crash

I had a huge database meltdown when I tried to remove something in Admin that existed in a fixture, since I didn't want to have the same items from the Walkthrough-content I decided to clean my __init__ files and reupload my database without any product-fixtures and create them myself. 

---

### Secret_Key/Staticfiles Crash

At one point I tried to deploy the page to Heroku and with that change the ALLOWED_HOSTs and the roots to staticfiles, this made the page upload completely blank and without any staticfiles. After talking to the tutors, we just backtraced it and restored it to normal, this is also when the tutor told me that my secret keys were exposed and I created and env.py file. 

--- 

### **Stripe Test Webhook Issues**

**not a bug but something that I had to query regardless**

When initally setting up Stripe payments, I was not having any issues with either ```payment_intent.succeeded``` or ```payment_intent.payment_failed``` test webhooks. However, once the full payment system was in place and fully functional, I was having issues with ```payment_intent.succeeded``` test webhook. I would recieve a 500 error both in Stripe and the local terminal:

![Stripe test webhook issue](docs/bugs-and-fixes/bug-08-01.PNG)

![Stripe test webhook issue](docs/bugs-and-fixes/bug-08-02.PNG)

The 500 error was pointing to the ```bag``` in the webhook_handler.py file. However, the ```bag``` variable was created in the views.py file. I didn't know how to solve this so I contected tutor support and the Full Stack Frameworks slack channel. <br>
The general consensus was that this would be an expected behviour when sending a test ```payment_intent.succeeded``` webhook.<br>
When sending a ```payment_intent.succeeded``` test webhook, Stripe sends default data, but the data held in the ```cache_checkout_data(request)``` would be different, causing the conflict.

![Stripe test webhook issue](docs/bugs-and-fixes/bug-08-03.PNG)

To test this theory, I commented out the ```cache_checkout_data(request)``` function and the test webhook worked.