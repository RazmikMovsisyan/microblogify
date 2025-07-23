# **Microblogify**

[Live Project on Heroku](https://microblogify-f169ead0df1f.herokuapp.com/)

![Responsive Mockup](/assets/images/am-i-responsive.jpg)

Welcome to **Microblogify** – a community microblogging platform!

Microblogify is a modern, responsive full-stack web application designed to empower users to express themselves through short, concise blog posts—similar to a microblogging platform. Built with Django and a relational database, Microblogify enables users to share thoughts, and interact with content in a dynamic, community-driven environment.

The platform offers essential features such as user registration, authentication, and role-based access, allowing different levels of interaction based on user status. Authenticated users can create, read, update, and delete posts, while also exploring content from the wider user base. Comments help foster engagement, turning the app into a vibrant space for digital expression.

The design prioritizes accessibility, user experience, and mobile responsiveness, ensuring the site is intuitive and enjoyable to use on all devices. Microblogify was developed using Agile methodologies, with clearly defined user stories guiding its functionality and interface.

Whether you want to share daily updates, thoughts, or start discussions, Microblogify provides a lightweight, social experience tailored for microcontent creators.

The goal is to promote authentic user interactions and community discussions through a well-structured and secure full-stack platform.

---

## **Table of Contents**
- [Microblogify](#microblogify)
  - [Planning](#planning)
    - [Features](#features)
    - [Used Technologies](#used-technologies)
    - [App Owner Goals](#app-owner-goals)
    - [User Stories (prioritized using MoSCoW method)](#user-stories-prioritized-using-moscow-method)
  - [Wireframes](#wireframes)
  - [Database Design](#database-design)
  - [Validation](#validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
  - [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
  - [Deployment](#deployment)
      - [Heroku](#heroku)
  - [Version Control](#version-control)
  - [Development Process and Git Commands](#development-process-and-git-commands)
  - [Clone and Fork](#clone-and-fork)
  - [Custom 404 Page](#custom-404-page)
  - [Credits](#credits)
  - [Finished Product](#finished-product)


---

## **Planning**

### **Features**
- User authentication and role-based access.
- Post creation with Markdown support.
- Commenting functionality.
- Admin dashboard for managing users and posts.
- Responsive design and accessibility-compliant interface.

### **Used Technologies**
- Python, Django, PostgreSQL
- HTML5, CSS3, JavaScript
- Django AllAuth (authentication)
- Cloudinary (image hosting)
- Heroku (deployment)
- Git & GitHub (version control)
- Draw.io / Figma (wireframes and design)
- Markdown (documentation)

---

### **App Owner Goals**
- Provide a safe and friendly microblogging platform.
- Enable easy post interaction through comments.
- Allow administrators to moderate content.
- Provide clear UX/UI feedback to users at every step.

---

### **User Stories (prioritized using MoSCoW method)**

#### **Must Have**

**User Registration**
- *As a new visitor,* I can register for an account so that I can create and manage posts.

**Acceptance Criteria:**
- AC1: When I provide valid registration details, I am successfully registered.
- AC2: I am automatically logged in after registration.

---

**User Login/Logout**
- *As a registered user,* I can log in and log out so that I can access my personal dashboard securely.

**Acceptance Criteria:**
- AC1: Given correct credentials, I can log in.
- AC2: I can log out with one click.

---

**Create Post**
- *As a logged-in user,* I can create a new post so that I can share updates publicly.

**Acceptance Criteria:**
- AC1: I can submit a valid form to create a post.
- AC2: After submission, the new post appears in the feed.

---

**View Posts**
- *As a user,* I can view a list of recent posts so that I can read what others have shared.

**Acceptance Criteria:**
- AC1: The homepage displays the latest posts from all users.
- AC2: Each post includes author, content, and date.

---

**Edit and Delete a Post**
- *As a user,* I can edit or delete my own posts so that I can update or remove content I’ve shared.

**Acceptance Criteria:**
- AC1: Only the author of the post sees “Edit” and “Delete” buttons.
- AC2: Clicking “Edit” opens a form pre-filled with the post content.
- AC3: After saving, the post updates on the detail page.
- AC4: Clicking “Delete” shows a confirmation prompt.
- AC5: After confirming deletion, the post is removed and the user is redirected.

---

**Comment on Post**
- *As a logged-in user,* I can comment on posts so that I can join conversations.

**Acceptance Criteria:**
- AC1: Comments appear below each post.
- AC2: Only logged-in users can comment.

---

#### **Should Have**

**User Profile Page**
- *As a user,* I can view another user's profile so that I can see all their posts.

**Acceptance Criteria:**
- AC1: The profile displays username and profile image.
- AC2: Only that user's posts are listed under the profile.

---

**User Delete Profile**
- *As a logged-in user,* I can delete my profile and all my posts so that I can permanently leave the platform.

**Acceptance Criteria:**
- AC1: A delete button is visible on my profile.
- AC2: A confirmation prompt appears before deletion.
- AC3: Upon confirmation, the profile and all posts are deleted.
- AC4: I am logged out and redirected with a success message.

---

#### **Could Have**

**Follow Users**
- *As a logged-in user,* I can follow and unfollow other users so that I can build my personal feed.

**Acceptance Criteria:**
- AC1: “Follow” button is visible on other user profiles.
- AC2: Followed users' posts appear on a personalized feed.

---

#### **Won’t Have (for now)**

- Private messaging between users  
- Tagging posts with hashtags  
- Real-time notifications


| **Original Story Title**       | **Included** |
|-------------------------------|---------------|
| **Edit and Delete a Post**    | ✅             |
| **Comment on Post**           | ✅             |
| **User Profile Page**         | ✅             |
| **User Delete Profile**       | ✅             |
| **User Registration**         | ✅             |
| **User Login/Logout**         | ✅             |
| **Delete Post**               | ✅             |
| **Edit Post**                 | ✅             |
| **View Posts**                | ✅             |
| **Create Post**               | ✅             |

![Responsive Mockup](/assets/images/user-stories-project-moscow.png)

---

## Database Design

This ERD shows the core models of the Django project and how they are connected.
I kept it simple and easy to understand, so anyone can quickly see how the data is structured.

The design was created during the planning phase and strictly followed during implementation.
You can find the implementation in [blog/models.py](blog/models.py), which maps exactly to the structure shown here.



![Entity Relationship Diagrams](assets/images/entity-relationship-diagrams.png)
[Live Preview in Mermaid Editor](https://mermaid.live/edit#pako:eNqVU8FuwjAM_ZXK54JSRkrJlV0nIU27TEgoa0yJ1CQoTTcY8O9zgQKiaGw5xXnPfn5xsoXcKQQB6J-1LLw0MxvReqvQR7tdr7fbRVPvFrrESERLWd3AbhtNXRUIyz3KgHfwiTMGbUP58vrMOGR1GB5z1J8N56rO9rhvliaWVpe4Cl7bIqqJZqXBDoBG6vJ4um9rtnZ-KdvETc35HS1tZHElFHAdog_tbkUaew8UZB2W7q5G0KHsmqnKurgRzp0NdHOXU0UzCNrgaRxq7uwdsF6pDti1dzbTzueBnxV5nv_B5D87pzYghsJrBSL4GmMw6GmuFMKhoxmEJdLwQdBW4ULWZZjBzO4pbSXtu3OmzfSuLpYgFrKsKDpew-ndtxRq2L1ubN7GVAHEFtYgkhHvZ0M25ix5YjxL-SCGDYiM9dNhyjM-SniajLLxPobvgybrj_h4kDBGGSxlwyylDtAq9BNX2wBiwGNApYPzL8dfePiM-x8zbxbG)


## **Wireframes**

I used [Balsamiq](https://balsamiq.com/wireframes) to create the wireframes for this project. I chose Balsamiq because it has a sketchy, hand-drawn look that makes it clear these are wireframes, not real screenshots. This helps avoid confusion and shows that the designs are just drafts.

I tried to make the wireframes as realistic and useful as possible, while still keeping the rough, planning-style look that wireframes are meant to have.

Balsamiq was helpful because:

- It let me focus on layout and structure instead of details
- It made it easy to share ideas and get feedback
- It was quick to use and good for early design work

The wireframes can also be viewed as a [PDF exported from Balsamiq.](assets/wireframes/balsamiq-wireframes.pdf)

| Page         | Desktop View                                 | Mobile View                                       |
|--------------|-----------------------------------------------|---------------------------------------------------|
| Sign Up      | ![](assets/wireframes/sign-up.png)           | ![](assets/wireframes/phone-sign-up.png)          |
| Login        | ![](assets/wireframes/login.png)             | ![](assets/wireframes/phone-login.png)            |
| Homepage     | ![](assets/wireframes/home.png)              | ![](assets/wireframes/phone-homepage.png)         |
| Add Post     | ![](assets/wireframes/add-post.png)          | ![](assets/wireframes/phone-new-post.png)         |
| Post Detail  | ![](assets/wireframes/post-page.png)         | ![](assets/wireframes/phone-post-title.png)       |
| Profile Page | ![](assets/wireframes/profile-page.png)      | ![](assets/wireframes/phone-profile-page.png)     |
| Error 404    | ![](assets/wireframes/error-404.png)         | ![](assets/wireframes/phone-error-404.png)        |


## **Validation**

### **HTML**

I have used HTML W3C Validator to validate my HTML files.

| File         | URL                                                                                                                                     | Screenshot                                      |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [login.html](blog/templates/account/login.html)       | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2Faccounts%2Flogin%2F)                     | ![](assets/validation/login.html.png)           |
| [signup.html](blog/templates/account/signup.html)     | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2Faccounts%2Fsignup%2F)                    | ![](assets/validation/signup.html.png)          |
| [base.html](blog/templates/blog/base.html)            | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2F)                                        | ![](assets/validation/base.html.png)            |
| [post_detail.html](blog/templates/blog/post_detail.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2Fbuilding-a-family%2F)                 | ![](assets/validation/post-detail.html.png)     |
| [post_form.html](blog/templates/blog/post_form.html)  | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2Fnew%2F)                                  | ![](assets/validation/post-form.html.png)       |
| [post_list.html](blog/templates/blog/post_list.html)  | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com)                                           | ![](assets/validation/base.html.png)            |
| [profile.html](blog/templates/blog/profile.html)      | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2Fprofile%2F)                              | ![](assets/validation/profile.html.png)         |
| [404.html](blog/templates/404.html)                   | *(Cannot provide w3 Validator link. Test via direct input due to 404 error)*                                                             | ![](assets/validation/404.html.png)             |

### **CSS**

I have used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator)  to validate my main CSS file.

| File         | URL                                                                                                                                     | Screenshot                                      |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [style.css](staticfiles/css/style.css)       | [Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmicroblogify-f169ead0df1f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)                     | ![](assets/validation/blog:static:css:style.css.png)           |


### **JavaScript**

I have used [JShint Validator](https://jshint.com) Validator to validate my JS file.


| File         | URL                                                                                                                                     | Screenshot                                      |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [javascript.js](staticfiles/js/javascript.js)       | N/A                     | ![](assets/validation/javascript.js.png)           |

### **Python**

I have used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate my Python files.


| File                      | Linter                                                                                                                                                                             | Screenshot                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [admin.py](blog/admin.py)               | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/admin.py)               | ![](assets/validation/admin.py.png)               |
| [apps.py](blog/apps.py)                 | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/apps.py)                | ![](assets/validation/apps.py.png)                |
| [forms.py](blog/forms.py)               | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/forms.py)               | ![](assets/validation/forms.py.png)               |
| [models.py](blog/models.py)             | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/models.py)              | ![](assets/validation/models.py.png)              |
| [signal.py](blog/signal.py)             | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/signal.py)              | ![](assets/validation/signal.py.png)              |
| [urls.py](blog/urls.py)                 | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/urls.py)                | ![](assets/validation/urls.py.png)                |
| [views.py](blog/views.py)               | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/blog/views.py)               | ![](assets/validation/views.py.png)               |
| [settings.py](microblogify/settings.py) | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/microblogify/settings.py)   | ![](assets/validation/microblogify:settings.py.png) |
| [urls.py](microblogify/urls.py)         | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/microblogify/urls.py)       | ![](assets/validation/microblogify:urls.py.png)     |
| [manage.py](manage.py)       | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RazmikMovsisyan/microblogify/refs/heads/main/manage.py)       | ![](assets/validation/manage.py.png)               |

## **Testing**

### **Unit Testing**

`test_forms.py` & `test_models.py` demonstrate the functionality of some parts of my custom tests.

---
I performed two individual unit tests to verify the correctness of forms and models:

Each file was executed independently using Django’s test runner, and screenshots were taken as proof of successful test execution.
Both directories (`blog/` and `tests_blog/`) include `__init__.py` to ensure they are treated as Python modules.
Each test file was run separately using the following commands:

```
# Run test_forms.py
python3 manage.py test blog.tests_blog.test_forms
```

- `blog/tests_blog/test_forms.py`

![unittest1](assets/documentation/unittest1.png)

```
# Run test_models.py
python3 manage.py test blog.tests_blog.test_models
```

- `blog/tests_blog/test_models.py`

![unittest2](assets/documentation/unittest2.png)

---

### **Automated Testing**

#### Python (Unit Testing)

I created a dedicated test suite using Django’s built-in `unittest` framework to verify the functionality and robustness of my project.

## Test coverage

I wrote unit tests to cover the following:

- **Forms**: validation of comment input and user registration logic.
- **Views**: logic and response of list/detail views, post creation/edit/delete.
- **Models**: string representations and database interactions.
- **URLs**: URL resolution and reverse name matching.

In total, I created **6 functional test files**, which together yielded **75 % total code coverage**, including **100 % coverage for all test files themselves**.

In order to run the tests, I ran the following command in the terminal:

python3 manage.py test
To create the coverage report, I would then run the following commands:

```
pip3 install coverage
pip3 freeze --local > requirements.txt

coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py manage.py test
coverage report
```

To see the HTML version of the report, and find out whether some pieces of code were missing, I ran the following commands:

```
coverage html
python3 -m http.server
```
Below are the results from the full coverage report on my application that I've tested:

![coverage report](assets/validation/coverage-report.png)
### Why not 100 %?

Some parts of `views.py` involve conditional logic for authenticated users, HTTP POST actions, and error cases that are tedious or impractical to test in a limited timeframe. Similarly, `models.py` and `forms.py` include fallbacks or helper logic (like slugs, user fields) that are typically covered via integration testing.

**In a real-world project**, I would:
- add more integration and edge-case tests,
- include `setUpTestData` for efficiency,
- and use mocks for testing third-party behaviors.

### **Manual Testing**

| **Test Case**                  | **Action**                                           | **Expected Result**                                     | **Result** |
|-------------------------------|------------------------------------------------------|---------------------------------------------------------|------------|
| Register new user             | Fill and submit the signup form                      | User is registered and redirected                       | ✅          |
| Login/Logout                  | Provide credentials, log in and out                  | Login state changes are reflected                       | ✅          |
| Create post                   | Fill post form and submit                            | Post is created and displayed                           | ✅          |
| Edit/Delete own post          | Use edit/delete options on own post                  | Post is updated/removed from UI and database            | ✅          |
| Add comment                   | Submit comment on a post                             | Comment is displayed under the post                     | ✅          |
| Admin deletes comment         | Admin deletes comment from dashboard                 | Comment is removed                                      | ✅          |
| Access control                | Unauthenticated user tries to create a post          | Redirected to login page                                | ✅          |

---


### **Bugs**
- Initial login redirect not working → Fixed by setting `LOGIN_REDIRECT_URL`.
- Markdown rendering on post detail was buggy → Updated template filter and added sanitization.

---

## **Deployment**

### **Heroku**

Deployed via **Heroku**.
Live link: [Microblogify](https://microblogify-f169ead0df1f.herokuapp.com/)

Steps:
1. Created Heroku app and linked GitHub repo.
2. Added PostgreSQL and Cloudinary add-ons.
3. Config Vars added: `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, etc.
4. Added `Procfile`, `requirements.txt`, `runtime.txt`.
5. Disabled Django debug, ensured `.env` file excluded via `.gitignore`.


---


> [!EXAMPLE]
> You would replace the values with your own if cloning/forking my repository.

### Setting Config Vars on Heroku

- Click on the **Settings** tab of your Heroku app.
- Scroll down to the **Config Vars** section and click **Reveal Config Vars**.
- Add the required environment variables by entering the appropriate **Key** and **Value**.

![settings_config_vars](assets/documentation/heroku_settings_var.png)
| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `SECRET_KEY` | any-random-secret-key |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |

I have used [Randomkeygen](https://randomkeygen.com/) to generate my individual `SECRET_KEY`

Heroku needs some additional files in order to deploy properly.
- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

Or:

Deploy manually:
To deploy your app manually via the Heroku Dashboard:

- Go to your app on the Heroku website.
![Deploy0](assets/documentation/deploy0.png)

- In the top menu, click on **“Deploy.”**
![Deploy1](assets/documentation/deploy1.png)
- Scroll down to the Manual Deploy section and click on **Deploy Branch**
![Deploy2](assets/documentation/deploy2.png)

- After a successful deployment, click the **“View”** button to open your live app.
![Deploy3](assets/documentation/deploy3.png)

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
After logging in, go to your Dashboard.
- Click on **Go to API Keys**
![dashboard](assets/documentation/cloudinary_dashboard.png)

- Click on **Generate New API Key**

- You will see:
**Key name, API key, API secret**

![generate_api](assets/documentation/cloudinary_generate_api.png)

- These are your Cloudinary credentials used to connect your app.
- Copy the Cloud name, API key, and API secret.
- Store them in your environment variables (e.g., in a .env file):
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!INFO]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.


## **Version Control**
- Git used throughout, hosted on [GitHub Repo](https://github.com/RazmikMovsisyan/microblogify).
- Clear commit history per feature/bugfix.
- No sensitive info committed.

---

## **Development Process and Git Commands**

- I started the project by using the MS Visual Studio on my local machine.
- I regularly staged changes using the command `git add <filename>` or `git add .`, then committed using `git commit -m 'short descriptive message here'`.
- Finally, I pushed the changes to GitHub with `git push`.
- Every push automatically deploys the latest changes to Heroku from the 'main' branch.

## Clone and Fork

You can easily clone or fork the **Microblogify** repository for further development.

1. Visit the repository on GitHub: [Microblogify Repository](https://github.com/RazmikMovsisyan/microblogify).
2. Click the **Fork** button to create your own copy.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary
os.environ.setdefault("HOST", "user-inserts-own-host")
os.environ.setdefault("CSRF_TRUSTED_ORIGIN", "https://localhost")

# local environment only (do not include these in production/deployment!)
# (in settings I made sure that DEBUG = False in heroku if you do not add DEBUG to your config vars there)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.


#### **Clone the Repository using VS Code**

The repository has a single branch with a clear commit history. To clone the repository:

##### For **Mac** Users:

1. Open the **Terminal**.
2. Navigate to your preferred directory:  
   ```bash
   cd /path/to/your/directory
   ```
3. Clone the repository:  
   ```bash
   git clone https://github.com/RazmikMovsisyan/microblogify
   ```
4. Navigate into the directory:  
   ```bash
   cd Microblogify
   ```

##### For **Windows** Users:

1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the desired directory:  
   ```cmd
   cd C:\path\to\your\directory
   ```
3. Clone the repository:  
   ```cmd
   git clone https://github.com/RazmikMovsisyan/microblogify
   ```
4. Navigate into the directory:  
   ```cmd
   cd Microblogify
   ```

## Custom 404 Page

![error404](assets/images/error404.png)

A custom **404 error page** has been implemented to handle non-existent routes or broken links. Instead of a generic browser message, users are shown a friendly, styled error page that helps guide them back to the main site — improving overall user experience and navigation.


## Credits

All images featured in this project were sourced from **Stockimages**, ensuring high-quality visuals that enhance the overall design and user experience. These images were selected to complement the content and provide a clean, engaging aesthetic throughout the site.

The favicon used in this project was obtained from **Icons8**. Icons8 offers a wide variety of free and premium icons that are perfect for web development projects, and their favicon collection provided just the right visual touch for this site's branding.

Proper credit is given to all resources used in accordance with fair use and licensing guidelines.

A special thank to [Roman Rakic](https://github.com/rockroman) for reviewing my project during the 1:1 session and providing valuable feedback for the resubmission.

## Finished Product

![finished prodcut](assets/images/finished-product.png)![footer](assets/images/footer.png)![signup](assets/images/signup.png)![login](assets/images/login.png)![post-comment-screenshot](assets/images/post-and-comment-screenshot.png)![profile](assets/images/profile.png)