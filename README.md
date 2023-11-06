# **MovieNest**

## Introduction

MovieNest is a website made for movie made for movie enthusiasts. It is a full stack project built with Django framwork for the backend. HTML, CSS and JavaScript are used for the projects front-end part. Bootstrap is also used for design and responsive development. MovieNest allows users to easily see top rated and trending movies. Users are also able to create accounts and submit reviews of movies already watched, as well as reading and commenting reviews made by others.The website also features the posibility to add interesting movies to "favorites".

[MovieNest Live Website](https://movie-nest-cc8eb513ed09.herokuapp.com/)

---

## Agile Development

The project was developed using an agile workflow and agile principles. Jira was the tool used to keep all of it together. Epics, user stories and developer stories were created and then added to the backlog. The backlog is were the stories are reviewed, refined and then committed for development. 

### Workflow

<details><summary>Backlog</summary>
<img src="docs/screenshots/backlog.png">
</details>

Jira's backlog feature was used in combination with the Kanban template. The stories start in the backlog after they are created. Here they are assigned to Epics and prioritized using the MoSCoW method. Subtasks and Acceptance criteria are added to the user stories in an effort to better outline the requirements for each story to be completed. Story points are also assigned to estimate the overall effort required to complete a user story.

<details><summary>Board</summary>
<img src="docs/screenshots/agile-board.png">
</details>

After a user story is refined, it is sent to the Board.

- Committed for Dev: This status is used for refined stories that are ready to be worked on.
- In Progress: The user stories that are currently in progress.
- In Review: This status is used to review the code one more time before testing.
- In Testing: This status is used for manual testing.
- Deployed: Deployed to Heroku to see that everything works in production ( Note that I didn't deployed after each story was completed).
- Done: Completed user stories.

<details><summary>Workflow Scheme</summary>
<img src="docs/screenshots/agile-workflow.png">
</details>

---

## User Experience(UX)

### Strategy Plane

#### Project Goals

- To develop a user-friendly and responsive website that makes it easy to get information about different movies.
- To provide users with the ability to easily see what movies are trending/top rated.
- To provide users with the ability to easily search for movies by keywords or titles.
- To provide users with the ability to create a profile and add movies to "Favorites".
- To allow registered users to review movies and comment on other reviews and watchlists.
- To provide registered users the ability to edit or delete their profiles, reviews and comments.

#### Target Audience

- **Movie Enthusiasts:** Someone who has a strong passion for movies and is always on the lookout for the latest releases or classic films.
- **Casual Movie Viewers:** Someone who enjoys watching movies, but is not so involved in the film community.
- **Film Critics and Reviewers:** Professional critics who want to share their insight with others.
- **Users Looking for Movie Recommendations:** Movie watchers that want a good recommendation for a Sunday evening movie session.

### User Stories

#### **Epic: Project Setup**

* **Task: As a developer, I want to create a new Django project.**
* **Task: As a developer, I want to establish the project structure and initial settings.**
* **As a developer, I want to configure the database settings for the project and create the initial database schema.**
* **Task: As a developer, I want to deploy the website on Heroku.**

#### **Epic: Templates/ Home Page**

* **Task: As a developer, I want to create a responsive and user-friendly home page design.**
* **User Story: As user, I want to immediately understand its purpose and navigation options.**
* **User Story: As a user, I want to be able to get in touch with the site owner.**

#### **Epic: User Registration and Authentication**

* **User Story: As an admin, I want access to an admin panel where I can manage the website's content.**
* **User Story: As a user, I want to be able to register for an account.**
* **User Story: As a registered user, I want to be able to log in and out from my account.**

#### **Epic: User Account/Profile**

* **User Story: As a registered user, I want to have a profile page where I can view and edit my user information.**
* **User Story: As a registered user, I want to be able to view movies that I liked (favourites).**
* **User Story: As an admin, I want to be able to manage user accounts, including disabling or banning accounts when necessary.**

#### **Epic: Search for Movies**

* **Task: As a developer, I want to integrate a movie database API so that I can retrieve movies for my project.**
* **User Story: As a user, I want to be able to search for movies using keywords or titles.**
* **User Story: As a user, I want to see the search results presented in a user-friendly and responsive format.**

#### **Epic: Movie Details Page**

* **Task: As a developer, I need to design and create a template for displaying movie details.**
* **User Story: As a user, I want to view detailed information about a movie when I click on a movie title.**
* **User Story: As a user, I want to read user-generated reviews for the movie to get an idea of its quality.**
* **User Story: As a user, I want to see the average rating for a movie.**

#### **Epic: User Reviews/Comments and likes**

* **User Story: As a registered user, I want to be able to submit a review for a movie.**
* **User Story: As a registered user, I want to comment on reviews written by others.**
* **User Story: As a user, I want to edit and delete my own reviews and comments.**
* **User Story: As a registered user, I want to be able to like movies, adding them to my list of favourites.**
* **User Story: As an admin, I want to be able to delete inappropriate reviews and comments.**

#### **Epic: Watchlists**

* **User Story: As an admin, I want to create, edit, and delete watchlists.**
* **User Story: As a registered user, I want to view and comment on different watchlists.**

### Scope Plane

#### Features Planning

|User Type | Feature | Importance | Viability |  | Delivered |
| :--- | :--- | :---: | :---: | :---: | :---: |
| | User roles (Admin, Registered User, Guest) | 5 | 5 | MVP |  |
| Guest | Register for an account | 4 | 5 | MVP |  |
| All | Search for movies by keywords or titles | 4 | 5 | MVP |  |
| All | View top-rated movies | 4 | 4 | MVP |  |
| All | View trending movies | 4 | 4 | MVP | |
| Registered User | View movie details | 4 | 5 | MVP |  |
| Registered User & Admin | Sign in/Sign out | 4 | 5 | MVP |  |
| Registered User | User profile | 4 | 5 | MVP |  |
| Registered User | Edit profile | 3 | 4 | MVP |  |
| Registered User & Admin | Delete account | 3 | 4 | MVP |  |
| Registered User | Leave reviews for movies | 4 | 5 | MVP |  |
| Registered User | Comment on movie reviews | 3 | 4 | MVP |  |
| Registered User | Like movies(add to favorites) | 3 | 4 | MVP |  |
| Registered User | View like movies(favorites) | 3 | 4 | MVP |  |
| Registered User | Edit and delete own reviews | 4 | 4 | MVP |  |
| Registered User | Edit and delete own comments | 3 | 3 | MVP | |
| Admin | Admin panel for website management | 4 | 4 | MVP |  |
| Admin | Create and manage watchlists | 4 | 4 | MVP |  |
| Admin | Delete reviews/comments | 3 | 5 | MVP |  |
| Registered User | View new movie releases | 2 | 3 | |  |
| Registered User | Advanced search filters (e.g., genre, release year) | 1 | 3 | |  |

### Structure Plane

#### Initial Database Scheme

**Relationships:**

* The User Profile has One-to-Many relationship with the Review and Comments models. One user can write multiple reviews and comments.
* The User Profile has also Many-to-Many relationship with the Watchlist model. Admins can create multiple watchlists.

* The Movie model has One-to-Many relationship with the Review model. One movie can have multiple reviews.
* The Movie model has Many-to-Many relationship with the Watchlist model. Movies can be in multiple watchlists.

* The Review model has One-to-Many relationship with the Comments model. One review can have multiple comments.

![Initial Database Scheme](/docs/screenshots/initial_schema.png)

### Skeleton Plane

#### Wireframes

The wireframes were created with [Balsamiq](https://balsamiq.com/). My initial idea for the websites structure. Not all features were structured with wireframes.

- Desktop

    Home Page

    ![Home Page Wireframe Desktop](docs/wireframes/home-desktop.png)

    Trending/Top Rated

    ![Trending/Top Rated Wireframe Desktop](docs/wireframes/trending-desktop.png)

    Movie Details

    ![Movie Details Wireframe Desktop](docs/wireframes/movie-detail-desktop.png)

    Review Details

    ![Review Details Wireframe Desktop](docs/wireframes/review-detail-desktop.png)

    Watchlists

    ![Watchlists Wireframe Desktop](docs/wireframes/watchlists-dekstop.png)

    Sign In

    ![Sign In Wireframe Desktop](docs/wireframes/signin-desktop.png)

    Sign Up

    ![Sign Up Wireframe Desktop](docs/wireframes/signup-desktop.png)

- <details><summary>Mobile</summary>

    Home Page

    ![Home Page Wireframe Mobile](docs/wireframes/home-mobile.png)

    Trending/Top Rated

    ![Trending/Top Rated Wireframe Mobile](docs/wireframes/trending-mobile.png)

    Movie Details

    ![Movie Details Wireframe Mobile](docs/wireframes/movie-detail-mobile.png)

    Review Details

    ![Review Details Wireframe Mobile](docs/wireframes/review-detail-mobile.png)

    Watchlists

    ![Watchlists Wireframe Mobile](docs/wireframes/watchlists-mobile.png)

    Sign In

    ![Sign In Wireframe Mobile](docs/wireframes/signin-mobile.png)

    Sign Up

    ![Sign Up Wireframe Mobile](docs/wireframes/signup-mobile.png)

    </details>
    
### Surface Plane

#### Color Scheme

![Color Scheme](docs/screenshots/color-scheme.png)

I thought a darker theme would fit the website perfectly and it would give a nice minimal look. I also choose Red since it attracts the most attention and is associated with strong emotions. All the main text on the website is white, which adds some nice contrast.

#### Typography

![Typography](docs/screenshots/typography.png)

- **Cinzel -** Used for headings mainly. It's an elegant and decorative font and I think it gives a sense of sophistication and style to the website.
- **Lato -** Used for the main text on the website. It's a popular font with a clean and modern look. I felt like it's a safe choice and very suitable for displaying content in a clear manner.
- **Quicksand -** Only used for the websites logo. Since it's a playful and friendly font, I felt like it suits the website overall.

#### Imagery

---

## Features

---

## Technologies Used

### Languages

HTML, CSS, JavaScript, Python.

### Frameworks

- [Django](https://www.djangoproject.com/) - Version 4.2.6 - A Python web framework that is used for rapid development.
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Version 5.3.2 - A framework for building responsive.

### Libraries

- [dj_databsae_url](https://pypi.org/project/dj-database-url/) - Version 2.1.0. Allows to utilise the DATABASE_URL variable.
- [gunicorn](https://pypi.org/project/gunicorn/) - Version 21.2.0. A Python WSGI HTTP Server.
- [psycopg2](https://pypi.org/project/psycopg2/) - Version 2.9.9. Allows connection with postgres database
- [Font Awesome](https://fontawesome.com/) - Version 6.4.2 - Used to integrate icons in the website.
### Other Tools

- [Git](https://git-scm.com/) - For version control.
- [GitHub](https://github.com/) - To save and store the files for this project.
- [ElephantSQL](https://www.elephantsql.com/) - For database.
- [Heroku](https://www.heroku.com/) - For deployment.
- [Gitpod](https://www.gitpod.io/) - For development.
- [Obsidian](https://obsidian.md/) - For notes.
- [Balsamiq](https://balsamiq.com/) - For wireframes.

---

## Credits

- [Django Docs](https://docs.djangoproject.com/en/4.2/)

- [Django 3.0 Tutorial IMDB clone](https://www.youtube.com/watch?v=FawGmAas4h0&list=PL9tgJISrBWc6ktmvTSLGrn055XzVb0OwZ&index=1)

- [Django Recipe Sharing Tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)

- [Slack](https://slack.com/intl/en-ie/)

- [TMDB docs](https://developer.themoviedb.org/docs)

- CI Project Checklist

