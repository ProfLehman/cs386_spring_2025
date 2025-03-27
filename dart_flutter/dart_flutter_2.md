
# 📅 Session 2: Object-Oriented Dart & Async Programming

🎯 ***Learning Objectives:**

By the end of this session, you will be able to:
- Define classes and objects in Dart, 
- Use constructors to initialize objects
- Understand how and why Dart uses `Future`, `async`, and `await`
- Write non-blocking code using Dart’s async features

---

## 🧠 Why Learn OOP and Async?

> Flutter apps need to:
- ✅ Organize code using **classes**
- ✅ Fetch data and perform tasks without freezing the UI

Dart gives us:
- 🧱 Object-Oriented Programming
- ⚡ Asynchronous Programming

These are foundational for building responsive, maintainable apps.

---

## 🧱 Dart Class Basics

```dart
class Student {
  String name;
  int age;

  Student(this.name, this.age);

  void greet() {
    print('Hi, I’m $name and I’m $age years old.');
  }
}
```

- `this.name` assigns constructor parameter to the instance variable
- A Dart class = blueprint for objects

---

## 🛠 Creating Objects

```dart
void main() {
  Student s1 = Student('Alice', 20);
  s1.greet();
}
```

- `Student` is a custom type
- This is how you instantiate and use objects

---

## 🔄 Dart vs Python (Quick Comparison)

| Concept      | Dart                                | Python                              |
|--------------|-------------------------------------|--------------------------------------|
| Class        | `class Student {}`                  | `class Student:`                     |
| Constructor  | `Student(this.name, this.age)`      | `def __init__(self, name, age)`      |
| Create obj   | `Student('A', 20)`                  | `Student('A', 20)`                   |

---

## 🧩 Named Constructor Parameters

```dart
class Book {
  String title;
  String author;

  Book({required this.title, this.author = 'Unknown'});
}
```

- Cleaner and more readable
- Order doesn’t matter
- Optional values supported

---

## ⚡ Async Programming in Dart

---

### 🤔 Why Use Async?

Without async:
- ❌ App freezes while waiting (e.g., API calls)

With async:
- ✅ UI stays responsive
- ✅ User experience improves

Async lets Dart **wait** without blocking the app.

---

### 🔍 What is a `Future`?

```dart
Future<void> fetchData() async {
  print('Fetching...');
  await Future.delayed(Duration(seconds: 2));
  print('Done!');
}
```

- `await` pauses function but **not the app**
- Dart continues running other tasks

---

### 📈 Async Execution Flow Example

```dart
print('Start');
await Future.delayed(Duration(seconds: 1));
print('End');
```

**Output:**
```
Start
End
(after 1 sec)
Done!
```

✅ Dart uses **single-threaded event loop**  
❌ No threads are created

---

### 🔁 Async Inside a Class

```dart
class Downloader {
  Future<void> downloadFile() async {
    print('Downloading...');
    await Future.delayed(Duration(seconds: 1));
    print('Download complete.');
  }
}

void main() {
  Downloader d = Downloader();
  d.downloadFile();
  for (int i=0; i< 100; i++)
  {
    print( i );
  }
}

```

Combine **OOP + async** for real-world features like downloading, uploading, etc.

---

## 🧪 In-Class Challenge

**Task: Build a `Person` class**
- Fields: `name`, `email`
- Method: `introduce()` prints both
- Method: `delayedIntro()` (async) — prints after 2 seconds

---
🚀 **Next Session:** Flutter Introduction

---

## 🏠 **Homework - Part B. - Due: Friday 3/28**

1. Convert **Problem Set #3 - Part A. Pet Class** to Dart and demonstrate each of the methods.
2. Update the speak method to use Future and delay speak by 3 seconds.
3. Place code in file **part2.dart**.  Add filename, your name, date, description to comments at top of file.
4. You can use AI, but make sure you edit responses to match your understanding ie. may need to fine-tune or simplify approach to make sure you understand and can explain any code submitted.

-- end --

