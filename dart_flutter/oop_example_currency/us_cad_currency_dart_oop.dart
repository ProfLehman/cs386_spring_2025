// us_cad_currency_dart_oop.dart
// prof. lehman
// spring 2025
//
// Currency class demonstrates instance and shared variables in Dart

class USCADCurrency {
  // shared static variable between instances
  static double highestRate = -1;

  // private instance variables
  double _amount = 0;
  double _rate = 0;

  // constructor
  USCADCurrency(double newAmount, double newRate) {
    amount = newAmount;
    rate = newRate;
  }

  // getters and setters
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

  // convert method
  double convertToCAD() {
    return _amount * _rate;
  }

  // get highest rate
  double highest() {
    return USCADCurrency.highestRate;
  }

  // string output
  @override
  String toString() {
    return 'US: \$${_amount.toStringAsFixed(2)}\n'
        'CAN \$: ${convertToCAD().toStringAsFixed(2)}\n'
        'US to CAD rate ${_rate.toStringAsFixed(2)}\n'
        'Highest Rate Seen ${USCADCurrency.highestRate.toStringAsFixed(2)}';
  }
}

void main() {
  var friday = USCADCurrency(100.00, 1.45);
  print(friday);
  print('');

  var saturday = USCADCurrency(100.00, 4.45);
  print(saturday);
  print('');

  friday.rate = 1.32;
  print(friday);
  print('');

  friday.amount = 23.45;
  print(friday);
  print('');
}


