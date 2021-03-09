const prescriptionList = document.querySelector('#prescription-list');
const form = document.querySelector('#add-prescription-form');

// create element & render prescription
function renderPrescription(doc){
    let li = document.createElement('li');
    let name = document.createElement('span');
    let phone = document.createElement('span');
    let status = document.createElement('span');
    let code = document.createElement('span');
    let print = document.createElement('button');
    let cross = document.createElement('div');
    

    li.setAttribute('data-id', doc.id);
    name.textContent = doc.data().name;
    phone.textContent = doc.data().phone;
    status.textContent = doc.data().status;
    code.textContent = doc.id;

    cross.textContent = 'x';
    print.textContent = 'Print barcode';

    li.appendChild(name);
    li.appendChild(phone);
    li.appendChild(status);
    li.appendChild(code);
    li.appendChild(cross);
    li.appendChild(print);

    prescriptionList.appendChild(li);

    //deleting data
    cross.addEventListener('click', (e) =>{
        e.stopPropagation();
        let id = e.target.parentElement.getAttribute('data-id');
        db.collection('Prescriptions').doc(id).delete();
    })

    print.addEventListener('click', (e) =>{
        e.stopPropagation();
        let id = e.target.parentElement.getAttribute('data-id');
        db.collection('Prescriptions').doc(id).delete();
    }) 

}

// getting data
//db.collection('Prescriptions').orderBy('name').get().then(snapshot => {
  //  snapshot.docs.forEach(doc => {
       //THIS DON'T console.log(doc.data());
    //   renderPrescription(doc);
    //});
//});

//saving data
form.addEventListener('submit', (e) => {
    e.preventDefault();
    db.collection('Prescriptions').add({
        name: form.name.value,
        phone: form.phone.value,
        status: "new"
    });
    form.name.value = '';
    form.phone.value = '';
});

// real-time listener
db.collection('Prescriptions').orderBy('name').onSnapshot(snapshot => {
    let changes = snapshot.docChanges();
    changes.forEach(change => {
        if(change.type == 'added'){
            renderPrescription(change.doc);
        } else if (change.type == 'removed'){
            let li = prescriptionList.querySelector('[data-id=' +change.doc.id+ ']');
            prescriptionList.removeChild(li);
        } 
    })
})