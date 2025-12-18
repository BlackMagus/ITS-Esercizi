import React, { useState, useEffect } from 'react';


const Esercizione1 = () => {
  const [attivaCard, setAttivaCard] = useState(null);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const cards = [
    { id: 1, titolo: "Card 1", testo: "Descrizione 1" },
    { id: 2, titolo: "Card 2", testo: "Descrizione 2" },
    { id: 3, titolo: "Card 3", testo: "Descrizione 3" },
  ];

  useEffect(() => {
    document.body.style.backgroundColor = isDarkMode ? "#222" : "#fff";
    document.body.style.color = isDarkMode ? "#fff" : "#000";
  }, [isDarkMode]);

  return (
    
    <div className='container mt-4'>
      <div className='row'>
        {cards.map((card) => (
          <div className='col-md-4' key={card.id}>
          
            <div 
              className='card mb-3' 
              style={{ cursor: "pointer" }}
              onClick={() => setAttivaCard(card.id)}
            >
              <div className='card-body'>
                <h5 
                  className='card-title' 
                  style={{ color: attivaCard === card.id ? "red" : "black" }}
                >
                  {card.titolo}
                </h5>
                <p 
                  className='card-text' 
                  style={{color: attivaCard === card.id ? "red" : "black" }}
                >
                  {card.testo}
                </p>
              </div>
            </div>
          </div>
        ))}
        <button 
        className={`btn ${isDarkMode ? 'btn-light' : 'btn-dark'}`}
        onClick={() => setIsDarkMode(!isDarkMode)}
      >
        Attiva {isDarkMode ? "Light" : "Dark"} Mode
      </button>
      </div>
    </div>
    
  );
};

export default Esercizione1;