const maxAttempts = 10;

function startGame() {
  fetch('/start', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      document.getElementById('game').style.display = 'block';
      document.getElementById('result').innerText = data.message;
      document.getElementById('attempts').innerText = "Attempts: 0";
      document.getElementById('guessInput').value = '';
      document.getElementById('guessInput').disabled = false;
      document.getElementById('progressBar').style.width = '0%';
      document.getElementById('startBtn').disabled = true;
      document.getElementById('restartBtn').style.display = 'none';
    });
}

function makeGuess() {
  const guess = document.getElementById('guessInput').value;
  fetch('/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ guess: guess })
  })
  .then(res => res.json())
  .then(data => {
    const resultEl = document.getElementById('result');
    resultEl.innerText = data.result;
    resultEl.className = "";

    if (data.result.includes("Too low")) {
      resultEl.classList.add("result-low");
    } else if (data.result.includes("Too high")) {
      resultEl.classList.add("result-high");
    } else if (data.result.includes("Correct")) {
      resultEl.classList.add("result-correct");
    } else if (data.result.includes("Game Over")) {
      resultEl.classList.add("result-error");
    }

    document.getElementById('attempts').innerText = "Attempts: " + data.attempts;
    updateProgress(data.attempts);

    if (data.game_over) {
      document.getElementById('restartBtn').style.display = 'block';
      document.getElementById('guessInput').disabled = true;
    }
  });
}

function restartGame() {
  fetch('/start', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      document.getElementById('result').innerText = data.message;
      document.getElementById('attempts').innerText = "Attempts: 0";
      document.getElementById('guessInput').value = '';
      document.getElementById('guessInput').disabled = false;
      document.getElementById('progressBar').style.width = '0%';
      document.getElementById('restartBtn').style.display = 'none';
    });
}

function updateProgress(attempts) {
  const progressPercent = (attempts / maxAttempts) * 100;
  document.getElementById('progressBar').style.width = progressPercent + '%';
}
