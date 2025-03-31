/*
  File: us_cad_converter_oop.dart
  Author: Prof. Lehman
  Date: Spring 2025
  Description:
    A simple Flutter app that converts USD to CAD using a user-defined
    exchange rate. Demonstrates use of stateful widgets, custom classes,
    text input, and basic currency formatting.

  Chat GPT 4o with modifications from earlier Flutter apps and class exercises.
*/

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Currency Converter',
      home: const CurrencyConverterPage(),
    );
  }
}

class CurrencyConverterPage extends StatefulWidget {
  const CurrencyConverterPage({super.key});

  @override
  State<CurrencyConverterPage> createState() => _CurrencyConverterPageState();
}

class _CurrencyConverterPageState extends State<CurrencyConverterPage> {
  
  //*** class data ***
  final TextEditingController usdController = TextEditingController();
  final TextEditingController rateController = TextEditingController(text: "1.43");  
  
  String result = "";
  
  USCADCurrency converter = USCADCurrency(0.0, 0);  // *** currency converter instance
  
  
  void convertCurrency() {
    double? usd = double.tryParse(usdController.text);
    double? rate = double.tryParse(rateController.text);

    if (usd == null || rate == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("Please enter valid numbers for USD and Rate."),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    // set amount and rate from GUI
    converter.amount = usd;
    converter.rate = rate;
    
    // format as currency
    final formatter = NumberFormat.currency(locale: 'en_US', symbol: '\$');
    String formattedCAD = formatter.format(converter.convertToCAD());

    
    setState(() {
      
      //result = "Converted to CAD: $formattedCAD\n"
      //    "Rate: ${rate.toStringAsFixed(2)}\n"
      //    "Highest Rate Seen: ${USCADCurrency.highestRate.toStringAsFixed(2)}";
      result = converter.toString();
      
    });
  }

  void clearFields() {
    usdController.clear();
    rateController.clear();
    
    rateController.text = "1.43";
    
    setState(() {
      result = "";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("US to CAD Converter")),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Enter USD and Exchange Rate:", style: TextStyle(fontSize: 20)),
            const SizedBox(height: 10),
            TextField(
              controller: usdController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: "USD Amount",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: rateController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: "Exchange Rate",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(onPressed: convertCurrency, child: const Text("Convert")),
                ElevatedButton(onPressed: clearFields, child: const Text("Clear")),
              ],
            ),
            const SizedBox(height: 20),
            Text(
              result,
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}

class USCADCurrency {
  static double highestRate = -1;
  double _amount = 0;
  double _rate = 0;

  USCADCurrency(double newAmount, double newRate) {
    amount = newAmount;
    rate = newRate;
  }

  double get amount => _amount;

  set amount(double newAmount) {
    if (newAmount >= 0.0) {
      _amount = newAmount;
    }
  }

  double get rate => _rate;

  set rate(double newRate) {
    if (newRate >= 0.0) {
      _rate = newRate;
      if (_rate > USCADCurrency.highestRate) {
        USCADCurrency.highestRate = _rate;
      }
    }
  }

  double convertToCAD() {
    return _amount * _rate;
  }

  double highest() {
    return USCADCurrency.highestRate;
  }

  @override
  String toString() {
    return 'US: \$${_amount.toStringAsFixed(2)}\n'
           'CAN \$: ${convertToCAD().toStringAsFixed(2)}\n'
           'US to CAD rate ${_rate.toStringAsFixed(2)}\n'
           'Highest Rate Seen ${USCADCurrency.highestRate.toStringAsFixed(2)}';
  }
}
