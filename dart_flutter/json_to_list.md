Here’s a complete Dart/Flutter app that reads a local `quiz.json` file from the app’s assets, shows each word in a list, and displays its meaning when tapped.

---

### 📁 File Structure
```
/lib
  main.dart
/assets
  quiz.json
/pubspec.yaml
```

---

### ✅ Step 1: `quiz.json` (Place in `/assets/`)
```json
{
  "words": [
    { "word": "ephemeral", "meaning": "lasting for a very short time" },
    { "word": "lucid", "meaning": "expressed clearly; easy to understand" },
    { "word": "benevolent", "meaning": "well meaning and kindly" },
    { "word": "ubiquitous", "meaning": "present, appearing, or found everywhere" },
    { "word": "arduous", "meaning": "involving or requiring strenuous effort; difficult and tiring" },
    { "word": "cogent", "meaning": "clear, logical, and convincing" },
    { "word": "placate", "meaning": "to make someone less angry or hostile" },
    { "word": "voracious", "meaning": "having a very eager approach to a particular activity" },
    { "word": "serendipity", "meaning": "the occurrence of events by chance in a happy or beneficial way" },
    { "word": "ameliorate", "meaning": "to make something bad or unsatisfactory better" }
  ]
}
```

---

### ✅ Step 2: `pubspec.yaml` (add these lines)
```yaml
flutter:
  assets:
    - assets/quiz.json
```

---

### ✅ Step 3: `main.dart`

```dart
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;

void main() {
  runApp(QuizApp());
}

class QuizApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Vocabulary Quiz',
      home: WordListScreen(),
    );
  }
}

class Word {
  final String word;
  final String meaning;

  Word({required this.word, required this.meaning});

  factory Word.fromJson(Map<String, dynamic> json) {
    return Word(
      word: json['word'],
      meaning: json['meaning'],
    );
  }
}

class WordListScreen extends StatefulWidget {
  @override
  _WordListScreenState createState() => _WordListScreenState();
}

class _WordListScreenState extends State<WordListScreen> {
  List<Word> _words = [];

  @override
  void initState() {
    super.initState();
    loadQuizData();
  }

  Future<void> loadQuizData() async {
    final String response = await rootBundle.loadString('assets/quiz.json');
    final data = json.decode(response);
    final List<Word> loadedWords =
        (data['words'] as List).map((e) => Word.fromJson(e)).toList();

    setState(() {
      _words = loadedWords;
    });
  }

  void showMeaning(BuildContext context, Word word) {
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text(word.word),
        content: Text(word.meaning),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: Text('OK'))
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Vocabulary Quiz')),
      body: ListView.builder(
        itemCount: _words.length,
        itemBuilder: (context, index) {
          final word = _words[index];
          return ListTile(
            title: Text(word.word),
            onTap: () => showMeaning(context, word),
          );
        },
      ),
    );
  }
}
```

---

### 🚀 To Run:
- Make sure `quiz.json` is in `/assets/`
- Run `flutter pub get`
- Launch the app

Let me know if you’d like to add features like quiz mode, multiple choice, or score tracking!
