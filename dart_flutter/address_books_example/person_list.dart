import 'person.dart';

class PersonList {
  final List<Person> _people = [];

  List<Person> get people => _people;

  int get length => _people.length;

  Person getPersonAt(int index) => _people[index];

  void addPerson(Person person) {
    _people.add(person);
  }

  void removePersonAt(int index) {
    _people.removeAt(index);
  }

  void updatePersonAt(int index, Person updatedPerson) {
    _people[index] = updatedPerson;
  }

  void printAll() {
    if (_people.isEmpty) {
      print('Person list is empty.');
    } else {
      for (var person in _people) {
        print(person.toString());
      }
    }
  }

  @override
  String toString() {
    if (_people.isEmpty) {
      return 'PersonList: [empty]';
    } else {
      return _people.map((person) => person.toString()).join('\n');
    }
  }
}
