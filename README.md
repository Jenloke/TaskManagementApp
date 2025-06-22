# Task Management Application

> STATUS: ONGOING

## Stack Used

- Python 3.12.9
- PyMongo
- Datetime alonside timezone for UTC compliance
- _Optional_ venv (if PyMongo isn't installed globbaly but that's bad practice)

### Task Object

| Name               | Values                         |
| ------------------ | ------------------------------ |
| task_id            | integer                        |
| title              | string                         |
| description        | string                         |
| due_date           | datetime with utc              |
| priority_level     | 1=High, 2=Medium, 3=Low        |
| status             | 1=Open, 2=Ongoing, 3=Completed |
| creation_timestamp | datetime with utc              |

### Functionalities

- **ADD** Task
- **READ** all Task list from Database
- **UPDATE** a specific task, based on task_id
- **UPDATE** a specifiic task to be completed, based on task_id
- **DELETE** a specific task, based on task_id

### TO DO Left

- Create DB if not yet created or connected cause current solution assumes DB is up and running
- Complete other functionalities
- Exception Handling
- Utilize the Task class after getting the current state of the collection
- Create ENUMS for priority and status fields
- Utilize TaskManager class
