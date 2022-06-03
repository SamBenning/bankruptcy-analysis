function createForm(data) {
    const formContainer = document.getElementById("formContainer")
    const form = document.createElement("form")
    form.method = "POST"



    // const testElement = document.createElement("p")
    // testElement.innerHTML = "This is a test"



    for(const prop in data) {
        
        let label = document.createElement('label')
        let input = document.createElement('input')
        let div = document.createElement('div')
        let buttonDiv = document.createElement('div')

        input.type = "number"
        input.step = "any"
        input.className = "form-control"
        input.id = prop
        input.name = data[prop]["column_name"]
        
        label.htmlFor = prop
        label.innerHTML = data[prop]["column_name"]

        buttonDiv.className = "btn-group"
        buttonDiv.role = "group"

        const fillWithMeanBtn = document.createElement("button")
        fillWithMeanBtn.innerHTML = "Fill With Mean Value"
        fillWithMeanBtn.className = "btn btn-secondary"
        fillWithMeanBtn.type = "button"
        

        div.className = "form-group"

        div.appendChild(label)
        div.appendChild(input)
        div.appendChild(buttonDiv)
        buttonDiv.appendChild(fillWithMeanBtn)

        form.appendChild(div)

        fillWithMeanBtn.addEventListener("click", (e) => {
            input.value = data[input.id]["column_mean"];
        })
    }

    const fillWithMeanBtn = document.createElement("button")
    fillWithMeanBtn.innerHTML = "Fill All With Mean Values"
    fillWithMeanBtn.className = "btn btn-primary"
    

    fillWithMeanBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if(field.value === '') {
                mean = data[field.id]["column_mean"]
                field.value = mean
            }
        }
    })

    const fillWithMeadianBtn = document.createElement("button")
    fillWithMeadianBtn.innerHTML = "Fill All With Median Values"
    fillWithMeadianBtn.className = "btn btn-primary"

    fillWithMeadianBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if(field.value === '') {
                median = data[field.id]["column_median"]
                field.value = median
            }
        }
    })

    const fillWithMinBtn = document.createElement("button")
    fillWithMinBtn.innerHTML = "Fill All With Min Values"
    fillWithMinBtn.className = "btn btn-primary"

    fillWithMinBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if (field.value === '') {
                min = data[field.id]["column_min"]
                field.value = min
            }
        }
    })

    const fillWithMaxBtn = document.createElement("button")
    fillWithMaxBtn.innerHTML = "Fill All With Max Values"
    fillWithMaxBtn.className = "btn btn-primary"

    fillWithMaxBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if (field.value === '') {
                max = data[field.id]["column_max"]
                field.value = max
            }
        }
    })

    const submitBtn = document.createElement("button")
    submitBtn.type = "submit"
    submitBtn.className = "btn btn-primary"
    submitBtn.innerHTML = "Make Prediction"
    form.appendChild(submitBtn)

    formContainer.appendChild(fillWithMeanBtn)
    formContainer.appendChild(fillWithMeadianBtn)
    formContainer.appendChild(fillWithMinBtn)
    formContainer.appendChild(fillWithMaxBtn)
    formContainer.appendChild(form)

}

