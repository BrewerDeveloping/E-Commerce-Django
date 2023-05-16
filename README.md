[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10537047&assignment_repo_type=AssignmentRepo)
# Assessment 3: HTML/CSS/JS and Django
- **E-commerce Business**

## Requirements

Build an e-commerce website with a shopping-cart feature. 
- Your website should be a Django application that renders HTML templates, using CSS/Bootstrap. *Otherwise you must write your CSS or use a different framework.*
- Using Django ORM/psycopg2/Postgres:
    - Create a model named `products` to store product data. It should have the following fields. Using what you have learned, use your best judgement how to define each of these fields:
        - `id` - a unique id.
        - `name` - name of the product.
        - `category` - the product category.
        - `cost` - the product cost.
    - Create a model named `shopping_cart` to store the shopping cart. It should have the following fields. Using what you have learned, use your best judgement how to define each of these fields:
        - `product_id` - the `id` of the product in the cart.
        - `quantity` - the number of items of the product in the cart.
    - If necessary or desired create whatever other fields on these models, or whatever other models you want.
    - **Through whatever means you prefer, insert some fake data into your database. You should have at least 3 different products, and at least two different categories. **
    
Here is an example product:
| id  | name   | category      | cost |
| --- | -------|-------------- |------|
| 1  | shampoo | personal care | 4.5 |
| 2  | pencil  | office supplies | 1.50 |

Here is an example shopping cart:
| product_id  | quantity   |
| ----------- | -----------|
| 1           | 3          |
| 2           | 10         | 


Your website must allow the user to search for and browse products, and add products to their shopping cart.

### Required Pages & Features

#### **Home page** (index.html)
- Suggested route: `/`
- Whatever basic home page content / intro content you want.
- Site navigation links to:
  - **Each** Category page
  - Shopping Cart page
  - Search page (if using a search bar, a page for searching is not necessary)

#### **Category pages**
Each product category (e.g. "Home", "Kitchen", "Office", etc...) has it's own page. Requirements for each individual category page are:

- Suggested route: `/category/<:id>`
- Site navigation link to homepage.
- Lists all products in that category. 
  - User is able to click on a product and be taken to the Individual Product Page for that product.
- *Stretch goals:* 
  - Pagination
  - "Featured Products" -- three featured products at the top of the Category Page, which display full product information, are clickable links, and have working "Add to Shopping Cart" buttons.

#### **Individual Product Page**
- Suggested route: `product/<:id>`
- Displays all product information for a specific product.
  - Name
  - Category
  - Price
  - An image representing the product. 
- The user is able to click an "Add to Shopping Cart" button to add this product to their shopping cart.
  - *Clicking this button multiple times increases the quantity of the product in the cart*

#### **Shopping Cart page**
Displays the shopping cart and details of items in it.

  - Suggested route: `/shopping-cart`
  - Site navigation link to homepage.
  - Display all of the products added to the user's shopping cart. For product item users should be able to see:
    - Quantity/number of item ordered. Example: 
        ```
        Mechanical Pencil: 3 
                      Pen: 1
        ```
    - The Subtotal for each item. For example, if cost of 1 mechanical pencil is $2 and 1 pen is $3: 
      ```
      Mechanical Pencil: 3 - $6
                    Pen: 1 - $3 
      ```
    - Total price for the entire order. Example:
      ```
      Mechanical Pencil: 3 - $6
                    Pen: 1 - $3 
            TOTAL PRICE:     $9
      ```
  - *Bonus/Stretch Goals*: 
    - Remove product from cart

#### **Search page**
A user is able to search for a specific product by name.
- Suggested route: `/search/<:search_string>`
- Site navigation link to homepage.
- If product exists, display product information. If product is not available, display an appropriate message. 

#### Additionally, your site should:
  - Use Bootstrap Navbar component or write equivalent CSS.
  - Use Bootstrap Grid or write equivalent CSS.
  - Use another Bootstrap component (dropdown, carousel, navbar, etc) or write equivalent CSS.
  - Include some basic styling using CSS
  - Avoid repeating HTML across your different pages by using `{% include partial.html %}` and `{% extends layout.html %}`. There should only be one `<html>` tag in your whole project!
  - If necessary, use python-dotenv and .gitignore to keep your API keys out of git.

## Important Grading Information
- Make sure you read the [Assessment-3 Grading Rubric](https://docs.google.com/spreadsheets/d/1-YjVU8Wt7qgW8yOImASqB2uYiLBu93dVJuLYjUlEIgk/edit?usp=sharing).
- Your assessment, regardless of completion status, must be submitted by the deadline. 

- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade.
  - *10% penalty*: If you complete and submit the retake after one week of receiving your grade.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of any other student/individual.

## TURNING IN YOUR PROJECT (VERY IMPORTANT!!) ##
- In order to receive a grade for this project, you MUST record yourself doing a demo of your code and project. 
- Your video file should be submitted (via slack) to Nick Smith. 
- You can use whatever method you see fit to record your own video. (Screen capture software, personal zoom recording, phone camera, etc.)  
- At a minimum, your video must include the following things displayed clearly and readable on screen:
    - Starting your django server, and naviagating a browswer window to the server page. 
    - Using your hyperlinks/navbar so we can verify functionality.
    - Show your shopping cart and demo everything in the "Website Functionality" section of the rubric.
    - Mention which two components you used from Bootstrap. 
    - OPTIONAL: If you are implementing an API call, show how you are keeping your API keys out of git. 
