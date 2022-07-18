f = open('PRUEBA/HomeBanking/cheques.html', 'w')

html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
<header>
        <img class="logo" src="imagenes/itbanksinfondo.png">
        <img class="barra" src="imagenes/multicolor.png">
        <nav class="navbar navbar-expand-lg bg-light">
            <div class="container-fluid">
              <a class="navbar-brand" href="#"></a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <p>MENU</p>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="../index.html">Inicio</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="IniSes.html">Iniciar Sesion</a>
                  </li>
                  <li class="nav-item">
                        <a class="nav-link" href="comprardolar.html">Comprar Dolares</a>
                        </li>
                    <li class="nav-item">
                            <a class="nav-link" href="calcularAmigos.html">Calcular Gastos</a>
                            </li>
                    <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Consultas
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                      <li><a class="dropdown-item" href="cuentas.html">Cuentas</a></li>
                      <li><a class="dropdown-item" href="tarjetas.html">Tarjetas</a></li>
                      <li><a class="dropdown-item" href="prestamos.html">Préstamos</a></li>
                    </ul>
                  </li>
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Transacciones
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                      <li><a class="dropdown-item" href="transferencias.html">Transferencias</a></li>
                      <li><a class="dropdown-item" href="pagoserv.html">Pago de servicios e impuestos</a></li>
                      <li><a class="dropdown-item" href="pagotarj.html">Pago de Tarjeta</a></li>
                    </ul>
                  </li>
                </ul>
                <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Buscar</button>
                </form>
              </div>
            </div>
          </nav>
</header>
<main>
  <div class="container my-5 text-center">
    <input type="text" id="dni" placeholder="Ingresar DNI" required="">
    <input class="btn btn-primary" id="agregarMonto" type="submit" value="Chequear" onclick="traer()"></input>
    <div class="mt-5">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Nombre</th>
          <th scope="col">Apellido</th>
          <th scope="col">Estado</th>
          <th scope="col">Tipo</th>
          <th scope="col">Monto</th>
          <th scope="col">Cupo Diario Restante</th>
          <th scope="col">Saldo en la Cuenta</th>
          <th scope="col">Fecha</th>
        </tr>
      </thead>
      <tbody id="contenido">
        
      </tbody>
    </table>
    </div>
  </div>
</main>
<script>
var contenido = document.querySelector('#contenido')
const documento = document.getElementById('dni');

function traer(){
  fetch('ejemplos_json/black.json')
    .then(res => res.json())
    .then(datos => {
      if(documento.value == datos.dni){
      tabla(datos)
      }
    })
  fetch('ejemplos_json/classic.json')
    .then(res => res.json())
    .then(datos => {
      if(documento.value == datos.dni){
      tabla(datos)
      }
    })
  fetch('ejemplos_json/gold.json')
    .then(res => res.json())
    .then(datos => {
      if(documento.value == datos.dni){
      tabla(datos)
      }
    })
}
function tabla(datos){
  contenido.innerHTML= ''
  console.log(datos.transacciones.length)
  for (var i=0;i<datos.transacciones.length;i++){
    console.log(datos.transacciones[i]);
    contenido.innerHTML += `
    <tr>
        <th scope="row">${datos.transacciones[i].numero}</th>
        <th>${datos.nombre}</th>
        <th>${datos.apellido}</th>
        <td>${datos.transacciones[i].estado}</td>
        <td>${datos.transacciones[i].tipo}</td>
        <td>${datos.transacciones[i].monto}</td>
        <td>${datos.transacciones[i].cupoDiarioRestante}</td>
        <td>${datos.transacciones[i].saldoEnCuenta}</td>
        <td>${datos.transacciones[i].fecha}</td>
    </tr>
    `
  }
}

</script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""

f.write(html_template)
f.close()