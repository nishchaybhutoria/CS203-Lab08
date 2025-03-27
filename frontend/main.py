from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

BACKEND_URL = "http://34.47.223.158:9567"

@app.get('/', response_class=HTMLResponse)
def render():
        return f'''
<html>

<body>
    <textarea id="text" rows="10" cols="70"></textarea> <br> <br>
    <button onclick="get()">Get</button>
    <button onclick="insert()">Insert</button>
    <div id="output"></div>
    <script>
        const BACKEND_URL = "{BACKEND_URL}";
        function get() {{
            let query = document.getElementById("text").value;
            fetch(BACKEND_URL + "/search", {{
                method: "POST",
                headers: {{ "Content-Type": "application/json" }},
                body: JSON.stringify({{ "query": query }})
            }})
                .then(response => response.json())
                .then(data => document.getElementById("output").innerText = data.text);
            console.log(query);
        }}
        function insert() {{
            let text = document.getElementById("text").value;
            fetch(BACKEND_URL + "/insert", {{
                method: "POST",
                headers: {{ "Content-Type": "application/json" }},
                body: JSON.stringify({{ "text": text }})
            }}).then(response => response.json()).then(data => console.log(data));
        }}
    </script>
</body>

</html>
'''