
"""Plotly Dash HTML layout override."""

html_layout = """

<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
               <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbar"
        >
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbar">
            <div class="navbar-nav">
                <a class="nav-item nav-link" id="home" href="/">Home</a>
                <a class="nav-item nav-link" id="data-dash" href="/dashapp/">Data Dash</a>
                <a class="nav-item nav-link" id="predict" href="/enter-info">Predict</a>
                <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>
            </div>
        </div>
    </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>


        </body>
    </html>

"""