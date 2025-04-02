# List View

Copy and paste code into DartPad

---

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dynamic ListView Demo',
      theme: ThemeData(primarySwatch: Colors.teal),
      home: ListViewExample(),
    );
  }
}

class ListViewExample extends StatelessWidget {
  // Dynamic list of items with title and description
  final List<Map<String, String>> items = [
    {'title': 'Apple', 'description': 'Apples are sweet and crunchy.'},
    {'title': 'Banana', 'description': 'Bananas are high in potassium.'},
    {'title': 'Cherry', 'description': 'Cherries are small and red.'},
    {'title': 'Date', 'description': 'Dates are chewy and sweet.'},
    {'title': 'Elderberry', 'description': 'Elderberries are used in syrups.'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Fruits List'),
      ),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          final item = items[index];
          return ListTile(
            leading: CircleAvatar(child: Text('${index + 1}')),
            title: Text(item['title']!),
            subtitle: Text('Tap to learn more...'),
            trailing: Icon(Icons.arrow_forward_ios),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => DetailScreen(
                    title: item['title']!,
                    description: item['description']!,
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  final String title;
  final String description;

  DetailScreen({required this.title, required this.description});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(
          description,
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}

```


## 🧩 App Structure Overview

The app has two main screens:
1. **Main screen** with a dynamic `ListView` of items
2. **Detail screen** that displays a description for the tapped item

It demonstrates:
- **Dynamic lists** using `List<Map<String, String>>`
- **Navigation** between screens
- **Passing data** to another screen

---

## 🧱 Main Components

### `main()` and `MyApp`
```dart
void main() => runApp(MyApp());
```
This is the entry point of the app. It runs the `MyApp` widget.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dynamic ListView Demo',
      theme: ThemeData(primarySwatch: Colors.teal),
      home: ListViewExample(),
    );
  }
}
```
- `MaterialApp` wraps the whole app and provides themes, routing, etc.
- `home` sets the starting screen to `ListViewExample`.

---

## 📜 `ListViewExample` – The Main Screen

```dart
final List<Map<String, String>> items = [
  {'title': 'Apple', 'description': 'Apples are sweet and crunchy.'},
  ...
];
```
- A dynamic list using a `List<Map<String, String>>`, each item with a `title` and `description`.

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    final item = items[index];
    ...
  },
)
```
- `ListView.builder` efficiently creates a scrolling list.
- `itemCount` tells how many items to build.
- `itemBuilder` defines how each row (item) is built.

### `ListTile` in Each Row

```dart
ListTile(
  leading: CircleAvatar(child: Text('${index + 1}')),
  title: Text(item['title']!),
  subtitle: Text('Tap to learn more...'),
  trailing: Icon(Icons.arrow_forward_ios),
  onTap: () { ... }
)
```
Each list item shows:
- A circle with the item number
- The fruit name as the `title`
- A subtitle hint
- A right arrow icon
- And a `tap handler` to go to the detail screen

---

## 📲 Navigation to Detail Screen

```dart
Navigator.push(
  context,
  MaterialPageRoute(
    builder: (context) => DetailScreen(
      title: item['title']!,
      description: item['description']!,
    ),
  ),
);
```

- `Navigator.push` is how you go to a new screen.
- `MaterialPageRoute` is used to define the transition.
- Data (title and description) is passed to `DetailScreen` via its constructor.

---

## 🧾 `DetailScreen` – Second Screen

```dart
class DetailScreen extends StatelessWidget {
  final String title;
  final String description;

  DetailScreen({required this.title, required this.description});
```

- This screen receives the `title` and `description` passed from the first screen.

```dart
AppBar(title: Text(title)),
body: Padding(
  padding: const EdgeInsets.all(16.0),
  child: Text(
    description,
    style: TextStyle(fontSize: 18),
  ),
),
```
- Shows the `title` in the app bar
- Displays the `description` in the body

---

## ✅ Summary of Concepts Used

| Concept                | Description                                              |
|------------------------|----------------------------------------------------------|
| `ListView.builder`     | Builds a dynamic list efficiently                        |
| `List<Map<String, String>>` | Stores item data (title + description)             |
| `ListTile`             | A ready-to-use widget for list rows                      |
| `Navigator.push`       | Navigates to another screen                              |
| Constructor parameters | Pass data between screens                                |

---

Absolutely! Let's dive into how `ListView.builder` works in Flutter.

---

## 🧱 What is `ListView.builder`?

`ListView.builder` is a constructor for the `ListView` widget that **builds list items lazily**—only when they're about to appear on the screen. This makes it much more **efficient** for long or dynamic lists.

---

## 🧪 Syntax

```dart
ListView.builder({
  required int itemCount,
  required IndexedWidgetBuilder itemBuilder,
})
```

### 🔹 Parameters:

| Parameter     | Description |
|---------------|-------------|
| `itemCount`   | How many items should be built. Usually the length of your list. |
| `itemBuilder` | A function that returns a widget for each item index. It's called as needed. |

---

## 🛠️ Example Use

```dart
ListView.builder(
  itemCount: fruits.length,
  itemBuilder: (context, index) {
    return ListTile(
      title: Text(fruits[index]),
    );
  },
)
```

### What this does:
- Let's say `fruits = ['Apple', 'Banana', 'Cherry']`
- Flutter will call `itemBuilder` for `index` 0, 1, 2...
- It only builds widgets that are visible on screen (great for performance).

---

## 🧠 Why Use It?

### ✅ Efficient for long lists
Instead of building 1,000 widgets up front, it builds only what’s visible.

### ✅ Works well with dynamic data
You can display lists where the content is loaded from a database, API, or user input.

---

## 🧪 Comparison to `ListView(...)`

| `ListView(...)`         | `ListView.builder(...)`                     |
|-------------------------|---------------------------------------------|
| Good for small static lists | Good for long or dynamic lists         |
| Builds all children at once | Builds on demand for better performance |
| Uses a list of widgets  | Uses an item builder function               |

---

## 🔁 Typical Pattern

```dart
final items = List.generate(100, (index) => 'Item $index');

ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return Text(items[index]);
  },
)
```

This will create a scrollable list of 100 items, but only build widgets as needed.

---


