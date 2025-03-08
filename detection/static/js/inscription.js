
var modifyButton = document.createElement('button');
modifyButton.textContent = 'Modifier';
modifyButton.className = 'modify-button'; 

modifyButton.onclick = function() {
    modifyRow(newRow);
};
cellModify.appendChild(modifyButton); 

function modifyRow(row) {
    alert('Fonctionnalité de modification non implémentée.');
}

function modifyRow(row) {
    var cells = row.getElementsByTagName('td');
    
    for (var i = 0; i < cells.length - 2; i++) { 
        var cellValue = cells[i].textContent;
        cells[i].innerHTML = '<input type="text" value="' + cellValue + '">';
    }

    var saveButton = document.createElement('button');
    saveButton.textContent = 'Enregistrer';
    saveButton.className = 'save-button';
    saveButton.onclick = function() {
        saveChanges(row);
    };

    var modifyCell = cells[cells.length - 1];
    modifyCell.innerHTML = ''; 
    modifyCell.appendChild(saveButton);
}

function saveChanges(row) {
    var inputs = row.getElementsByTagName('input');

    for (var i = 0; i < inputs.length; i++) {
        var cell = inputs[i].parentNode;
        cell.textContent = inputs[i].value;
    }

    var modifyButton = document.createElement('button');
    modifyButton.textContent = 'Modifier';
    modifyButton.className = 'modify-button';
    modifyButton.onclick = function() {
        modifyRow(row);
    };

    var modifyCell = row.cells[row.cells.length - 1];
    modifyCell.innerHTML = ''; 
    modifyCell.appendChild(modifyButton);
}
