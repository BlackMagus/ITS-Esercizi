import React, { useState } from "react";

function Termostato() {
  
  const [temperatura, setTemperatura] = useState(20);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
    
      <h1>Temperatura: {temperatura}°C</h1>

      <div style={{ marginTop: "20px" }}>
        <button onClick={() => setTemperatura(temperatura + 1)} style={{ marginRight: "10px" }}>
          +
        </button>
        <button onClick={() => setTemperatura(temperatura - 1)}>
          -
        </button>
      </div>
    </div>
  );
}

export default Termostato;
