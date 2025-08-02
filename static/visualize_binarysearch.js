console.log("Binary Search JS loaded");

function createArrayBoxes(array, step, stepIndex) {
    const arrayContainer = document.createElement('div');
    arrayContainer.classList.add("array-line");

    array.forEach((val, idx) => {
        const box = document.createElement('div');
        box.classList.add('array-box');
        box.textContent = val;

        box.id = `step-${stepIndex}-box-${idx}`;

        if (idx < step.L || idx > step.R) {
            box.classList.add("failed");
        } else if (idx === step.mid && step.action === "found") {
            box.classList.add("found");
        } else if (idx === step.mid) {
            box.classList.add("mid");
        }

        arrayContainer.appendChild(box);
    });

    return arrayContainer;
}

function createJoin(step, target) {
    const arrowDiv = document.createElement('div');
    arrowDiv.classList.add('join-container');

    const arrowText = document.createElement('span');
    arrowText.classList.add('join-text');

    if (step.action === "found") {
        arrowText.textContent = `✅ Found ${target} at index ${step.mid}`;
    } else {
        const comparison = target < step.value ? "<" : target > step.value ? ">" : "==";
        arrowText.textContent = `${target} ${comparison} ${step.value}`;
    }

    arrowDiv.appendChild(arrowText);
    return arrowDiv;
}


function animateStepsBinary(target, steps, array) {
    const container = document.querySelector('.binary-animation');
    container.innerHTML = "";

    steps.forEach((step, i) => {
        setTimeout(() => {
            const arrow = createJoin(step, target); 
            const arrayLine = createArrayBoxes(array, step, i);
            const stepContainer = document.createElement('div');
            stepContainer.classList.add('binary-step');

            stepContainer.appendChild(arrow);
            stepContainer.appendChild(arrayLine);
            container.appendChild(stepContainer);
        }, 1200 * i);
    });
}
