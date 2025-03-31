import 'package:flutter/material.dart';
import 'package:intl/intl.dart';


void main() {
  runApp(const MyApp());
}

/*
  File: us_cad_converter_oop_two_page.dart
  Author: Prof. Lehman
  Date: Spring 2025
  Description:
    Flutter app with swipe navigation to convert USD to CAD using an exchange
    rate set on a second screen. Demonstrates PageView, custom classes,
    shared state, and currency formatting.
*/

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Currency Converter',
      home: CurrencyConverterHome(),
    );
  }
}

class CurrencyConverterHome extends StatefulWidget {
  const CurrencyConverterHome({super.key});

  @override
  State<CurrencyConverterHome> createState() => _CurrencyConverterHomeState();
}

class _CurrencyConverterHomeState extends State<CurrencyConverterHome> {
  final PageController _pageController = PageController();
  final TextEditingController usdController = TextEditingController();
  final TextEditingController rateController = TextEditingController(text: "1.38");

  String result = "";
  double exchangeRate = 1.38;

  void convertCurrency() {
    double? usd = double.tryParse(usdController.text);

    if (usd == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("Please enter a valid USD amount."),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    var currency = USCADCurrency(usd, exchangeRate);
    final formatter = NumberFormat.currency(locale: 'en_US', symbol: '\$');
    String formattedCAD = formatter.format(currency.convertToCAD());

    setState(() {
      result = "Converted to CAD: $formattedCAD\n"
          "Rate: ${exchangeRate.toStringAsFixed(2)}\n"
          "Highest Rate Seen: ${USCADCurrency.highestRate.toStringAsFixed(2)}";
    });
  }

  void updateExchangeRate(String value) {
    double? newRate = double.tryParse(value);
    if (newRate != null && newRate > 0) {
      setState(() {
        exchangeRate = newRate;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return PageView(
      controller: _pageController,
      children: [
        // Page 1: Converter
        Scaffold(
          appBar: AppBar(title: const Text("US to CAD Converter")),
          body: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Enter USD to convert:", style: TextStyle(fontSize: 20)),
                const SizedBox(height: 10),
                TextField(
                  controller: usdController,
                  keyboardType: TextInputType.number,
                  decoration: const InputDecoration(
                    labelText: "USD Amount",
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 20),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton(onPressed: convertCurrency, child: const Text("Convert")),
                    ElevatedButton(
                      onPressed: () {
                        usdController.clear();
                        setState(() => result = "");
                      },
                      child: const Text("Clear"),
                    ),
                  ],
                ),
                const SizedBox(height: 20),
                Text(
                  result,
                  style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  textAlign: TextAlign.center,
                ),
                const Spacer(),
                const Text("Swipe left to set rate", style: TextStyle(color: Colors.grey)),
              ],
            ),
          ),
        ),

        // Page 2: Settings
        Scaffold(
          appBar: AppBar(title: const Text("Exchange Rate Settings")),
          body: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Set Exchange Rate (US to CAD):", style: TextStyle(fontSize: 20)),
                const SizedBox(height: 10),
                TextField(
                  controller: rateController,
                  keyboardType: TextInputType.number,
                  decoration: const InputDecoration(
                    labelText: "Exchange Rate",
                    border: OutlineInputBorder(),
                  ),
                  onChanged: updateExchangeRate,
                ),
                const SizedBox(height: 20),
                Text(
                  "Current Rate: ${exchangeRate.toStringAsFixed(2)}",
                  style: const TextStyle(fontSize: 18),
                ),
                const Spacer(),
                const Text("Swipe right to go back", style: TextStyle(color: Colors.grey)),
              ],
            ),
          ),
        ),
      ],
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
