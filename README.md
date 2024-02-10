#### This is a "Recipe Explorer", project generated from ChatGPT

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

#### Day XX
- create base frontend
  - create pages with auth/autho 
  - create dummy modal detail recipe
  - create dummy profile page
  - create login page
  - create dummy dashboard/home page, the search bar is here
  - create save page, this will display all recipe that saved/favorited by user


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