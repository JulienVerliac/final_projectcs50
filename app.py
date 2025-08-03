from math import floor
from flask import Flask, render_template, request
import random

# Call Flask
app = Flask(__name__)

# Welcome route
@app.route("/")
def index():
    return render_template("index.html")

# ------
# Routes
# ------

@app.route("/linear-search", methods=["GET","POST"])
def vis_linear():
    print("Route hit!")
    if request.method == "GET":
        return render_template("visualize_linearsearch.html")
    
    if request.method == "POST":
        target = request.form.get("target")
        target = int(target)
        arr = random.sample(range(1, 16), 8)
        steps, step_count, was_found = linear_search(arr, target)
        print("Target:", target)
        print("Array:", arr)
        print("Steps:", steps)
        print("Step count:", step_count)
        print("Found:", was_found)
        return render_template("visualize_linearsearch.html", arr = arr, target = target, steps = steps, step_count = step_count, was_found = was_found)

@app.route("/binary-search", methods=["GET","POST"])
def vis_binary():
    print("Route hit!")
    if request.method == "GET":
        return render_template("visualize_binarysearch.html")
    
    if request.method == "POST":
        target = request.form.get("target")
        target = int(target)
        arr = sorted(random.sample(range(1, 30), 15))
        binary_steps = binary_search(arr, target)
        print("Target:", target)
        print("Array:", arr)
        print("steps:", binary_steps)
        step_count = len(binary_steps)
        was_found = any(step['found'] for step in binary_steps)
        return render_template("visualize_binarysearch.html", arr = arr, target = target, steps = binary_steps, step_count = step_count, was_found = was_found)   

@app.route("/bubble-sort", methods=["GET","POST"])
def vis_bubble():
    print("Route hit!")
    if request.method == "GET":
        return render_template("visualize_bubblesort.html")
    
    if request.method == "POST":
        n = 6
        array_to_sort = random.sample(range(1, 101), n)
        original_array = array_to_sort.copy()

        sort_steps = bubble_sort(array_to_sort)
        print("Original array:", original_array)
        print("Compared:", sort_steps)
        print("Array sorted:", array_to_sort)
        return render_template("visualize_bubblesort.html", original_array = original_array, sort_steps = sort_steps, array_to_sort = array_to_sort )

# -------------------------------------------------
# Algorithms we want to visualize and we may call #
# -------------------------------------------------

def linear_search(arr, target):
    steps = []
    was_found = False

    for i in range(len(arr)):
            steps.append({"index": i, "value": arr[i], "found": arr[i] == target})

            if arr[i] == target:
                was_found = True
                break

    step_count = len(steps)
    return steps,step_count, was_found

def binary_search(arr, target):
    steps = []
    L = 0 #L = left index
    R = len(arr) - 1 #R = right index

    while L <= R:
        mid = L + floor((R - L) / 2)

        if arr[mid] < target:
            action = "move right"
            step = {
                "L" : L,
                "R" : R,
                "mid" : mid,
                "val_L": arr[L],
                "val_R": arr[R],
                "value" : arr[mid],
                "target" : target,
                "found" : False,
                "action" :  action
            }
            L = mid + 1
            steps.append(step)

        elif arr[mid] > target:
            action = "move left"
            step = {
                "L" : L,
                "R" : R,
                "mid" : mid,
                "val_L": arr[L],
                "val_R": arr[R],
                "value" : arr[mid],
                "target" : target,
                "found" : False,
                "action" :  action
            }
            R = mid - 1
            steps.append(step)

        elif arr[mid] == target:
            action = "found"
            step = {
                "L" : L,
                "R" : R,
                "mid" : mid,
                "val_L": arr[L],
                "val_R": arr[R],
                "value" : arr[mid],
                "target" : target,
                "found" : True,
                "action" :  action
            }
            steps.append(step)
            break

    return steps

def bubble_sort(arr):
    steps = []
    n = len(arr)
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(n-1):
            steps.append({"compared": [i, i + 1], "array": arr.copy(), "step_type": "compare"})
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                steps.append({"swapped_indices": [i, i + 1], "array": arr.copy(), "step_type": "swap"})
        if not swapped:
            break  
        n = n - 1
    return steps

def merge_sort(arr):
    pass

if __name__ == "__main__":
    app.run(debug=True)