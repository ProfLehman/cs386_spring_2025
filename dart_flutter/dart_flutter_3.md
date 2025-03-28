
# 📅 Session 3: Flutter

🎯 ***Learning Objectives:**

By the end of this session, you will be able to:
- Recognize Flutter class structure
- Recognize Flutter Widgets
- Recognize Flutter layout options
- Create IPO app using Flutter

---
# Currency App Version 1

---
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: CurrencyConverter(),
    );
  }
}

class CurrencyConverter extends StatefulWidget {
  @override
  _CurrencyConverterState createState() => _CurrencyConverterState();
}

class _CurrencyConverterState extends State<CurrencyConverter> {
  final TextEditingController usdController = TextEditingController();
  double convertedAmount = 0.0;
  static const double conversionRate = 1.35; // Example rate: 1 USD = 1.35 CAD

  void convertCurrency() {
    double? usdAmount = double.tryParse(usdController.text);
    if (usdAmount != null) {
      setState(() {
        convertedAmount = usdAmount * conversionRate;
      });
    } else {
      // Show error if input is invalid
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a valid number')),
      );
    }
  }

  void clearFields() {
    setState(() {
      usdController.clear();
      convertedAmount = 0.0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("USD to CAD Converter")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              "Enter USD amount:",
              style: TextStyle(fontSize: 18),
            ),
            TextField(
              controller: usdController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                hintText: "Enter amount in USD",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: convertCurrency,
              child: Text("Convert"),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: clearFields,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
              child: Text("Clear"),
            ),
            SizedBox(height: 20),
            Text(
              "Converted Amount: ${convertedAmount.toStringAsFixed(2)} CAD",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}

```
---

## **🛠️ Code Breakdown and Explanation**

---

### **1️⃣ Importing Flutter Packages**
```dart
import 'package:flutter/material.dart';
```
✅ **What it does:**  
- This imports Flutter's **Material Design UI framework**, which provides pre-built widgets like buttons, text fields, and layouts.
- In **Tkinter**, you’d do something similar with:
  ```python
  from tkinter import *
  ```

---

### **2️⃣ The `main()` Function – Starting the App**
```dart
void main() {
  runApp(MyApp());
}
```
✅ **What it does:**  
- `main()` is the **entry point** of the Flutter app.
- `runApp(MyApp())` **launches** the application, just like how `root.mainloop()` in Tkinter starts the GUI loop.

---

### **3️⃣ Creating the Root Widget – `MyApp` Class**
```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: CurrencyConverter(),
    );
  }
}
```
✅ **What it does:**  
- This is the **main application widget**.
- `MaterialApp`:
  - Wraps the whole app in a **Material Design theme**.
  - **`home:`** Defines the **starting screen** (`CurrencyConverter`).
  - **`debugShowCheckedModeBanner: false`** removes the debug banner in the top-right corner.

🔍 **Comparison to Tkinter**  
- In Tkinter, you’d define a root window:
  ```python
  root = Tk()
  root.title("Currency Converter")
  ```

---

### **4️⃣ Creating the UI as a Stateful Widget**
```dart
class CurrencyConverter extends StatefulWidget {
  @override
  _CurrencyConverterState createState() => _CurrencyConverterState();
}
```
✅ **What it does:**  
- **Stateful Widget** = A widget that **remembers and updates its state**.
- This is like **Tkinter's `StringVar()`** or `IntVar()` to update labels dynamically.

🔍 **Why is this needed?**  
- The conversion results **change dynamically**, so we use a **StatefulWidget** instead of `StatelessWidget`.

---

### **5️⃣ The `_CurrencyConverterState` Class (Manages UI & Logic)**
```dart
class _CurrencyConverterState extends State<CurrencyConverter> {
```
✅ **What it does:**  
- This manages the **UI state** for our converter.
- It stores **user input** and **conversion results**.

---

### **6️⃣ Initializing Variables**
```dart
final TextEditingController usdController = TextEditingController();
double convertedAmount = 0.0;
static const double conversionRate = 1.35; // Example rate: 1 USD = 1.35 CAD
```
✅ **What it does:**  
- **`usdController`** → Works like `Entry()` in Tkinter, managing text input.
- **`convertedAmount`** → Stores the converted amount.
- **`conversionRate`** → A constant for USD to CAD conversion.

🔍 **Tkinter Equivalent:**
```python
usd_entry = Entry(root)
usd_var = DoubleVar()
```

---

### **7️⃣ Converting the USD Amount**
```dart
void convertCurrency() {
  double? usdAmount = double.tryParse(usdController.text);
  if (usdAmount != null) {
    setState(() {
      convertedAmount = usdAmount * conversionRate;
    });
  } else {
    // Show error if input is invalid
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Please enter a valid number')),
    );
  }
}
```
✅ **What it does:**  
- **Reads user input** from `usdController.text`.
- **Converts it to a number** using `double.tryParse()`.
- **Updates the UI** with `setState()`, triggering a refresh.
- **Shows an error message** if input is invalid.

🔍 **Tkinter Equivalent:**
```python
def convert():
    try:
        usd = float(usd_entry.get())
        converted = usd * 1.35
        result_label.config(text=f"Converted: {converted} CAD")
    except ValueError:
        result_label.config(text="Invalid input!")
```

---

### **8️⃣ Clearing the Input Fields**
```dart
void clearFields() {
  setState(() {
    usdController.clear();
    convertedAmount = 0.0;
  });
}
```
✅ **What it does:**  
- **Clears the text field**.
- **Resets the converted amount**.

🔍 **Tkinter Equivalent:**
```python
def clear():
    usd_entry.delete(0, END)
    result_label.config(text="")
```

---

### **9️⃣ Building the UI with `Scaffold`**
```dart
@override
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(title: Text("USD to CAD Converter")),
    body: Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
```
✅ **What it does:**  
- **`Scaffold`** → Provides a basic app structure (like `Frame` in Tkinter).
- **`AppBar`** → Adds a title bar.
- **`Padding`** → Adds spacing around the widgets.
- **`Column`** → Arranges elements **vertically** (like `pack(side=TOP)` in Tkinter).

---

### **🔟 Creating the Input TextField**
```dart
TextField(
  controller: usdController,
  keyboardType: TextInputType.number,
  decoration: InputDecoration(
    hintText: "Enter amount in USD",
    border: OutlineInputBorder(),
  ),
),
```
✅ **What it does:**  
- `controller: usdController` → Controls the input text.
- `keyboardType: TextInputType.number` → Ensures only numbers are entered.
- `decoration` → Adds a placeholder (`hintText`) and border.

🔍 **Tkinter Equivalent:**
```python
usd_entry = Entry(root)
usd_entry.pack()
```

---

### **🔟 Adding Buttons (Convert & Clear)**
```dart
ElevatedButton(
  onPressed: convertCurrency,
  child: Text("Convert"),
),
SizedBox(height: 10),
ElevatedButton(
  onPressed: clearFields,
  style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
  child: Text("Clear"),
),
```
✅ **What it does:**  
- `ElevatedButton` → A clickable button.
- **Calls `convertCurrency()`** when pressed.
- **`SizedBox(height: 10)`** → Adds spacing between buttons.
- **Changes the "Clear" button color** to red.

🔍 **Tkinter Equivalent:**
```python
convert_button = Button(root, text="Convert", command=convert)
clear_button = Button(root, text="Clear", command=clear)
```

---

### **🔟 Displaying the Converted Amount**
```dart
Text(
  "Converted Amount: ${convertedAmount.toStringAsFixed(2)} CAD",
  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
),
```
✅ **What it does:**  
- Dynamically updates **convertedAmount**.
- `toStringAsFixed(2)` → Formats to **2 decimal places**.

🔍 **Tkinter Equivalent:**
```python
result_label = Label(root, text="Converted Amount: 0.00 CAD")
```

---

## 🎯 **Final Summary**
| **Feature**       | **Flutter Equivalent**           | **Tkinter Equivalent**       |
|-------------------|--------------------------------|-----------------------------|
| **Text Input**    | `TextField(controller: usdController)` | `Entry()` |
| **Buttons**       | `ElevatedButton(onPressed: func)` | `Button(command=func)` |
| **Layouts**       | `Column()`, `Padding()`        | `pack(), grid()` |
| **Updating UI**   | `setState(() {...})`          | `StringVar().set()` |
| **Error Handling**| `tryParse()` + `SnackBar()`   | `try/except ValueError` |

---

## Generic IPO Example

See **IPO template example.md** posted on GitHub.

---
🚀 **Next Session:** More Flutter Basics

---

## 🏠 **Homework - Part C. - Due: Monday 3/31**

1. Create a basic IPO app that inputs one (or more) numeric values. May not be class example posted.
2. Add a "Calculate" or equivelent button that uses the input to perform a calculation
3. Add a label to display the results of your calculation
4. Add a clear button to clear your input textbox and output label
3. Place code in file **part3.dart**.  Add filename, your name, date, description to comments at top of file.

-- end --

