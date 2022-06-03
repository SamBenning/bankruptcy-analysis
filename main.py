from Capstone import create_app
import jyserver.Flask as jsf

app = create_app()

@jsf.use(app)
class App():
    def create_form(self):
        print("Hello world")
        self.js.document.getElementById("me").innerHTML = "Hello"

if __name__ == "__main__":
    app.run(debug=True)