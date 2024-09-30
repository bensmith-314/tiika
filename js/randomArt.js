function randomArtPiece() {
    const randomIndex = Math.floor(Math.random() * 1240); // Needs to be dynamically updated when generated
    if (randomIndex.toString().length === 3) {
        window.location.href = `0${randomIndex}.html`;
    } else if (randomIndex.toString().length === 2) { 
        window.location.href = `00${randomIndex}.html`;
    } else if (randomIndex.toString().length === 1) {
        window.location.href = `000${randomIndex}.html`;
    } else {
        window.location.href = `${randomIndex}.html`;
    }
}

// Attach event listener to the button
document.getElementById('randomArtPiece').addEventListener('click', randomArtPiece);