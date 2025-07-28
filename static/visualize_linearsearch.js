console.log("JS loaded");

function animateSteps(target) {
    const boxes = document.querySelectorAll('.array-box');
    let index = 0

    function highlightNext(){
        if (index >= boxes.length) return;

        const box = boxes[index];
        const value = parseInt(box.textContent);

        box.classList.add('active');

        setTimeout(() => {
            if (value === target) {
                box.classList.remove('active');
                box.classList.add('found');
            } else {
                box.classList.remove('active');
                box.classList.add('failed');
                index++;
                highlightNext();
            }
        }, 1500);
    }

    highlightNext();
}