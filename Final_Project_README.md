# 📘 CS 386 Final Project Requirements
**Course Project Presentation:**  
🗓️ **Wednesday, April 30th**  
🕥 **10:30 AM** (during the final exam session)

---

## 🔍 Project Overview
Each student will design and build a functional application—**web**, **desktop**, or **mobile**—that integrates the key concepts covered in this course. Your project must demonstrate both **technical competency** and **good software design practices**.

You may use **either Dart/Flutter or Python** as your development language.

---

## ✅ Required Features

### 1. **Language & Platform**
- ✅ You may choose **Python** or **Dart/Flutter**.
- ✅ Your project must be able to:
  - **Save and open data** if using **Python**.
  - **Read or open data** (from files or a database) if using **Dart/Flutter**.

### 2. **Object-Oriented Design**
- Your project must use an **object-oriented architecture**.
- Follow a **Model-View** structure:
  - `Model` → handles data and business logic.
  - `View` → GUI using Tkinter (Python) or Flutter widgets (Dart).
  - Optional: separate a `Controller` if you prefer MVC.

### 3. **Data Input/Output**
- Your app must save/load data from:
  - A file (e.g., `.json`, `.txt`, `.csv`)
  - Or a database (e.g., SQLite, Hive, Firebase)
- This should be a core feature of your app (not just a demo).

### 4. **GUI and UX**
- Your app must include a **graphical user interface**.
- Use good design practices (clear layout, intuitive interactions, consistent styling).

### 5. **Source Code Management**
- Push your full project to **GitHub**.
- Submit your project by **sharing the GitHub link**.
- Use clear commit messages and organize your repository with folders like:
  - `/lib` or `/src`
  - `/assets`
  - `/test`

---

## 📄 Required Documentation

### A. **README.md File**  
Your GitHub repository must include a well-written `README.md` file that serves as a user and developer guide.

It should contain:

1. **Project Introduction**  
   - What does your app do?
   - Who is the target user?

2. **Design and Architecture**
   - Description of how the app is structured.
   - Include **Mermaid class diagrams** for major classes.
     - Example:
       ````markdown
       ```mermaid
       classDiagram
         class Person {
           - String name
           - String email
           + fromJson()
         }
         PersonList --> Person
       ```
       ````

3. **Instructions**
   - How to install or run the app.
   - How to use key features (add screenshots or GIFs if helpful).
   - How to test it (describe any unit testing or manual testing done).

4. **Challenges and Insights**
   - What problems did you face and solve?
   - What did you learn about GUI design, programming, or tools?

5. **Next Steps**
   - If you had more time, what would you improve, add, or refactor?
   - Any features you'd like to explore in the future?

---
### Point Breakdown

| Component    | **Percent |
| -------- | ------- |
| Project Functionality and Complexity  | 50% |
| Internal Code Documentation  | 10% |
| OOP Design | 10% |
| Data Input/Output | 10%|
| Documentation    | 20% |


---
## 📣 Presentation Guidelines (April 30)
- Prepare a **5–8 minute live demo or screen recording**.
- Walk through your app and briefly explain your code structure.
- Highlight features and data input/output.
- Share **1 key challenge** and how you solved it.

---
--end--
---
