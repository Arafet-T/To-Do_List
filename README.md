# To-Do Management Module - Odoo 19

A custom Odoo 19 module for managing tasks through a simple and organized To-Do system.

---

## Features

### Task Management

- Create and manage tasks
- Assign tasks to users
- Track task status:
  - New
  - In Progress
  - Completed
- Add task descriptions
- Set due dates

---

## Advanced Features

### Timesheet Management

- Add an **Estimated Time** field to tasks
- Record multiple timesheet lines related to a task
- Track spent time on each task
- Validation to ensure:
  - Total recorded time does not exceed the estimated time

### Archiving

- Archive completed or unused tasks
- Restore archived tasks when needed
- Preserve task history safely

### Server Actions

A custom server action named **Close** allows users to:

- Close one task
- Close multiple tasks at once
- Update task status directly from list view

### Scheduled Actions (Cron Job)

Automated scheduled actions are included to:

- Detect overdue tasks based on the **Due Date**
- Notify users about late tasks
- Highlight overdue tasks in the tree/list view

### Report Generation

Users can print task reports directly from Odoo.

Features:

- Printable task reports
- Clean report design
- Export and print task information easily

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
- `estimated_time` → Estimated Time

---

## Views

### List View

Displays all tasks with their main information.

### Form View

Allows users to:

- Create tasks
- Edit tasks
- Manage timesheet lines
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
git clone https://github.com/your-username/your-repository.git
```

### 2. Copy the module

Copy the module into your Odoo custom addons directory.

### 3. Start Odoo

```bash
python odoo-bin --addons-path=addons,custom_addons
```

### 4. Install the module

- Activate Developer Mode
- Open **Apps**
- Click **Update Apps List**
- Search for the module
- Click **Install**

---

## Requirements

- Python 3.12.10
- PostgreSQL 18
- Odoo 19


---

## Project Structure

```text
todo_management/
│
├── models/
├── reports/
├── security/
├── static/
├── views/
├── __init__.py
├── __manifest__.py
└── README.md
```

---

## Future Improvements

- Email notifications
- Telegram notifications
- Kanban view
- Task priorities
- Dashboard statistics
- Real-time notifications
- AI-based task reminders

---

## Author

Developed as part of an Odoo learning/project exercise.
