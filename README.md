# To-Do Management Module - Odoo 19

A custom Odoo 19 module for managing tasks through a simple and organized To-Do system.

## Features

- Create and manage tasks
- Assign tasks to users
- Track task status:
  - New
  - In Progress
  - Completed
- Add task descriptions
- Set due dates
- Search and filter tasks
- Group tasks by:
  - Assigned User
  - Status
  - Due Date
- Chatter
---

## Technologies

- Odoo 19
- Python 3.12.10
- PostgreSQL 18

---

## Module Structure

### Model

#### `todo.task`

Fields:

- `name` → Task Name
- `assign_to` → Assigned User
- `description` → Task Description
- `due_date` → Due Date
- `status` → Task Status

---

## Views

### List View

Displays all tasks with key information.

### Form View

Allows users to:

- Create tasks
- Edit tasks
- Update task status

### Search View

Includes:

- Search by Task Name
- Search by Assigned User
- Filters by Status
- Group By options:
  - Assign To
  - Status
  - Due Date

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arafet-T/your-repository.git
```

### 2. Copy the module

Copy the module into your Odoo custom addons directory.

### 3. Start Odoo

```bash
python odoo-bin --addons-path=addons,custom_addons
```

### 4. Install the module

- Activate Developer Mode
- Go to **Apps**
- Click **Update Apps List**
- Search for the module 'To-Do List'
- Click **Activate**

---

## Requirements

- Python 3.12.10
- PostgreSQL 18
- Odoo 19

---

## Future Improvements

- Email notifications
- Kanban view
- Task priorities
- Activity reminders
- Dashboard statistics

---

## Author

Developed as part of an Odoo learning/project exercise.