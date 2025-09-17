import React, { useState } from "react";

function CampoRicerca() {
  
  const [testoRicerca, setTestoRicerca] = useState("");

  return (
    <div style={{ textAlign: "center", marginTop: "30px" }}>
      
      <input
        type="text"
        value={testoRicerca}
        onChange={(e) => setTestoRicerca(e.target.value)} 
        style={{ padding: "5px", fontSize: "16px" }}
      />

      
      <p>Stai cercando: {testoRicerca}</p>
    </div>
  );
}

export default CampoRicerca;
