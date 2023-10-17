window.addEventListener('DOMContentLoaded', function() {
    const timerElement = document.getElementById('timer');
    const startButton = document.getElementById('start-button');
    const stopButton = document.getElementById('stop-button');
    const videoElement = document.getElementById('animation-video');
    let countdown;
    let counter = 30;
  
    function startTimer() {
      resetTimer();
      timerElement.textContent = counter;
  
      countdown = setInterval(function() {
        counter--;
        timerElement.textContent = counter;
  
        if (counter <= 0) {
          clearInterval(countdown);
          stopVideo();
        }
      }, 1000);
    }
  
    function stopTimer() {
      clearInterval(countdown);
      stopVideo();
    }
  
    function playVideo() {
      videoElement.play();
    }
  
    function pauseVideo() {
      videoElement.pause();
    }
  
    function stopVideo() {
      pauseVideo();
      videoElement.currentTime = 0;
    }
  
    function resetTimer() {
      counter = 30;
      timerElement.textContent = counter;
    }
  
    startButton.addEventListener('click', function() {
      startTimer();
      playVideo();
    });
  
    stopButton.addEventListener('click', function() {
      stopTimer();
    });
  });
  
  
