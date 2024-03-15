import { useParams } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import '../styles/libro.css';

export const Libro = () => {
  const params = useParams()

  const MiComponente = () => {
    const [data, setData] = useState([])

    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch(`http://127.0.0.1:7500/rutadetallada/${params.id}`)
          const jsonData = await response.json()
          setData(jsonData)
        } catch (error) {
          console.error(error)
        }
      }

      fetchData()
    }, [])

    const uniqueResenas = [...new Set(data.map(item => item.resena))]
    const escritoresDeResena = [...new Set(data.map(item => item.escritor_de_resena))]

    return (
      <>
        {data.length > 0 ? (
          <div className='libro'>
            <h3>{data[0].titulo_del_libro}</h3>
            <h4>Autor: {data[0].autor}</h4>
            <img src={data[0].imagen} alt={`Portada de ${data[0].titulo_del_libro}`} />
            <h3>Reseñas</h3>
            {uniqueResenas[0] !== null ?             uniqueResenas.map((resena, index) => (
              <h6 key={index}>{escritoresDeResena[index]}: {resena}</h6>
            )) : <h6>No hay reseñas de este libro</h6>}
          </div>
        ) : (
          <h1>NO HAY DATOS DISPONIBLES</h1>
        )}
      </>
    );}

  return (
    <main>
      <MiComponente />
    </main>
  )
}