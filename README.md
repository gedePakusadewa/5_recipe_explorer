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

##### Day 10
- ~responsive dashboard~
  - update style menu
  - fix navbar on page mark

issue and solution
- 


##### Day 9
- ~login/sign page~
  - fix button style
  - make page responsive for desktop and phone
- ~fix style in general related to btn class~
- ~fix double favorite~
- ~add loading icon in pop up deatil recipe~
- ~fix when search keyword outside pasta~
- ~fix different modal content for detail pasta in favorite~
- ~add string do general resource~
- ~fix position card in dashboard to be like row~
- responsive dashboard
  - update style menu

issue and solution
- 

#### Day 8
- ~implement "click button favorite" in frontend~
  - update style favorite
  - when user click favorite, system automatically add recipre to favorite
  - when system succesfully add recipe to DB, a simple modal appear
   
#### Day 7
- ~check best way to implement detail recipe in frontend~
  - use modal
  - modal appear in home and favorite page
- ~add soma style to profile~
  - update position
  - add new title for profile
  - set color #e9ebe8
- check what things need update to implement favorite
  - when user click favorite then sistem write to DB if favorite already or not exist in DB. my planning to add remove favorite when clicked when the recipe already in favorite but this will be implemented later.
  - add modal that contain message "the recipe" got favorited.
  - update style of favorite page, when there are no any favorite then it show "there no favorite recipe yet"

issue and solution
- should make modal or new page when user click detail?
  - use modal because it only display data about ingredient and instruction. if maybe in the future I add some information in detail then it preferable to just make a new page

#### Day 6
- ~implement recipe detail in BACKEND~
  - create new API
  - using this https://api.spoonacular.com/recipes/1003464/information?apiKey= because this endpoint API contain ingredient and instruction in one response
- check best way to implement detail recipe in frontend

issue and solution
- how to make API that suited with simple ingredient response?
  - save API RECIPE as list then add it to DICT
- using recipe detail API, should backend process it to return simple JSON or just send it directly to frontend?
  - let backend process it first because in front that response will easily process than directly send API detail recipe to frontend and also only send data that needed by frontend
- should make modal or new page when user click detail?
  -  

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
- check how to implement recipe detail
  - backend : combine this API response:
    - https://api.spoonacular.com/recipes/654959/ingredientWidget.json
    - https://api.spoonacular.com/recipes/654959/analyzedInstructions
  - frontend : 

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