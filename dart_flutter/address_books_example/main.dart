import 'package:flutter/material.dart';
import 'person.dart';
import 'person_list.dart';
import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Person List App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const PersonListPage(),
    );
  }
}

class PersonListPage extends StatefulWidget {
  const PersonListPage({super.key});

  @override
  State<PersonListPage> createState() => _PersonListPageState();
}

class _PersonListPageState extends State<PersonListPage> {

  final PersonList personList = PersonList();

@override
void initState() {
  super.initState();
  loadPeopleFromJson();
}

Future<void> loadPeopleFromJson() async {
  final String response = await rootBundle.loadString('assets/people.json');
  final List<dynamic> data = jsonDecode(response);
  setState(() {
    for (var item in data) {
      personList.addPerson(Person.fromJson(item));
    }
  });
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Person List')),
      body: ListView.builder(
        itemCount: personList.length,
        itemBuilder: (context, index) {
          final p = personList.getPersonAt(index);
          return ListTile(
            title: Text(p.name),
            subtitle: Text(p.phoneNumber),
            trailing: const Icon(Icons.arrow_forward_ios),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => PersonDetailPage(person: p),
                ),
              );
            },
          );
        },
      ),
    );
  }
}

class PersonDetailPage extends StatelessWidget {
  final Person person;

  const PersonDetailPage({super.key, required this.person});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(person.name)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Name: ${person.name}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Phone: ${person.phoneNumber}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Email: ${person.email}', style: const TextStyle(fontSize: 18)),
          ],
        ),
      ),
    );
  }
}
