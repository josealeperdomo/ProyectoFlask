import { Link } from 'react-router-dom';
import '../styles/App.css'
import React, { useEffect, useState } from 'react';

function Libros() {
  
  const MiComponente = () => {
    const [data, setData] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch('http://127.0.0.1:7500/libros');
          const jsonData = await response.json();
          setData(jsonData);
        } catch (error) {
          console.error(error);
        }
      };
  
      fetchData();
    }, []);
  
    return (
      <>
        {data.map((item) => (
          <>
          <div key={item.id} className='libro'>
          <h3>{item.titulo}</h3>
          <Link to={`/libros/${item.id}`}>  
            <img src={item.imagen} alt={`portada de ${item.titulo}`} />
          </Link>
          </div>
          </>
        ))}
      </>
    );
  };


  return (
    <>
      <main>
      <h1>Libros</h1>
        <section className='libros'>
        {MiComponente()}
        </section>
      </main>
    </>
  )
}

export default Libros
