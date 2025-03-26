### **Session 3: Understanding Flutter Widgets and Layouts**  

#### **Objective:**  
By the end of this session, students will understand the core widget system in Flutter, including how to use basic layout widgets. They will be able to build simple UI structures and compare Flutter widgets to Tkinter components.  

---

### **1. Review and Warm-Up (10 mins)**  
- Quick recap of previous lessons: Dart basics and running a simple Flutter app in DartPad.  
- Discussion: What are widgets? How do they compare to Tkinter's widgets (e.g., `Label`, `Button`, `Frame`)?  
- Live Q&A on challenges from last session.  

---

### **2. Core Concept: Flutter's Widget System (15 mins)**  
- **Everything in Flutter is a Widget.**  
  - Types of Widgets:  
    - **StatelessWidget** (unchanging UI)  
    - **StatefulWidget** (UI that updates dynamically)  
- **Widgets as a Tree**  
  - Parent-child relationships (Widget composition)  
  - Comparison to Tkinter’s `Frame` and `Pack/ Grid`  
  - Explain `build()` method and how Flutter renders UI  

---

### **3. Exploring Basic Widgets (30 mins - Hands-on Coding)**  
- Open **DartPad** and guide students through these widgets:  
  - **Text Widget**: Display simple text  
  - **Container**: Adding background color, padding, and borders  
  - **Row & Column**: Organizing widgets in horizontal and vertical layouts  
  - **SizedBox**: Adding spacing between widgets  
  - **ElevatedButton**: Creating interactive buttons  

#### **Example Code: Basic Layout**
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Flutter Layouts")),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Hello, Flutter!", style: TextStyle(fontSize: 24)),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => print("Button Pressed"),
              child: Text("Press Me"),
            ),
          ],
        ),
      ),
    );
  }
}
```
- **Ask students to modify**: Change text size, add background color, or replace `Column` with `Row`.  

---

### **4. Activity: Recreate a Simple UI (30 mins)**  
**Task:** Students will create a basic profile card UI using the widgets they just learned.  
**Features:**  
- A `Text` widget for the name  
- An `ElevatedButton` for "Follow"  
- A `Column` layout  

**Example Layout:**  
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Profile Card")),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("John Doe", style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
              SizedBox(height: 10),
              ElevatedButton(
                onPressed: () {},
                child: Text("Follow"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
**Extensions:** Let students customize by adding an `Image` widget and colors.  

---

### **5. Wrap-Up and Homework (5 mins)**  
- **Recap:** What are `Column`, `Row`, `Container`, and `Text` widgets?  
- **Discuss:** How does this compare to Tkinter layouts?  
- **Homework Assignment:**  
  - Modify the profile card UI by adding an image using the `Image.network` widget.  
  - Try replacing `Column` with `Row` to see how the layout changes.  

---

### **Key Takeaways:**  
✅ Flutter’s UI is built entirely from widgets.  
✅ Stateless and Stateful widgets define UI behavior.  
✅ Layout widgets (`Row`, `Column`, `Container`) organize UI elements.  
✅ Flutter UI follows a widget tree structure similar to Tkinter's frame system.  

This session sets the foundation for UI development, preparing students for interactive layouts in the next class. 🚀
