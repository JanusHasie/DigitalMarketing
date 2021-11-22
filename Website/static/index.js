function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId }),
    }).then((_res) => {
        window.location.href ="/";
    });
}

function deleteImg(imgId) {
    fetch("/delete-img", {
        method: "POST",
        body: JSON.stringify({imgId: imgId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}