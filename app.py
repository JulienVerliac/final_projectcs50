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
    pass
def bubble_sort(arr, target):
    pass
def merge_sort(arr, target):
    pass
def call_stack(arr, target):
    pass

if __name__ == "__main__":
    app.run(debug=True)