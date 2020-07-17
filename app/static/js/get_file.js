let file_get_id;

const handleInputChange = () => {
    $('#file_get_input').change(function (e) {
        file_get_id = e.target.value
    })
}

const handleFileBtn = () => {
    $('#file_get_btn').click(function (e) {
        console.log("clicked")
        let url = `/files/download_redirect/${file_get_id}`
        window.open(url)
    })
}

function main() {
    handleFileBtn()
    handleInputChange()
}

window.onload = main
