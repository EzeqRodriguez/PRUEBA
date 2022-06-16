function cargarDolar() {


    // fetch('datosdol.json')
    //     .then(cotizacion => cotizacion.json())
    //     //.then(cotizacion => console.log(cotizacion))


    //     .then(cotizaciones => {
    //         cotizaciones.forEach(cotiza => {
    //             console.log(cotiza);
    //         });

    //     })
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    // Exito
    .then(response => response.json())  // convertir a json
    .then(json => console.log(json))    //imprimir los datos en la consola
    .catch(err => console.log('Solicitud fallida', err)); // Capturar errores
    
}
cargarDolar();