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
    task_creation.style.display = 'none';
    add_task.style.display = 'flex';
}
