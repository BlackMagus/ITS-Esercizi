import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Saluto from './Saluto.jsx'
import CardUtente from './CardUtente.jsx'
import MenuRistorante from './MenuRistorante.jsx'
import Termostato from './Termostato.jsx'
import CampoRicerca from './CampoRicerca.jsx'
import MessaggioSegreto from './MessaggioSegreto'
import ModuloContatti from './ModuloContatti'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  // Esercizio 9
  return (
    <div>
      <ModuloContatti />
    </div>
  );

  // Esercizio 6
  return (
    <div>
      <MessaggioSegreto />
    </div>
  );

  // Esercizio 5
  return (
    <div>
      <CampoRicerca />
    </div>
  );

  // Esercizio 4
  return (
    <div>
      <Termostato />
    </div>
  );

  // Esercizio 3
  return (
    <div>
          <h1> Benvenuto al Ristorante!</h1>
            <MenuRistorante /> 
    
    </div>
    );

  // Esercizio 2
  return (
      <div>
        <Saluto />
          
            <CardUtente
            nome="Mario"
            email="mario.rossi@gmail.com"
            imgUrl="https://BlahBlah.so/220x"
            />

            <CardUtente
            nome="Maria"
            email="maria.rosa@gmail.com"
            imgUrl="https://BlahBlah.so/200x"
            />

            <CardUtente
            nome="Mariano"
            email="mariano.rossi@gmail.com"
            imgUrl="https://BlahBlah.so/270x"
            />
  
        </div>
    );

  // Esercizio 1
  return (
      <div>
        <Saluto />
      </div>
  )

  // Esercizio 0
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
