let formData;

const handleFileInputChange = () => {
    $('#file_submit_input').change(function (e) {
        const file = this.files[0];
        formData = new FormData();
        formData.append('media', file);
        formData.append('text', "filename");
        console.log(formData)
        console.log(file)
    })
}

const handleFileBtn = () => {
    $('#file_submit_btn').click(function (e) {
        console.log("clicked")
        let url = "/files/upload"
        fetch(url, {
            method: 'POST',
            body: formData
        })
            .then(response => {
                console.log(response)
                return response.json()
            })
            .then(data => {
                swal("File added!", `Save this id: ${data.id}`, "success");
            })
    })
}

function main() {
    handleFileInputChange()
    handleFileBtn()
}

window.onload = main
