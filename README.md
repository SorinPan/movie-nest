# **MovieNest**

## Introduction



[MovieNest Live Website](https://movie-nest-cc8eb513ed09.herokuapp.com/)

---

## User Experience(UX)

### Agile Development

#### Epic: Project Setup

* Task: Create a new Django project named "MovieNest."
* Task: Set up the project structure and initial settings.
* Task: Configure the database settings for the project and create the initial database schema.
* Task: Set up templates for HTML rendering and static files.
* Task: Design the user interface.
* Prepare deployment.

#### Epic: User Registration and Authentication

* User Story: As a user, I want to be able to register for a MovieNest account.
  * Subtask: Create a registration view and template.
  * Subtask: Implement user registration form.
* User Story: As a registered user, I want to be able to log in to my MovieNest account.
  * Create a login view and template.
  * Implement user login form.

#### Epic: User Account Profile

* User Story: As a registered user, I want to have a profile page where I can view and edit my user information.
  * Subtask: Create a user profile view and template.
  * Subtask: Implement the ability to view and edit user information.
  * Subtask: Add an option to upload and update a profile picture.
* User Story: As a registered user, I want to be able to mark movies as my favorites.
  * Subtask: Add a "Favorite" button to movie details pages.
  * Subtask: Implement the ability to add and remove movies from the user's favorites list.
  * Subtask: Display the list of favorite movies on the user profile page.
* User Story: As a user, I want to be able to delete my MovieNest account.
  * Subtask: Add a "Delete Account" option on the profile page.
  * Subtask: Implement the functionality to delete the user account and associated data.

#### Epic: Movie Details Page

* User Story: As a user, I want to search for movies by various criteria.
  * Subtask: Create a search view and template.
  * Subtask: Implement search functionality.
* User Story: As a user, I want to view detailed information about a movie.
  * Subtask: Create a view and template for displaying movie details.

#### Epic: User Reviews and Ratings

* User Story: As a registered user, I want to write a review for a movie.
  * Subtask: Create an "Add Review" view and template.
  * Subtask: Implement a form for adding reviews.
  * Subtask: Associate reviews with movies and users.
* User Story: As a registered user, I want to be able to rate a movie.
  * Subtask: Implement the rating system.
  * Subtask: Update the movie details template to display the average rating.
* User Story: As a user, I want to read reviews for a movie.
  * Subtask: Create a view and template for displaying reviews on a movie's details page.