document.addEventListener("DOMContentLoaded", function() {
    function changeTargetWord(newWord) {
        var targetWordSpan = document.getElementById("targetWord");
        if (targetWordSpan) {
            targetWordSpan.textContent = newWord;
        }
    }

    var words = ["children", "parents", "senior citizen"];
    var currentIndex = 0;

    function cycleWords() {
        changeTargetWord(words[currentIndex]);
        currentIndex = (currentIndex + 1) % words.length;
    }

    setInterval(cycleWords, 3000);
});
