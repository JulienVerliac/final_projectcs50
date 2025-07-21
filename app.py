from flask import Flask, render_template, request
import random

# Call Flask
app = Flask(__name__)

# Welcome route
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# ------
# Routes
# ------

@app.route("/linear-search", methods=["GET","POST"])
def vis_linear():
    if request.method == "GET":
        return render_template("visualize.html")
    if request.method == "POST":
        target = request.form.get("target")
        target = int(target)
        arr = random.sample(range(1, 20), 8)
        steps = linear_search(arr, target)
        print("Target:", target)
        print("Array:", arr)
        print("Steps:", steps)
        return render_template("visualize.html", arr = arr, target = target, steps = steps)


# -------------------------------------------------
# Algorithms we want to visualize and we may call #
# -------------------------------------------------

def linear_search(arr, target):
    steps = []
    for i in range(len(arr)):
        if(arr[i] == target):
            print("The element is found at position", (i+1))
            steps.append({"index": i, "value": arr[i], "found": arr[i] == target})
            return steps
    print("The element is not present in the array")
    return steps
    

def binary_search(arr, target):
    pass
def bubble_sort(arr, target):
    pass
def merge_sort(arr, target):
    pass
def call_stack(arr, target):
    pass
