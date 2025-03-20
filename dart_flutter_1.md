
### **📅 Week 1, Session 1: Dart Basics & DartPad Intro (Expanded with More Examples)**

🎯 **Objective:** Understand Dart's syntax, data types, and basic control structures through hands-on examples and comparisons with Python.

---

## **1️⃣ Introduction to Dart & DartPad (5 min)**

- **What is Dart?**
    
    - Developed by Google for building mobile, web, and server applications.
    - **Strongly typed** (unlike Python, which is dynamically typed).
    - Used in **Flutter** to create fast and efficient UI applications.
- **DartPad Setup** (💡 No installation needed! Run Dart code online at [dartpad.dev](https://dartpad.dev/)).
    
- **Basic Syntax Overview**
    
    - Dart **requires** `main()` function, unlike Python.
    - Every statement **ends with a semicolon (`;`)** (like Java, C++).
    - Comments:
        
        ```dart
        // Single-line comment
        /* Multi-line
           comment */
        ```
        

---

## **2️⃣ Variables & Data Types (10 min)**

### **💡 Example 1: Declaring Variables**

```dart
void main() {
  int age = 25; // Integer
  double pi = 3.1415; // Floating-point number
  String name = "Alice"; // String
  bool isFlutterFun = true; // Boolean

  print("Age: $age");
  print("Pi: $pi");
  print("Name: $name");
  print("Is Flutter fun? $isFlutterFun");
}
```

**🔹 Python Comparison**

```python
age = 25  # int
pi = 3.1415  # float
name = "Alice"  # str
is_flutter_fun = True  # bool

print(f"Age: {age}")
print(f"Pi: {pi}")
print(f"Name: {name}")
print(f"Is Flutter fun? {is_flutter_fun}")
```

📌 **Key Difference:**

- Dart requires explicit types (`int`, `double`, `String`), whereas Python **infers types automatically**.

### **💡 Example 2: Dynamic Typing with `var` and `dynamic`**

```dart
void main() {
  var name = "Bob"; // Automatically inferred as String
  dynamic age = 30; // Can change type
  age = "thirty"; // No error because it's dynamic

  print("Name: $name");
  print("Age: $age");
}
```

📌 **Key Takeaway:**

- `var` has **type inference** (it gets locked once assigned).
- `dynamic` can **change types**, but this can lead to **runtime errors**.

---

## **3️⃣ Lists & Maps (10 min)**

### **💡 Example 3: Lists in Dart (Similar to Python Lists)**

```dart
void main() {
  List<String> names = ["Alice", "Bob", "Charlie"];
  names.add("David"); // Add an item
  print("First Name: ${names[0]}");
  print("All Names: $names");
}
```

**🔹 Python Comparison**

```python
names = ["Alice", "Bob", "Charlie"]
names.append("David")
print(f"First Name: {names[0]}")
print(f"All Names: {names}")
```

📌 **Key Takeaway:**

- **Dart lists require a type** (`List<String>`), while Python lists can contain mixed types.

### **💡 Example 4: Maps in Dart (Like Python Dictionaries)**

```dart
void main() {
  Map<String, int> ages = {"Alice": 25, "Bob": 30, "Charlie": 22};
  print("Alice's Age: ${ages["Alice"]}");
  ages["David"] = 28; // Add new entry
  print("All Ages: $ages");
}
```

**🔹 Python Comparison**

```python
ages = {"Alice": 25, "Bob": 30, "Charlie": 22}
print(f"Alice's Age: {ages['Alice']}")
ages["David"] = 28
print(f"All Ages: {ages}")
```

📌 **Key Takeaway:**

- Dart Maps require explicit **key-value types**, while Python dictionaries do not.

---

## **4️⃣ Control Flow Statements (10 min)**

### **💡 Example 5: If-Else Statements**

```dart
void main() {
  int age = 20;

  if (age >= 18) {
    print("You are an adult.");
  } else {
    print("You are a minor.");
  }
}
```

**🔹 Python Comparison**

```python
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### **💡 Example 6: Loops (For & While)**

#### **For Loop**

```dart
void main() {
  for (int i = 1; i <= 5; i++) {
    print("Count: $i");
  }
}
```

**🔹 Python Comparison**

```python
for i in range(1, 6):
    print(f"Count: {i}")
```

#### **While Loop**

```dart
void main() {
  int i = 1;
  while (i <= 5) {
    print("Number: $i");
    i++;
  }
}
```

**🔹 Python Comparison**

```python
i = 1
while i <= 5:
    print(f"Number: {i}")
    i += 1
```

---

## **5️⃣ Functions (10 min)**

### **💡 Example 7: Simple Function**

```dart
void greet(String name) {
  print("Hello, $name!");
}

void main() {
  greet("Alice");
}
```

**🔹 Python Comparison**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### **💡 Example 8: Function with Return Value**

```dart
int add(int a, int b) {
  return a + b;
}

void main() {
  int sum = add(5, 7);
  print("Sum: $sum");
}
```

**🔹 Python Comparison**

```python
def add(a, b):
    return a + b

sum = add(5, 7)
print(f"Sum: {sum}")
```

---

## **6️⃣ Hands-on Exercise (10 min)**

**📝 Quick Coding Tasks for Students**

1. **Write a Dart function** that takes a number and returns whether it's even or odd.
2. **Modify Example 3**: Create a `List<int>` and print only the even numbers using a loop.
3. **Write a function** that converts a temperature from **Celsius to Fahrenheit**.

---

## **7️⃣ Wrap-up & Homework (5 min)**

✅ **Recap Key Concepts**: Variables, Lists, Maps, Loops, Functions  
🏡 **Outside Work:**

- Modify the function to handle **negative temperatures**.
- Write a Dart function that takes a list of numbers and returns the **largest number**.

---

### **📌 Key Takeaways from Session 1**

✅ Dart is **strongly typed** (unlike Python).  
✅ Lists (`List<int>`), Maps (`Map<String, int>`) require **explicit types**.  
✅ Functions use `void` (no return) or a **specific return type**.  
✅ Loops (`for`, `while`) are similar to Python but use `{}`.

🚀 **Next Session:** Object-Oriented Programming & Async in Dart!

---
