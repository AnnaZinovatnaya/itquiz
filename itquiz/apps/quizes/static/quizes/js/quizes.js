function check_answer(correct_answer, user_answer) {
    retVal = "";

    if (correct_answer == 'True' && user_answer) {
        retVal = " | CORRECT";
    }
    else if (correct_answer == 'True' && !user_answer) {
        retVal = " | THIS IS A CORRECT ANSWER";
    }
    else if (correct_answer == 'False' && user_answer) {
        retVal = " | NOT CORRECT";
    }

    return retVal;
}

function check_quiz() {
    let questions = document.getElementsByClassName('question');

    for (i = 0; i < questions.length; i++) {
        let answers = questions[i].getElementsByClassName('answer');
        for (j = 0; j < answers.length; j++) {
            let answer_text_label = answers[j].getElementsByTagName('LABEL')[0];

            answer_text_label.innerHTML += check_answer(answers[j].getElementsByTagName('LABEL')[1].innerHTML,
                answers[j].getElementsByTagName("INPUT")[0].checked);

            document.getElementById('btn').value = 'IT Quiz';
            document.getElementById('quiz_form').onsubmit = function() {
                window.location.href = document.getElementById('home_button').href;
                return false;
            };

        }
    }
    return false;
}

document.getElementById('quiz_form').onsubmit = check_quiz;