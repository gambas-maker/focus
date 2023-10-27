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

function openForm(){
    const task_creation =  document.querySelector('.task_creation');
    const add_task = document.querySelector('.add_task');
    task_creation.style.display = 'flex';
    add_task.style.display = 'none';
}

function closeForm(){
    const task_creation =  document.querySelector('.task_creation');
    const add_task = document.querySelector('.add_task');
    const add_note = document.querySelector('.note-control');
    const note_creation = document.querySelector('.note_creation');
    task_creation.style.display = 'none';
    add_task.style.display = 'flex';
    add_note.style.display = 'none';
    note_creation.style.display = 'flex';
}

function openNotes(){
    const note_creation = document.querySelector('.note_creation');
    const add_note = document.querySelector('.note-control');
    note_creation.style.display = 'none';
    add_note.style.display = 'flex';
}

function roundCounter(){
    const arrow_up = document.querySelector('.up');
    const arrow_down = document.querySelector('.down');
    const rounds = document.getElementById('id_rounds')

    arrow_up.addEventListener('click', function (e){
        e.preventDefault();
        console.log(rounds)
    });
}