function cargarDolar() {


    fetch('datosdol.json')
        .then(cotizacion => cotizacion.json())
        //.then(cotizacion => console.log(cotizacion))


        .then(cotizaciones => {
            cotizaciones.forEach(cotiza => {
                console.log(cotiza);
            });

        })

}
cargarDolar();