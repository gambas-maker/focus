function openModal(taskId) {
    const modal = document.getElementById(`modal${taskId}`);
    const card = document.getElementById(`card${taskId}`);
    card.style.display = 'none';
    modal.style.display = 'block';
}

function closeModal(taskId) {
    const modal = document.getElementById(`modal${taskId}`);
    const card = document.getElementById(`card${taskId}`);
    card.style.display = 'flex';
    modal.style.display = 'none';
}
