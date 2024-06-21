function executeAction(action) {
    let apName = document.getElementById('ap_name').value;
    let data = { action: action };

    if (action === 'show_cleartext') {
        data['ap_name'] = apName;
    }

    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

/**
 * function executeAction(aksi) {
    let namaAp = document.getElementById('ap_name').value;
    let data = { aksi: aksi };

    if (aksi === 'show_cleartext') {
        data['nama_ap'] = namaAp;
    }

    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.hasil;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

 */