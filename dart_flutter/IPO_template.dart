// IPO_template.dart
// sample template for IPO app
// with label, text, and button
//
// prof. lehman
// spring 2025
// 
// code modified by-hand from two Flutter Apps generated with ChatGPT 4o
//

import 'package:flutter/material.dart';

// starting point for all Dart/Flutter apps
void main() {
  runApp( MyApp() );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyAppClass(),
    );
  }
}

// create state instance that is mutable
class MyAppClass extends StatefulWidget {
  @override
  _MyAppClassState createState() => _MyAppClassState();
}

class _MyAppClassState extends State<MyAppClass> {
  
  // class data
  final TextEditingController textController = TextEditingController();
  String result = "";
  
  // methods for actions
  void doSomething() {
    
    // get text value
    // note: ? means int can store a null value  
    int? temp = int.tryParse(textController.text);
    
    if (temp == null) {
      setState(() {
        result = "Invalid input! Please enter a number.";
      });
    } else {
      setState(() {
        temp = temp! + 1; // ! ensures temp ios an int
        result = "Answer is $temp"; 
      });
    }
    
  }
  
  void clearAll() {
    
    textController.clear();
    textController.text = "0";
    
    setState(() {
      result = "";
    });
    
  }
  
  
  // setup GUI widgets and link to methods here
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("myApp Title")),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Enter something:",
              style: TextStyle(fontSize: 24),
            ),
            TextField(
              controller: textController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Enter Value",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 15),
            ElevatedButton(
              onPressed: doSomething,
              child: Text("Calculate"),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: clearAll,
              child: Text("Clear"),
            ),
            SizedBox(height: 20),
            Text(
              result,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
