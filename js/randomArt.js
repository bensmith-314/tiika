function randomArtPiece() {
    const randomIndex = Math.floor(Math.random() * 1782); // Needs to be dynamically updated when generated
    window.location.href = `${randomIndex}`;
}

// Attach event listener to the button
document.getElementById('randomArtPiece').addEventListener('click', randomArtPiece);