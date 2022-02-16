# django_quiz_site
Create different quizzes in admin panel and let other users solve them.

Creating quizzes:
  -  create tests, questions and answers, easily edit them separately
  -  you can set difficulty and category for each test
  -  questions may have different numbers of answers and multiple correct answers are possible
  -  super user can see each person's results, filter and sort them

Solving quizzes:
  -  you can see a panel with available test even before logging in
  -  each quizz pane includes its title, category, difficulty and number of questions
  -  when you want to solve a quizz, you must be logged in or you are redirected to login page
  -  when you solve at least one test, in your profile tab you can see whole history starting from the newest

Application uses standard django authentication and sqlite3 local database.
