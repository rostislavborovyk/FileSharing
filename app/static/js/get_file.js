let id;

const handleInputChange = () => {
    $('#file_get_input').change(function (e) {
        id = e.target.value
    })
}

const handleFileBtn = () => {
    $('#file_get_btn').click(function (e) {
        console.log("clicked")
        let url = `/files/download_redirect/${id}`
        window.open(url)
    })
}

function main() {
    handleFileBtn()
    handleInputChange()
}

window.onload = main
