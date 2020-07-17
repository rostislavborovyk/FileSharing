let formData;
let file_life_time;
let isFile = false;

const handleFileInputChange = () => {
    $('#file_submit_input').change(function (e) {
        const file = this.files[0];
        formData = new FormData();
        formData.append('media', file);
        isFile = true
    })
    $('#file_life_time').change(function (e) {
        file_life_time = e.target.value;
        formData.append('life_time', file_life_time);
    })

}

const handleFileBtn = () => {
    $('#file_submit_btn').click(function (e) {
        if(!isFile) {
            swal("Choose file!", "", "warning");
        } else if (file_life_time === "" || file_life_time === undefined) {
            swal("Set file lifetime!", "", "warning");
        } else {
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
        }
    })
}

function main() {
    handleFileInputChange()
    handleFileBtn()
}

window.onload = main
