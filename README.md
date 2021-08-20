# MLH-Holiday Planner Web app 
## https://holidayplanner.tech

## Usage 

1. Download Docker and docker-compose and make sure they are running
2. Clone the repository 
3. Make a local copy of `.env` file following `example.env`
4. Obtain a Skyscanner API key from: https://rapidapi.com/skyscanner/api/skyscanner-flight-search/ and add into the `.env`. file 
5. Start development environment:

```
$ docker-compose up --build -d
```
Access the flask app at http://localhost:5000/ 

Any changes to HTML front-end and back-end will be reflected by hitting refresh in the browser.
To install additional Flask packages, re-run docker-compose up build command.

## More about MLHolidays 

### Inspiration
While brainstorming project ideas, one of our team members mentioned how difficult it was to plan their vacation. This got us thinking about what can be improved in the process and noticed how tedious it was to organise a trip across multiple bookings. Our aim was to solve the problem of having to juggle between different websites, so we built a platform which combines all of the necessary features. 

### What it does
Our app makes it easier for people to plan their holiday trips. With an easy to use flight search and soon to come hotel search, users can quickly find accommodations for wherever they plan a visit. It relieves the stress of planning vacations so you can avoid the hassle and spend more time enjoying your holiday. 

### How we built it

In our team of four, we split the project into front-end, back-end, and devops then we assigned each person to a part to complete asynchronously. For the frontend, we used Jinja templating with pure HTML and CSS along with bootstrap to make our page responsive. In the back-end, we built a web server with python and flask which communicated with a postgreSQL database. The app is deployed on an AWS EC2 instance on a CentOS machine and is fully dockerised with a working CI/CD pipeline built with GitHub Actions. 

### What we learned
In regards to the front end for our application, we learned a lot about working with bootstrap files for designing and jquery files for the animations. This project helped us further our knowledge in flask, specifically the flask file structure and implementing sessions. We learned a great deal about working with APIs and integrating them into our web app.  It also helped us enhance our knowledge about github, python, docker, nginx and postgresql. We were also able to get familiar with monitoring tools such as prometheus and grafana. 

### What's next for MLHolidays
Integrating a hotel and car rental api with the listings endpoint. Adding a travel endpoint which uses web scraping to extract data from tripadvisor.com. 

## Tech Stack 

### Front-end 
    HTML 
    CSS 
    Bootstrap 
 
### Back-end 
    Flask 
    PostgreSQL 
    Docker 
    
