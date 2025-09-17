import React, { useState } from "react";

function MessaggioSegreto() {

  const [mostra, setMostra] = useState(false);

  return (
    <div style={{ textAlign: "center", marginTop: "30px" }}>
     <button onClick={() => setMostra(!mostra)}>
        {mostra ? "Nascondi messaggio" : "Mostra messaggio"}
      </button>

      {mostra && <p> Questo è il messaggio segreto</p>}
    </div>
  );
}

export default MessaggioSegreto;
