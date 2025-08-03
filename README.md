# Algorithm Visualizer

## Video Demo  
[Watch the demo](https://youtu.be/cv2L9kDIC3E)

## Description

This project is my final submission for the Harvard CS50x 2025 course. It is the result of several weeks of exploration, learning, coding, and experimentation around a central goal: making algorithms more understandable through visual interaction.

The **Algorithm Visualizer** is a web-based application that allows users to intuitively observe how three core algorithms behave step by step: **linear search, binary search, and bubble sort**. Rather than reading code or pseudocode, the user can watch the algorithms operate in real-time with animations, colors, and explanatory messages that clarify what is happening at each stage of the process.

My goal was not only to write working implementations of each algorithm but to build a user-friendly interface that helps demystify how they work under the hood. The application is designed to serve both students discovering computer science and curious learners who want to sharpen their algorithmic intuition.

---

## Technologies

- **Python (Flask)** – backend routing and server logic
- **HTML / CSS / JavaScript** – frontend and animations
- **VSCode (with WSL & GitHub Codespaces)** – development
- No external animation libraries: everything is custom-made

The frontend and backend communicate in a simple yet efficient way, and the visualization logic is entirely handled on the client side using JavaScript DOM manipulation, with custom animations created from scratch.

---

## Features

### Linear Search
- The user chooses a number to search for.
- An array of 8 integers within the range [1, 16] is generated.
- The algorithm checks each index sequentially.
- Highlighted in **grey** during search, **green** if found, **red** if not, and explains if not.
- A 50% chance that the number is not in the array emphasizes both success and failure cases.

### Binary Search
- Uses a sorted array of 15 numbers from [1, 30].
- The algorithm looks at the middle of the array, splitting it in half at each step.
- Discarded half is **red**, current search area is around the box in **blue**.
- The number is found faster, showcasing the power of binary search contrary to linear search.
- All steps are shown even if the number is not found.

### Bubble Sort
- Starts with a random unsorted array of 6 numbers between [1, 100].
- Adjacent elements are compared one pair at a time.
- Steps are in **pink**, swaps are shown with **blue** boxes.
- The array is fully sorted by the end, and final values are shown in **green**.

---

## Purpose

This project serves both as a **learning tool** and a **teaching aid**. The aim is to:
- Help beginners visualize abstract algorithmic logic.
- Reinforce understanding through repetition, animation, and color cues.
- Provide meaningful explanations even when searches fail or arrays are unsorted.

It emphasizes **clarity over speed**, focusing on slow and understandable animations over efficiency.

---

## Challenges

Building this project involved several learning curves:
- Writing animations in raw JavaScript without libraries
- Managing visual state while keeping the logic correct
- Handling user inputs cleanly across all scenarios
- Designing feedback for both success and failure cases

## Improvements
- Add more algorithms like insertion sort, merge sort, or Dijkstra’s algorithm
- Let users step through the algorithm manually (click "Next" to go to the next step)
- Add explanations in multiple languages
- Save user sessions and generate practice quizzes based on algorithm behavior
- Mobile responsiveness and improved visual design

## Insipiration and references
- The coding sloth : https://www.youtube.com/watch?v=jTJvyKZDFsY
- Build-your-own-x : https://github.com/codecrafters-io/build-your-own-x

