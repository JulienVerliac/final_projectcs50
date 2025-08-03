console.log("Bubble Sort JS loaded");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function createArrayBoxes(arr) {
    const container = document.getElementById("array-container");
    container.innerHTML = "";

    const line = document.createElement("div");
    line.classList.add("array-line");

    arr.forEach((val, idx) => {
    const box = document.createElement("div");
        box.classList.add("array-box");
        box.textContent = val;
        box.dataset.index = idx;

        line.appendChild(box);
    });

    container.appendChild(line);
}

function getBoxByValue(val) {
    const boxes = document.querySelectorAll(".array-box");
    for (let box of boxes) {
        if (parseInt(box.textContent) === val) {
            return box;
        }
    }
}

async function visualizeBubbleSort(steps) {
    const container = document.querySelector(".array-line");

    for (let step of steps) {
        const iA = step.compared?.[0] ?? step.swapped_indices[0];
        const iB = step.compared?.[1] ?? step.swapped_indices[1];
        const valA = step.array[iA];
        const valB = step.array[iB];

        const boxA = getBoxByValue(valA);
        const boxB = getBoxByValue(valB);

        if (!boxA || !boxB) continue; // sécurité

        // Comparison
        if (step.step_type === "compare") {
            boxA.classList.add("active");
            boxB.classList.add("active");
            boxA.style.backgroundColor = "#FF6F61";
            boxB.style.backgroundColor = "#FF6F61";
            await sleep(1000);
        }

        // Swap
        if (step.step_type === "swap") {
            boxA.style.backgroundColor = "#4682B4";
            boxB.style.backgroundColor = "#4682B4";

            await sleep(1000);

            const parent = boxA.parentNode;
            const indexBoxA = Array.from(parent.children).indexOf(boxA);
            const indexBoxB = Array.from(parent.children).indexOf(boxB);

            if (indexBoxA > indexBoxB) {
                parent.insertBefore(boxA, boxB);
            } else {
                parent.insertBefore(boxB, boxA);
            }

            await sleep(1000);
        }

        // Reinitialize colors
        const newBoxA = getBoxByValue(valA);
        const newBoxB = getBoxByValue(valB);

        if (newBoxA) {
            newBoxA.style.backgroundColor = "#2c2f33";
            newBoxA.classList.remove("active");
        }
        if (newBoxB) {
            newBoxB.style.backgroundColor = "#2c2f33";
            newBoxB.classList.remove("active");
        }
    }

    // When its all sorted = green
    const allBoxes = container.querySelectorAll(".array-box");
    for (let box of allBoxes) {
        box.style.backgroundColor = "#10A37F";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (typeof originalArray !== "undefined") {
        createArrayBoxes(originalArray);
    }

    if (typeof steps !== "undefined") {
        visualizeBubbleSort(steps);
    }
});
