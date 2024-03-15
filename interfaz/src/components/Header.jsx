import '../styles/header.css'
import {NavLink, Link} from 'react-router-dom'

export const Header = ()=>{
    
    return(
        <>
            <header>
                <section>
                <Link to={'/libros'}><img src="https://cdn-icons-png.flaticon.com/512/2232/2232688.png" alt="" /></Link>
                </section>
                <section>
                    <h1>Bienvenido a la Libreria</h1>
                </section>
                <section>
                    <ul>
                        <li><NavLink to={'/datos'}>Ver datos</NavLink></li>
                        <li><NavLink to={'/agregar_datos'}>Agregar datos</NavLink></li>
                    </ul>
                </section>
            </header>
        </>
    )
}