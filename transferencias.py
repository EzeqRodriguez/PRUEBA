from tipos import Classic, Black, Gold


def menu1():

    menu1 = int(input("Bienvenido: \nIngrese 1, para ver todas sus transferencias\nIngrese 2, para ver sus transferencias APROBADAS\nIngrese 3, para ver sus transferencias RECHAZADOS\n"))
    if menu1 == 1 :
        menuT()
    elif menu1 == 2 :
        menuA()
    elif menu1 == 3:
        menuR()
               
def menuT():
    
    menuDNI = int(input("Ingrese su DNI: "))
    
    if menuDNI == 41:
        black()
    elif menuDNI == 42:
        gold()
    elif menuDNI == 43:
        classic()
    else:
        print("Su DNI no esta en nuestra base de datos")
        
def menuA():
    
    menu2 = int(input("Ingrese su DNI: "))
    
    if menu2 == 41:
        blackA()
        
    elif menu2 == 42:
        classicA()
    elif menu2 == 43:
        goldA()
    else:
        print("Su DNI no esta en nuestra base de datos")
        
def menuR():
    
    menu3 = int(input("Ingrese su DNI: "))
    
    if menu3 == 41:
        blackR()
        
    elif menu3 == 42:
        classicR()
    elif menu3 == 43:
        goldR()
    else:
        print("Su DNI no esta en nuestra base de datos")



def blackA():
    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "ACEPTADA":
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)
    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def black():

    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)
 
    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def blackR():
    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "RECHAZADA":
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)
 
    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

###################################################################################

def classicA():
    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteB = Black(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "ACEPTADA":

            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)
    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def classicR():
    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteB = Black(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "RECHAZADA":

            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)
    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def classic():

    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteC = Classic(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)


    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

###################################################################################

def gold():

    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)


    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def goldA():

    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "ACEPTADA" :
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)


    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()

def goldR():
    f = open('HomeBanking/cheques.html', 'w')

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
<table class="table">
  <thead>
    <tr>
      <th scope="col">Estado</th>
      <th scope="col">Tipo</th>
      <th scope="col">Monto</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
"""
    f.write(html_template)
    import json

    datos = open("HomeBanking/ejemplos_json/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "RECHAZADA" :
            
            valor_html = "<tr>"
            valor_html = valor_html +"<td>"+ transferencias['estado'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['tipo'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['monto'] +"</td>"
            f.write(valor_html)
            valor_html = "<td>"+ transferencias['fecha'] +"</td>"+"</tr>"
            f.write(valor_html)


    html_pie_template="""
  </tbody>
</table>
    </main>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>
"""
    f.write(html_pie_template)
    f.close()



menu1()