import React from 'react'
import ReactDOM from 'react-dom/client'

import './styles/index.css'
import { Header } from './components/Header.jsx'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Libros from './pages/libros.jsx'
import { Libro } from './pages/Libro.jsx'
import { AgregarDatos } from './pages/AgregarDatos.jsx'
import { Datos } from './pages/Datos.jsx'
import { Footer } from './components/Footer.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route path='/libros' element={<Libros/>} />
        <Route path='/libros/:id' element={<Libro/>} />
        <Route path='/agregar_datos' element={<AgregarDatos/>}/>
        <Route path='/datos' element={<Datos/>}/>
      </Routes> 
      <Footer/>
    </BrowserRouter>
  </React.StrictMode>,
)
