console.log("JS loaded");

function animateSteps(target) {
    const boxes = document.querySelectorAll('.array-box');
    let index = 0

    const stepDuration = 1500; // Time for each step in milliseconds
    const blinkCycle = 0.8 * 1000; // 0.8s chosen in CSS file
    const blinkCount = 3;
    const blinkDuration = blinkCycle * blinkCount;

    // Start the animation with stepDuration as timing among each boxes
    function highlightNext(){
        if (index >= boxes.length) {
            setTimeout(() => {
                resetAnimation();
            }, stepDuration);
            return;
        }

        const box = boxes[index];
        const value = parseInt(box.textContent);

        box.classList.add('active');

        setTimeout(() => {
            box.classList.remove('active')

            if (value === target) {
                box.classList.add('found');
                
                setTimeout(() => {
                    resetAnimation();
                }, stepDuration);
            } else {
                box.classList.add('failed');
                index++;
                highlightNext();
            }
        }, stepDuration);
    }

    function resetAnimation(){
        boxes.forEach(box => {
            box.classList.remove('active', 'found', 'failed');
            box.classList.add('blink');
        });

        setTimeout(() => {
            boxes.forEach(box => box.classList.remove('blink'));
            index = 0;
            highlightNext();
        }, blinkDuration);
    }

    highlightNext();
}