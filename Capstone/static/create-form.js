function createForm(data) {
    const formContainer = document.getElementById("formContainer")
    const form = document.createElement("form")
    form.method = "POST"

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

        const fillWithMedianBtn = document.createElement("button")
        fillWithMedianBtn.innerHTML = "Fill With Median Value"
        fillWithMedianBtn.className = "btn btn-secondary"
        fillWithMedianBtn.type = "button"
        

        div.className = "form-group"

        div.appendChild(label)
        div.appendChild(input)
        div.appendChild(buttonDiv)
        buttonDiv.appendChild(fillWithMeanBtn)
        buttonDiv.appendChild(fillWithMedianBtn)

        form.appendChild(div)

        fillWithMeanBtn.addEventListener("click", (e) => {
            input.value = data[input.id]["column_mean"];
        })

        fillWithMedianBtn.addEventListener("click", (e) => {
            input.value = data[input.id]["column_median"]
        })
    }

    const overwriteDiv = document.createElement("div")
    overwriteDiv.class = "form-check"

    const overwriteExistingValues = document.createElement("input")
    overwriteExistingValues.type = "checkbox"
    overwriteExistingValues.id = "overwriteExisting"
    overwriteExistingValues.className = "form-check-input"

    const overwriteExistingValuesLabel = document.createElement("label")
    overwriteExistingValues.for = "overwriteExisting"
    overwriteExistingValuesLabel.innerHTML = "Over-write existing values"
    overwriteExistingValuesLabel.className = "form-check-label"

    overwriteDiv.appendChild(overwriteExistingValues)
    overwriteDiv.appendChild(overwriteExistingValuesLabel)

    overwriteDiv.style.padding = '30px'
    

    const fillWithMeanBtn = document.createElement("button")
    fillWithMeanBtn.innerHTML = "Fill All With Mean Values"
    fillWithMeanBtn.className = "btn btn-primary"
    

    fillWithMeanBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if(field.value === '' || document.getElementById("overwriteExisting").checked) {
                mean = data[field.id]["column_mean"]
                field.value = mean
            }
        }
    })

    const buttonDiv = document.createElement("div")
    buttonDiv.className = "btn-group"
    buttonDiv.role = "group"



    const fillWithMeadianBtn = document.createElement("button")
    fillWithMeadianBtn.innerHTML = "Fill All With Median Values"
    fillWithMeadianBtn.className = "btn btn-primary"

    fillWithMeadianBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if(field.value === '' || document.getElementById("overwriteExisting").checked) {
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
            if (field.value === '' || document.getElementById("overwriteExisting").checked) {
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
            if (field.value === '' || document.getElementById("overwriteExisting").checked) {
                max = data[field.id]["column_max"]
                field.value = max
            }
        }
    })

    const fillWithRandBtn = document.createElement("button")
    fillWithRandBtn.innerHTML = "Fill All With Random Values"
    fillWithRandBtn.className = "btn btn-primary"

    fillWithRandBtn.addEventListener("click", () => {
        const fields = document.querySelectorAll(".form-control")
        for(const field of fields) {
            if(field.value === '' || document.getElementById("overwriteExisting").checked) {
                max = data[field.id]["column_max"]
                min = data[field.id]["column_min"]
                field.value = Math.random() * (max - min) + min;
            }
        }
    })

    const submitBtn = document.createElement("button")
    submitBtn.type = "submit"
    submitBtn.className = "btn btn-primary"
    submitBtn.innerHTML = "Make Prediction"
    form.appendChild(submitBtn)

    buttonDiv.appendChild(fillWithMeanBtn)
    buttonDiv.appendChild(fillWithMeadianBtn)
    buttonDiv.appendChild(fillWithMaxBtn)
    buttonDiv.appendChild(fillWithMinBtn)
    buttonDiv.appendChild(fillWithRandBtn)
    formContainer.appendChild(buttonDiv)
    formContainer.appendChild(overwriteDiv)
    formContainer.appendChild(form)
}