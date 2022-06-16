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

        .then(response => response.json())  

        .then(response => {

            response.forEach(response => {

                console.log(response);

            });

        })
    
}
cargarDolar();