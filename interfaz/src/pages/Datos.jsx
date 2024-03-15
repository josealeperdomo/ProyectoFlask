import { useState, useEffect } from 'react'

export const Datos = ()=>{
    const MiComponente = () => {
        const [data, setData] = useState([]);
      
        useEffect(() => {
          const fetchData = async () => {
            try {
              const response = await fetch('http://127.0.0.1:7500/autores');
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
                <div key={item.id} className='autor'>
                <h3>ID: {item.id} | NOMBRE: {item.nombre}</h3>
                </div>
                </>
              ))}
            </>
          );
        };

        const MiComponenteUsuarios = () => {
          const [data, setData] = useState([]);
        
          useEffect(() => {
            const fetchData = async () => {
              try {
                const response = await fetch('http://127.0.0.1:7500/usuarios');
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
                  <div key={item.id} className='autor'>
                  <h3>ID: {item.id} | NOMBRE: {item.nombre}</h3>
                  </div>
                  </>
                ))}
              </>
            );
          };

          const MiComponenteGeneros = () => {
            const [data, setData] = useState([]);
          
            useEffect(() => {
              const fetchData = async () => {
                try {
                  const response = await fetch('http://127.0.0.1:7500/generos');
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
                    <div key={item.id} className='autor'>
                    <h3>ID: {item.id} | NOMBRE: {item.nombre}</h3>
                    </div>
                    </>
                  ))}
                </>
              );
            };

            const MiComponenteEditoriales = () => {
              const [data, setData] = useState([]);
            
              useEffect(() => {
                const fetchData = async () => {
                  try {
                    const response = await fetch('http://127.0.0.1:7500/editoriales');
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
                      <div key={item.id} className='autor'>
                      <h3>ID: {item.id} | NOMBRE: {item.nombre}</h3>
                      </div>
                      </>
                    ))}
                  </>
                );
              };

    return(
        <>
          <main>
            <section>
              <h1>Autores</h1>
              <MiComponente/>
            </section>
            <section>
              <h1>Usuarios</h1>
              <MiComponenteUsuarios/>
            </section>
            <section>
              <h1>Generos</h1>
              <MiComponenteGeneros/>
            </section>
            <section>
              <h1>Editoriales</h1>
              <MiComponenteEditoriales/>
            </section>
          </main>
            
        </>
    )
} 