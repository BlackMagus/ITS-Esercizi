import Saluto from './Saluto.jsx'
import CardUtente from './Vacanze/CardUtente.jsx'
import MenuRistorante from './MenuRistorante.jsx'
import Termostato from './Termostato.jsx'
import CampoRicerca from './Vacanze/CampoRicerca.jsx'
import MessaggioSegreto from './MessaggioSegreto'
import ModuloContatti from './ModuloContatti'
import './App.css'

function AppVacanze() {
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
}