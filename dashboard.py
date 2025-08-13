from flask import Flask, render_template_string, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# HTML template with Plotly integration
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Diabetes Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h2>Upload Diabetes Data (JSON)</h2>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" id="fileInput" name="file" accept=".json">
        <button type="submit">Upload</button>
    </form>

    <div id="charts" style="margin-top:20px;">
        <div id="chart1" style="height:400px;"></div>
        <div id="chart2" style="height:400px;"></div>
        <div id="chart3" style="height:400px;"></div>
        <div id="chart4" style="height:400px;"></div>
        <div id="chart5" style="height:400px;"></div>
    </div>

<script>
document.getElementById("uploadForm").addEventListener("submit", function(e) {
    e.preventDefault();
    let file = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", file);

    fetch("/upload", { method: "POST", body: formData })
    .then(response => response.json())
    .then(data => {
        // Plot 1: Plasma glucose concentration vs Age
        Plotly.newPlot('chart1', [{
            x: data.age,
            y: data.glucose,
            mode: 'markers',
            type: 'scatter',
            marker: { size: 8, color: 'blue' }
        }], { title: 'Plasma Glucose vs Age' });

        // Plot 2: Body Mass Index Distribution
        Plotly.newPlot('chart2', [{
            x: data.bmi,
            type: 'histogram'
        }], { title: 'BMI Distribution' });

        // Plot 3: Blood Pressure vs Age
        Plotly.newPlot('chart3', [{
            x: data.age,
            y: data.bp,
            mode: 'lines+markers'
        }], { title: 'Blood Pressure vs Age' });

        // Plot 4: Diabetes Pedigree Function Distribution
        Plotly.newPlot('chart4', [{
            x: data.dpf,
            type: 'histogram'
        }], { title: 'Diabetes Pedigree Function' });

        // Plot 5: Class Variable Count
        Plotly.newPlot('chart5', [{
            x: data.class_labels,
            y: data.class_counts,
            type: 'bar'
        }], { title: 'Diabetes Cases vs Non-Cases' });
    });
});
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = json.load(file)

    df = pd.DataFrame(data)

    # Extract relevant columns
    glucose = df["Plasma glucose concentration"].tolist()
    age = df["Age (years)"].tolist()
    bmi = df["Body mass index"].tolist()
    bp = df["Diastolic blood pressure"].tolist()
    dpf = df["Diabetes pedigree function"].tolist()

    # Class variable counts
    class_counts = df["Class variable"].value_counts()
    class_labels = class_counts.index.tolist()
    class_values = class_counts.values.tolist()

    return jsonify({
        "glucose": glucose,
        "age": age,
        "bmi": bmi,
        "bp": bp,
        "dpf": dpf,
        "class_labels": class_labels,
        "class_counts": class_values
    })

if __name__ == "__main__":
    app.run(debug=True)
