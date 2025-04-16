class Person {
  String name;
  String phoneNumber;
  String email;

  Person({
    required this.name,
    required this.phoneNumber,
    required this.email,
  });

  @override
  String toString() {
    return 'Name: $name, Phone: $phoneNumber, Email: $email';
  }

  void printInfo() {
    print(toString());
  }

  factory Person.fromJson(Map<String, dynamic> json) {
  return Person(
    name: json['name'],
    phoneNumber: json['phoneNumber'],
    email: json['email'],
  );
}
}



