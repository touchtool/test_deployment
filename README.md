# skdue
[![Build Status](https://app.travis-ci.com/patkamon/skdue.svg?branch=apply-ci)](https://app.travis-ci.com/patkamon/skdue) [![codecov](https://codecov.io/gh/patkamon/skdue/branch/apply-ci/graph/badge.svg?token=5EZP9GP4CX)](https://codecov.io/gh/patkamon/skdue)


## Description

**Skdue** is a web application that makes your life easier by helping you manage your schedule. With the ability which allows you to create and manage your activities and events, you will never miss any of them. What makes Skdue stand out from the other calendar applications is the feature that lets you follow your favorite people, companies, or celebrities and add their events to your schedule.

## Team Members

| Name    | GitHub                                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Ditthapong         | [HuskyIsHere](https://github.com/HuskyIsHere)  |
| Kittison  | [touchtool](https://github.com/touchtool)                                           |
| Natchanon | [natchanon-space](https://github.com/natchanon-space)                                                    |
| Patkamon | [patkamon](https://github.com/patkamon)                                                    |
| Thanabardi | [Thanabardi](https://github.com/Thanabardi)                                                     |

## Setup

- ### Django Setup
  ```
  # activate virtual environment
  source venv/bin/activate
  ```
  ```
  # install dependencies
  pip install -r requirements.txt
  ```
  ```
  # setup database
  python manage.py migrate
  python manage.py loaddata calendar_data
  ```
  ```
  # run server and explorer api
  python manage.py runserver
  ```

- ### Vue Setup
  ```
  # install vue
  npm install -g @vue/cli
  ```
  ```
  # install dependencies
  cd calendar_vue
  npm install
  ```
  ```
  # run frontend sever
  npm run serve
  ```
  [readmore](/../../wiki/Getting-Started)

## Iterantion Plan

<details>
  <summary> Iteration Plan 1 </summary>
  <p>

  #### Goals
  * This application has a working calendar.
  * Users can create a calendar and add events to it.

  #### Features
  * Display list of calendars.
  * Users can create a new calendar.
  * Events can be added or removed from the calendar.
  * Each event has basic information like date, time, description, and name.

  #### Evaluation Criteria
  * All features are working correctly.
  * After installation, the index page must have a calendar with Thai national holidays.

  #### Milestones
  A working minimal calendar that allows you to create an event.

  [readmore](/../../wiki/Iteration-Plan-1)

</p>
  </details>

<details>
  <summary> Iteration Plan 2 </summary>
  <p>

  #### Goals
* Refactoring the component in the application.
* Improving some subsystems to be more sufficiently.
* Deploy the first version.

#### Features
* Working navigation bar with search.
* Working sidebar with an event, calendar details.

#### Evaluation Criteria
* All features are working correctly.
* The application should look like a mock-up.
* The application is successfully deployed.

#### Milestones
Improving and refactoring the component vue of project to look like the mockup and fixing some bugs about API. Create the login form and deploy the first version of the project on hiroku.

  [readmore](/../../wiki/Iteration-Plan-2)

  </p>
    </details>

  <details>
    <summary> Iteration Plan 3 </summary>
    <p>
</p>
  </details>

  <details>
    <summary> Iteration Plan 4 </summary>
    <p>
</p>
  </details>

  <details>
    <summary> Iteration Plan 5 </summary>
    <p>
</p>
  </details>

## Project Documents

* [Project Proposal](https://docs.google.com/document/d/1ZdIS9-_TD_CAAROzRfGB1QxAL8mmSFebVxw4AjWr2yQ/edit#heading=h.pe6wpztc0dwa)
* [Project Jamboard](https://jamboard.google.com/d/1iB_wpYj0qTMekB9jfVZLBmZ4JiU3f6bvgBLjktGU23o/edit?usp=sharing)
* [Django Rest Model](https://drive.google.com/file/d/1Xu2_mMAfK72p_U584PJ2d0ifFIC8Fjo2/view?usp=sharing)
* [Vision Statement](./Vision-Statement)
[readmore](/../../wiki#project-documents)
