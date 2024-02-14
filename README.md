#### This is a "Recipe Explorer", project idea was generated from ChatGPT

### Project Image Preview

### Project Description:

Create a Recipe Explorer application that allows users to explore, search, and save their favorite recipes. The application will use a third-party recipe API to fetch recipe data and display it to users. Users can create accounts, log in, and save their favorite recipes for easy access.

Key Features:

- User Authentication

  Allow users to create accounts and log in. Implement secure authentication mechanisms to protect user data.

- Recipe Search

  Integrate a recipe API (e.g., Spoonacular, Edamam) to fetch a wide variety of recipes. Implement a search functionality to allow users to find recipes based on ingredients, cuisine, or dietary preferences.

- Recipe Details

  Display detailed information about each recipe, including ingredients, instructions, and nutritional information. ~Allow users to rate and leave comments on recipes~ (NOT IMPLEMENTED).

- Save and Favorite

  Enable users to save their favorite recipes to their profile. Implement a "favorites" section where users can quickly access their saved recipes.

- User Profile

  Create user profiles where users can view and manage their saved recipes, personal information, and preferences. ~Display a history of recently viewed recipes~(NOT IMPLEMENTED).

- ~Responsive Design~ (NOT-IMPLEMENTED)

  Ensure the application is responsive and works well on both desktop and mobile devices.

- Backend API

  Develop a backend API to handle user authentication, recipe data storage, and user-specific data. Create endpoints for user registration, login, fetching recipes, saving favorites, etc.

- Data Persistence:

  Implement a database to store user information, saved recipes, and other relevant data. Use appropriate database technologies like MongoDB, PostgreSQL, or MySQL.

- ~Security~ (NOT-IMPLEMENTED)
  
  Implement security best practices to protect user data, including encryption for sensitive information.

- ~Notifications~ (NOT-IMPLEMENTED)

  Implement email notifications for account verification, password reset, and other relevant events.

---

#### Additional Enhancements (Optional):

- User Preferences
  
  Allow users to set dietary preferences and allergies to filter recipe recommendations.

- Social Sharing

  Implement social sharing features, allowing users to share their favorite recipes on social media.

- Recipe Collections

  Enable users to create and share custom recipe collections or meal plans.

- Shopping List

  Provide an option for users to generate a shopping list based on selected recipes.

---
### Project Journal

#### Day 5
- ~create working dashboard~
  - add search bar
  - display search result
    - only display image with title and button LOVE (not working) "favorite"
- ~make a working profile~
  - make API for profile
  - make frontend to handle profile
- ~make backend favorite~
  - make table for this case
  - make API for get and set favorite
- ~make frontend to handle favorite~
  - display favorite recipe user using card style
  - check what api from recipe to this favorite case
    - this case using same API URL add url detail in home
  - check how to implement favorite case using API recipe
    - to avoid multiple request to same API, i add two additional colom so its just need request only when user need detail about recipe

issue and solution:
- can not get value from usestate although there is value from that const?
  - simply i forget to implement that usestate
- can not serialize favorite without using data user_id in request
  - simply use "user":user_id instead of User:user
- error when get data from favorite
  - simple i use same name for class name and model name, when i change model name, its solved
- should i use multiple request recipe id data for each favorite or just save small data in system DB then display it to user?
  - to avoid multiple request to API RECIPE, i add title and image URL colom to model Favorite. So, when user open page favorite, system only request detail recipe to API RECIPE
- url field from image url for django model?
  - use URLField() in model

#### Day 4
- ~update dashboard style and update navbar~

issue and solution:
- 

#### Day 3
- ~create base frontend~
  - create pages with auth/autho 
  - create dummy modal detail recipe
  - create dummy profile page
  - create login page
  - create dummy dashboard/home page, the search bar is here
  - create save page, this will display all recipe that saved/favorited by user
- ~improve the appearance of the login/signUp page~
- ~add and fix issue when user incorrecty input username/password in login/sign up~

issue and solution:
- None

#### Day 2
- ~make dummy response API~
  - to make sure little unnesisary request when update code frontend
- ~learn doc API from spoonacular~
  - make sure how recipe data is from API
  - make sure what thing can be search through API

issue and solution:
- why using import X2, X3?
  - I use "from CC, import X2, X3" instead of "from CC import *" because I want to differentiate this variable from other imported variables

#### Day 1
- create base backend
  - ~create Token authe/autho~
  - create list of backend API
    - API get and set user profile
    - API search recipe
    - API save favorite and get favorite
  - ~test spoonacular API in backend~
  - ~create project and app django~
- learn doc API from spoonacular
- ~understand the project requirement~

issue and solution:
- 