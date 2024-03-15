import { useState } from 'react'
import axios from 'axios'
import '../styles/agregarDatos.css'

export const AgregarDatos = ()=>{

    const [newautor,setNewautor] = useState({
        nombre:''
      })
    
      const crearAutor = async(e)=>{
        e.preventDefault()
        if (newautor.nombre !== '') {
          try{
            const response = await axios.post('http://127.0.0.1:7500/autores',newautor)
            console.log(response);
          }catch(error){
            console.log('error',error);
          }
        }else{
          alert('Agrega un valor')
        }
      }

      const [newuser,setNewuser] = useState({
        nombre:''
      })

      const crearUsuario = async(e)=>{
        e.preventDefault()
        if (newuser.nombre !== '') {
          try{
            const response = await axios.post('http://127.0.0.1:7500/usuarios',newuser)
            console.log(response);
          }catch(error){
            console.log('error',error);
          }
        }else{
          alert('agrega un valor')
        }
      }

      const [neweditorial,setNeweditorial] = useState({
        nombre:''
      })

      const crearEditorial = async(e)=>{
        e.preventDefault()
        if (neweditorial.nombre !== '') {
          try{
            const response = await axios.post('http://127.0.0.1:7500/editoriales',neweditorial)
            console.log(response);
          }catch(error){
            console.log('error',error);
          }
        }else{
          alert('agrega un valor')
        }
      }

      const [newgenero,setNewgenero] = useState({
        nombre:''
      })

      const crearGenero = async(e)=>{
        e.preventDefault()
          if (newgenero.nombre !== '') {
            try{
              const response = await axios.post('http://127.0.0.1:7500/generos',newgenero)
              console.log(response);
            }catch(error){
              console.log('error',error);
            }
          }else{
            alert('agrega un valor')
          }
      }

      const [newLibro,setNewLibro] = useState({
        titulo:"",
        ano_de_publicacion:"",
        autor_id:"",
        genero_id:"",
        editorial_id:"",
        imagen:""
      })
    
      const crearLibro = async(e)=>{
        e.preventDefault()
        if (newLibro.titulo !== '' && newLibro.ano_de_publicacion !== '' && newLibro.autor_id !== '' && newLibro.genero_id !== '' && newLibro.editorial_id !== '' && newLibro.imagen !== '') {
          try{
            const response = await axios.post('http://127.0.0.1:7500/libros',newLibro)
            console.log(response);
          }catch(error){
            console.log('error',error);
          }
        }else{
          alert('agrega todos los valores')
        }
      }

    return(
        <>
        <main>
            <section>
                <h3>Autor</h3>
                <form onSubmit={crearAutor} action="">
                    <input type="text" onChange={(e)=>setNewautor({...newautor, nombre: e.target.value})}/>
                    <input type="submit" value="Agregar autor"/>
                </form>
            </section>
            <section>
                <h3>Usuario</h3>
                <form onSubmit={crearUsuario} action="">
                    <input type="text" onChange={(e)=>setNewuser({...newuser, nombre: e.target.value})}/>
                    <input type="submit" value="Agregar Usuario" />
                </form>
            </section>
            <section>
                <h3>Editorial</h3>
                <form onSubmit={crearEditorial} action="">
                    <input type="text" onChange={(e)=>setNeweditorial({...neweditorial, nombre: e.target.value})}/>
                    <input type="submit" value="Agregar editorial" />
                </form>
            </section>
            <section>
                <h3>Genero</h3>
                <form onSubmit={crearGenero} action="">
                    <input type="text" onChange={(e)=>setNewgenero({...newgenero, nombre: e.target.value})}/>
                    <input type="submit" value="Agregar genero" />
                </form>
            </section>
            <section>
                <h3>Libro</h3>
                <form onSubmit={crearLibro} action="" className='addBook'>
                    <input type="text" placeholder='Ingresa el titulo' onChange={(e)=>setNewLibro({...newLibro, titulo: e.target.value})}/>
                    <input type="text" placeholder='Ingresa el ano' onChange={(e)=>setNewLibro({...newLibro, ano_de_publicacion: e.target.value})}/>
                    <input type="text" placeholder='Ingresa el id del autor' onChange={(e)=>setNewLibro({...newLibro, autor_id: e.target.value})}/>
                    <input type="text" placeholder='Ingresa el id de; genero' onChange={(e)=>setNewLibro({...newLibro, genero_id: e.target.value})}/>
                    <input type="text" placeholder='Ingresa el id de; editorial' onChange={(e)=>setNewLibro({...newLibro, editorial_id: e.target.value})}/>
                    <input type="text" placeholder='Ingresa el url de la portada' onChange={(e)=>setNewLibro({...newLibro, imagen: e.target.value})}/>
                    <input type="submit" value="Agregar libro" />
                </form>
            </section>
        </main>
        </>
    )
}