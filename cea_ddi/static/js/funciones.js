function obtener_datos(id,token,bandera){
    
    var url = "pk="+id+"&bandera="+bandera;
    var ajax = new XMLHttpRequest();
    //Con la funcion open decimos que metodo se usara, y a donde vamos a mandar los datos desde el cliente
    ajax.open("POST", "/obtener/", true);
    //Esta funcion es necesaria para poder hacer la comunicacion por POST
    ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    ajax.setRequestHeader("X-CSRFToken", token );
    ajax.send(url);
    //En esta linea, se hace un callback cada ves que el estado con la conexion cambie
    ajax.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            if(this.response != "no"){
                var respuesta = JSON.parse(this.response)
                if (bandera == 'e'){
                    
                    document.getElementById("numero").value = respuesta.numero
                    document.getElementById('fraccionamiento').value = respuesta.fraccionamiento
                    document.getElementById('pk').value = respuesta.pk
                }
                else if(bandera == 'd'){
                    document.getElementById("desarrolladora").value = respuesta.nombre
                    document.getElementById('representante').value = respuesta.representante
                    document.getElementById('propietario').value = respuesta.propietario
                    document.getElementById('pk').value = respuesta.pk
                }
                else if(bandera == 'c'){
                    document.getElementById("categoria").value = respuesta.nombre
                    document.getElementById('pk').value = respuesta.pk
                }
                else if(bandera == 's'){
                    console.log(respuesta)
                }
            }
        }
    }
}

function eliminar(id,token,bandera)
{
	
	if (confirm("¿Realmente deseas eliminar el registro?")){		
		var url = "pk="+id+"&bandera="+bandera;
		var ajax = new XMLHttpRequest();
		//Con la funcion open decimos que metodo se usara, y a donde vamos a mandar los datos desde el cliente
		ajax.open("POST", "/borrar/", true);
		//Esta funcion es necesaria para poder hacer la comunicacion por POST
		ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		ajax.setRequestHeader("X-CSRFToken", token );
		ajax.send(url);
		//En esta linea, se hace un callback cada ves que el estado con la conexion cambie
		ajax.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200) {
				if(this.response != "no"){
					window.location.replace(this.response)
				}
			}
		}
	}
}