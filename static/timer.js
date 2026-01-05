let timeLeft = 600; // 10 minutes
const timerElement = document.getElementById("timer");

const countdown = setInterval(() => {
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;

    timerElement.innerHTML = `Time Left: ${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

    if (timeLeft <= 0) {
        clearInterval(countdown);
        document.getElementById("quizForm").submit();
    }

    timeLeft--;
}, 1000);

// -------- VALIDATION FUNCTION --------
function validateQuiz() {
    const questions = document.querySelectorAll(".question");
    let allAnswered = true;

    questions.forEach(q => {
        const checked = q.querySelector("input[type='radio']:checked");
        if (!checked) {
            allAnswered = false;
        }
    });

    const errorMsg = document.getElementById("errorMsg");

    if (!allAnswered) {
        errorMsg.innerText = "⚠️ Please answer all questions before submitting.";
        errorMsg.style.color = "red";
        errorMsg.style.textAlign = "center";
        errorMsg.style.marginTop = "15px";
        return false; // prevent submission
    }

    return true;
}
