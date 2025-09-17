document.getElementById('quiz-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const topic = document.getElementById('topic').value;

    fetch('/generate_quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('quiz-output').innerText = data.quiz;
    });
});

document.getElementById('recommendation-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const student_id = document.getElementById('student_id').value;

    fetch('/get_recommendation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ student_id: student_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recommendation-output').innerText = data.recommendation;
    });
});