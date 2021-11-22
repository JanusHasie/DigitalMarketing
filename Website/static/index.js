function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId }),
    }).then((_res) => {
        window.location.href ="/";
    });
}

function deleteimg(imgId) {
    fetch("/delete-img", {
        method: "POST",
        body: JSON.stringify({imgId: imgId}),
    }).then((_res) => {
        window.location.href = "/viewmine";
    });
}

function download_file(pic) {
    fetch("/download", {
        method: "POST",
        body: JSON.stringify({pic: pic}),
    }).then((_res) => {
        window.location.href = "/viewmine"
    })
}