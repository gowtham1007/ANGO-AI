<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text to Image Generator</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        
        body {
            background: linear-gradient(135deg,);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        .container {
            margin-top: 50px;
        }
        
        .card {
            background-color: #fff;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        
        .card-title {
            color: #111213;
            font-weight: bold;
        }
        
        .form-control {
            border-color: #0e0f0f;
        }
        
        .btn-primary {
            background-color: #7e7f81;
            border-color: #0f0f10;
        }
        
        .btn-primary:hover {
            background-color: #919292;
            border-color: #101011;
        }
        
        .output img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
    </style>
</head>

<body>

    <div class="container">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Text to Image Generator</h5>
                        <textarea class="form-control" id="textInput" rows="5" placeholder="Enter text..."></textarea>
                        <button class="btn btn-primary mt-3" onclick="generateImage()">Generate Image</button>
                        <div class="output mt-3" id="imageOutput"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function generateImage() {
            var text = document.getElementById('textInput').value;
            var output = document.getElementById('imageOutput');
            output.innerHTML = '<img src="https://via.placeholder.com/400x200.png?text=' + encodeURIComponent(text) + '" alt="Generated Image">';
        }
    </script>

</body>

</html>
