// tip.dart
//
// prof. lehman
// spring 2025 (28 March 2025)
// 
// in-class code using sample template for IPO app
// to create a tip calculator
//

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';  // needed to format result as currency

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
  final TextEditingController textControllerBill = TextEditingController();
  final TextEditingController textControllerTip = TextEditingController();
  
  String result = "";
  
  // methods for actions
void doSomething() {
  
  double? bill = double.tryParse(textControllerBill.text);
  double? tip = double.tryParse(textControllerTip.text);

  String errorMsg = "";
    
  if (bill == null)
  {
    errorMsg = "Error: invalid bill amount";
  }
  
  if (tip == null)
  {
    if (bill != null)
    {
      errorMsg = "Error: invalid tip amount";        
    }
    else
    {
      errorMsg += ", Error: invalid tip amount";
    }
  }
  
  if (errorMsg != "")
  {
    // Show a SnackBar if input is invalid
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text( errorMsg ),
        backgroundColor: Colors.redAccent,
        duration: Duration(seconds: 3),
      ),
    );
  }
  else
  {
    double total = bill! + bill! * tip! / 100.0;
    final formatter = NumberFormat.currency(locale: 'en_US', symbol: '\$');
    String formattedTotal = formatter.format(total);

    setState(() {
      result = "Total with Tip: $formattedTotal";
    });
  }
}
  
  void clearAll() {
    
    textControllerBill.clear();
    textControllerBill.text = "20.00";
    
        textControllerTip.clear();
    textControllerTip.text = "20";
    
    setState(() {
      result = "";
    });
    
  }
  
  
  // setup GUI widgets and link to methods here
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("CS 386 Tip Calculator - In-Class 3/28")),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Tip Calculator",
              style: TextStyle(fontSize: 24),
            ),
            TextField(
              controller: textControllerBill,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Enter Bill",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 15),
            TextField(
              controller: textControllerTip,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Enter Tip ie. 20 = 20%",
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
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
