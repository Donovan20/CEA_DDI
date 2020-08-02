function obtener_datos(id, token, bandera) {
  var url = "pk=" + id + "&bandera=" + bandera;
  var ajax = new XMLHttpRequest();
  //Con la funcion open decimos que metodo se usara, y a donde vamos a mandar los datos desde el cliente
  ajax.open("POST", "/obtener/", true);
  //Esta funcion es necesaria para poder hacer la comunicacion por POST
  ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  ajax.setRequestHeader("X-CSRFToken", token);
  ajax.send(url);
  //En esta linea, se hace un callback cada ves que el estado con la conexion cambie
  ajax.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      if (this.response != "no") {
        var respuesta = JSON.parse(this.response);
        if (bandera == "e") {
          document.getElementById("numero").value = respuesta.numero;
          document.getElementById("fraccionamiento").value =
            respuesta.fraccionamiento;
          document.getElementById("pk").value = respuesta.pk;
        } else if (bandera == "d") {
          document.getElementById("desarrolladora").value = respuesta.nombre;
          document.getElementById("representante").value =
            respuesta.representante;
          document.getElementById("propietario").value = respuesta.propietario;
          document.getElementById("pk").value = respuesta.pk;
        } else if (bandera == "c") {
          document.getElementById("categoria").value = respuesta.nombre;
          document.getElementById("pk").value = respuesta.pk;
        } else if (bandera == "s") {
          console.log(respuesta);
        }
      }
    }
  };
}

function eliminar(id, token, bandera) {
  if (confirm("¿Realmente deseas eliminar el registro?")) {
    var url = "pk=" + id + "&bandera=" + bandera;
    var ajax = new XMLHttpRequest();
    //Con la funcion open decimos que metodo se usara, y a donde vamos a mandar los datos desde el cliente
    ajax.open("POST", "/borrar/", true);
    //Esta funcion es necesaria para poder hacer la comunicacion por POST
    ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    ajax.setRequestHeader("X-CSRFToken", token);
    ajax.send(url);
    //En esta linea, se hace un callback cada ves que el estado con la conexion cambie
    ajax.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        if (this.response != "no") {
          window.location.replace(this.response);
        }
      }
    };
  }
}
function doSearch() {
  const tableReg = document.getElementById("datos");
  const searchText = document.getElementById("searchTerm").value.toLowerCase();
  let total = 0;

  // Recorremos todas las filas con contenido de la tabla
  for (let i = 1; i < tableReg.rows.length; i++) {
    // Si el td tiene la clase "noSearch" no se busca en su cntenido
    if (tableReg.rows[i].classList.contains("noSearch")) {
      continue;
    }

    let found = false;
    const cellsOfRow = tableReg.rows[i].getElementsByTagName("td");
    // Recorremos todas las celdas
    for (let j = 0; j < cellsOfRow.length && !found; j++) {
      const compareWith = cellsOfRow[j].innerHTML.toLowerCase();
      // Buscamos el texto en el contenido de la celda
      if (searchText.length == 0 || compareWith.indexOf(searchText) > -1) {
        found = true;
        total++;
      }
    }
    if (found) {
      tableReg.rows[i].style.display = "";
    } else {
      // si no ha encontrado ninguna coincidencia, esconde la
      // fila de la tabla
      tableReg.rows[i].style.display = "none";
    }
  }
}
