# QuizReactFlask
Quiz application using React &amp; Flask

15 Question quiz with answer feedback and results.

-------

Start Backend = `flask run`
- port 5000
- /api/random_question/
  - Serves a random question in JSON
    - question: string
    - correctId: int
    - answers: string[]

Start Frontend = `npm start`
- port 3000
- Site is served from root route
