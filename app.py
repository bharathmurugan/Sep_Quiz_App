from flask import Flask, render_template_string, request

app = Flask(__name__)


# Quiz questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "What is the capital of Karnataka?",
        "options": ["Mysore", "Bangalore", "Hubli", "Mangalore"],
        "answer": "Bangalore"
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["Pune", "Nagpur", "Mumbai", "Nashik"],
        "answer": "Mumbai"
    },
    {
        "question": "What is the capital of Tamil Nadu?",
        "options": ["Coimbatore", "Madurai", "Chennai", "Salem"],
        "answer": "Chennai"
    },
    {
        "question": "What is the capital of Rajasthan?",
        "options": ["Jodhpur", "Jaipur", "Udaipur", "Kota"],
        "answer": "Jaipur"
    },
    {
        "question": "What is the capital of West Bengal?",
        "options": ["Howrah", "Durgapur", "Kolkata", "Siliguri"],
        "answer": "Kolkata"
    },
    {
        "question": "What is the capital of Bihar?",
        "options": ["Gaya", "Patna", "Muzaffarpur", "Bhagalpur"],
        "answer": "Patna"
    }
]


@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>India Capitals Quiz</title>


    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }


        body {
            font-family: Arial, Helvetica, sans-serif;

            min-height: 100vh;

            background:
                linear-gradient(
                    135deg,
                    #667eea,
                    #764ba2
                );

            display: flex;

            justify-content: center;

            align-items: center;

            padding: 20px;
        }


        .quiz-container {

            width: 100%;

            max-width: 650px;

            background: white;

            border-radius: 20px;

            padding: 35px;

            box-shadow:
                0 20px 50px
                rgba(0, 0, 0, 0.25);
        }


        .header {

            text-align: center;

            margin-bottom: 25px;
        }


        .header h1 {

            color: #333;

            font-size: 32px;

            margin-bottom: 8px;
        }


        .header p {

            color: #777;

            font-size: 15px;
        }


        .score-box {

            display: flex;

            justify-content: space-between;

            align-items: center;

            background: #f5f6ff;

            padding: 15px 20px;

            border-radius: 12px;

            margin-bottom: 25px;
        }


        .score {

            color: #667eea;

            font-weight: bold;
        }


        .question-number {

            color: #555;

            font-weight: bold;
        }


        .progress-container {

            width: 100%;

            height: 8px;

            background: #e5e5e5;

            border-radius: 10px;

            margin-bottom: 30px;

            overflow: hidden;
        }


        .progress-bar {

            height: 100%;

            width: 14.28%;

            background:
                linear-gradient(
                    90deg,
                    #667eea,
                    #764ba2
                );

            border-radius: 10px;

            transition: width 0.4s ease;
        }


        .question {

            font-size: 24px;

            font-weight: bold;

            color: #222;

            line-height: 1.4;

            margin-bottom: 25px;
        }


        .options {

            display: grid;

            gap: 14px;
        }


        .option {

            width: 100%;

            padding: 16px 18px;

            border: 2px solid #e2e2e2;

            background: white;

            border-radius: 12px;

            font-size: 16px;

            text-align: left;

            cursor: pointer;

            transition: all 0.2s ease;
        }


        .option:hover {

            border-color: #667eea;

            background: #f5f6ff;

            transform: translateY(-2px);
        }


        .option.correct {

            background: #d4edda;

            border-color: #28a745;

            color: #155724;
        }


        .option.wrong {

            background: #f8d7da;

            border-color: #dc3545;

            color: #721c24;
        }


        .option:disabled {

            cursor: not-allowed;
        }


        .feedback {

            min-height: 30px;

            margin-top: 20px;

            font-size: 17px;

            font-weight: bold;

            text-align: center;
        }


        .correct-text {

            color: #28a745;
        }


        .wrong-text {

            color: #dc3545;
        }


        .next-btn,
        .restart-btn {

            width: 100%;

            border: none;

            padding: 15px;

            border-radius: 12px;

            font-size: 17px;

            font-weight: bold;

            cursor: pointer;

            margin-top: 20px;

            transition: 0.2s;
        }


        .next-btn {

            background: #667eea;

            color: white;
        }


        .next-btn:hover {

            background: #5568d9;
        }


        .next-btn:disabled {

            background: #ccc;

            cursor: not-allowed;
        }


        .restart-btn {

            background: #764ba2;

            color: white;
        }


        .restart-btn:hover {

            background: #653d8c;
        }


        .result {

            text-align: center;

            display: none;
        }


        .result-icon {

            font-size: 70px;

            margin-bottom: 15px;
        }


        .result h2 {

            font-size: 30px;

            color: #333;

            margin-bottom: 10px;
        }


        .result p {

            color: #666;

            font-size: 18px;

            margin-bottom: 10px;
        }


        .final-score {

            font-size: 45px;

            font-weight: bold;

            color: #667eea;

            margin: 15px 0;
        }


        @media (max-width: 600px) {

            .quiz-container {

                padding: 25px 20px;
            }


            .header h1 {

                font-size: 26px;
            }


            .question {

                font-size: 20px;
            }


            .option {

                font-size: 15px;
            }
        }

    </style>

</head>


<body>


<div class="quiz-container">


    <!-- QUIZ -->

    <div id="quiz">

        <div class="header">

            <h1>
                🇮🇳 India Capitals Quiz
            </h1>

            <p>
                Test your knowledge of Indian states and capitals
            </p>

        </div>


        <div class="score-box">

            <div class="question-number">

                Question

                <span id="currentQuestion">
                    1
                </span>

                /7

            </div>


            <div class="score">

                Score:

                <span id="score">
                    0
                </span>

            </div>

        </div>


        <div class="progress-container">

            <div
                class="progress-bar"
                id="progressBar">
            </div>

        </div>


        <div
            class="question"
            id="question">
        </div>


        <div
            class="options"
            id="options">
        </div>


        <div
            class="feedback"
            id="feedback">
        </div>


        <button
            class="next-btn"
            id="nextBtn"
            disabled
            onclick="nextQuestion()">

            Next Question →

        </button>

    </div>



    <!-- RESULT -->

    <div
        class="result"
        id="result">

        <div class="result-icon">
            🎉
        </div>


        <h2>
            Quiz Completed!
        </h2>


        <p>
            Your final score is:
        </p>


        <div class="final-score">

            <span id="finalScore">
                0
            </span>

            /7

        </div>


        <p id="resultMessage"></p>


        <button
            class="restart-btn"
            onclick="restartQuiz()">

            🔄 Restart Quiz

        </button>

    </div>


</div>



<script>


// Quiz data coming from Flask

const questions =
    {{ questions | tojson }};


let currentIndex = 0;

let score = 0;

let answered = false;



// HTML elements

const questionElement =
    document.getElementById("question");

const optionsElement =
    document.getElementById("options");

const feedbackElement =
    document.getElementById("feedback");

const nextButton =
    document.getElementById("nextBtn");

const scoreElement =
    document.getElementById("score");

const currentQuestionElement =
    document.getElementById("currentQuestion");

const progressBar =
    document.getElementById("progressBar");



// Load question

function loadQuestion() {

    answered = false;

    nextButton.disabled = true;

    feedbackElement.innerHTML = "";

    const currentQuestion =
        questions[currentIndex];


    questionElement.textContent =
        currentQuestion.question;


    currentQuestionElement.textContent =
        currentIndex + 1;


    scoreElement.textContent =
        score;


    // Progress

    const progress =
        ((currentIndex + 1) /
        questions.length) * 100;


    progressBar.style.width =
        progress + "%";


    // Remove old options

    optionsElement.innerHTML = "";


    // Create buttons

    currentQuestion.options.forEach(
        function(option) {

            const button =
                document.createElement("button");


            button.className =
                "option";


            button.textContent =
                option;


            button.onclick =
                function() {

                    checkAnswer(
                        button,
                        option
                    );

                };


            optionsElement.appendChild(
                button
            );

        }
    );
}



// Check answer

function checkAnswer(
    button,
    selectedAnswer
) {

    if (answered) {

        return;

    }


    answered = true;


    const correctAnswer =
        questions[currentIndex].answer;


    const allOptions =
        document.querySelectorAll(
            ".option"
        );


    // Disable options

    allOptions.forEach(
        function(option) {

            option.disabled = true;

        }
    );


    // Correct

    if (
        selectedAnswer.toLowerCase() ===
        correctAnswer.toLowerCase()
    ) {

        button.classList.add(
            "correct"
        );


        score++;


        scoreElement.textContent =
            score;


        feedbackElement.innerHTML =
            '<span class="correct-text">' +
            '✓ Correct Answer!' +
            '</span>';

    }


    // Wrong

    else {

        button.classList.add(
            "wrong"
        );


        allOptions.forEach(
            function(option) {

                if (
                    option.textContent
                    .toLowerCase() ===
                    correctAnswer
                    .toLowerCase()
                ) {

                    option.classList.add(
                        "correct"
                    );

                }

            }
        );


        feedbackElement.innerHTML =
            '<span class="wrong-text">' +
            '✗ Wrong Answer! Correct answer: ' +
            correctAnswer +
            '</span>';

    }


    nextButton.disabled = false;

}



// Next question

function nextQuestion() {

    currentIndex++;


    if (
        currentIndex <
        questions.length
    ) {

        loadQuestion();

    }

    else {

        showResult();

    }

}



// Show result

function showResult() {

    document.getElementById(
        "quiz"
    ).style.display = "none";


    document.getElementById(
        "result"
    ).style.display = "block";


    document.getElementById(
        "finalScore"
    ).textContent = score;


    let message = "";


    if (
        score === questions.length
    ) {

        message =
            "🏆 Perfect score! Excellent work!";

    }

    else if (score >= 5) {

        message =
            "👏 Great job! You know your capitals well.";

    }

    else if (score >= 3) {

        message =
            "👍 Good attempt! Keep practicing.";

    }

    else {

        message =
            "📚 Keep learning and try again!";

    }


    document.getElementById(
        "resultMessage"
    ).textContent = message;

}



// Restart

function restartQuiz() {

    currentIndex = 0;

    score = 0;


    document.getElementById(
        "quiz"
    ).style.display = "block";


    document.getElementById(
        "result"
    ).style.display = "none";


    loadQuestion();

}



// Start

loadQuestion();


</script>


</body>

</html>
    """, questions=questions)


if __name__ == "__main__":
    app.run(debug=True)