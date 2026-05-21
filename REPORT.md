# Telegram To-Do Bot Report

## 1. Problem Statement

Many students and users need a simple way to manage daily tasks.

Mobile applications can be complicated or require installation. Telegram bots provide a fast and convenient solution because users can manage tasks directly inside Telegram.

The purpose of this project was to create a Telegram To-Do Bot using Python and aiogram with basic task management functions.

---

## 2. Solution Overview

The developed bot allows users to:

- add tasks;
- view tasks;
- delete tasks;
- clear all saved tasks.

All tasks are stored in `data.json`, which allows saving user data between bot sessions.

The project uses Object-Oriented Programming through the `TaskManager` class, which manages all operations related to tasks.

---

## 3. System Design

The system consists of several main components:

### Telegram Bot

Handles communication with users through Telegram commands and buttons.

### TaskManager Class

Responsible for:

- adding tasks;
- deleting tasks;
- loading data from JSON;
- saving data to JSON.

### JSON Storage

Tasks are stored in `data.json`.

This approach is simple and suitable for small projects.

### Keyboard Interface

Telegram reply keyboards improve usability and make interaction easier for users.

---

## 4. Challenges Faced

During development several challenges appeared:

- Understanding asynchronous functions in aiogram;
- Correctly saving and loading JSON data;
- Handling invalid user input;
- Organizing the project using OOP principles.

These problems were solved through testing and debugging.

---

## 5. Team Contributions

| Team Member | Contribution |
|---|---|
| Student 1 | Developed backend logic, Telegram bot commands, TaskManager class, CRUD operations and JSON storage |
| Student 2 | Prepared README, report and project documentation |
| Student 3 | Tested the bot, verified commands and integrated project components |

---

## 6. Conclusion

The project successfully achieved its goals.

The Telegram To-Do Bot works correctly and supports basic task management functions.

This project improved practical skills in:

- Python programming;
- aiogram framework;
- OOP concepts;
- file handling;
- exception handling;
- Telegram Bot API usage.

Future improvements:

- database support;
- reminders;
- deadlines;
- user authentication;
- notifications for unfinished tasks.