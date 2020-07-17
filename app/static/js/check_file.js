let file_check_id;

const show_file_data = (data) => {
    console.log("Showing file data")
    const container = document.getElementById("file-data-container")

    container.innerText = `File ${data.file_name} will expire in ${data.time_left.minutes} minutes`
        + ` and ${data.time_left.seconds} seconds`;
}

const handleInputChange = () => {
    $('#file_check_input').change(function (e) {
        file_check_id = e.target.value
    })
}

const handleFileBtn = () => {
    $('#file_check_btn').click(function (e) {
        let url = `/files/check_file/${file_check_id}`
        console.log(file_check_id)
        fetch(url, {
                method: 'GET',
            })
                .then(response => {
                    if (response.status === 404){
                        window.open("/error/404")
                    }
                    return response.json()
                })
                .then(data => {
                    show_file_data(data)
                })

    })
}

function main() {
    handleFileBtn()
    handleInputChange()
}

window.onload = main
