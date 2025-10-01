import React, { useState } from "react";

function ModuloContatti() {

  const [datiForm, setDatiForm] = useState({
    nome: "",
    email: "",
    messaggio: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setDatiForm({
      ...datiForm,
      [name]: value, 
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Dati inviati:", datiForm);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "30px" }}>
      <h2>Modulo di Contatto</h2>
      <form onSubmit={handleSubmit} style={{ display: "inline-block", textAlign: "left" }}>

        <div style={{ marginBottom: "10px" }}>
          <label>
            Nome:{" "}
            <input
              type="text"
              name="nome"
              value={datiForm.nome}
              onChange={handleChange}
            />
          </label>
        </div>

        <div style={{ marginBottom: "10px" }}>
          <label>
            Email:{" "}
            <input
              type="email"
              name="email"
              value={datiForm.email}
              onChange={handleChange}
            />
          </label>
        </div>

        <div style={{ marginBottom: "10px" }}>
          <label>
            Messaggio:{" "}
            <textarea
              name="messaggio"
              value={datiForm.messaggio}
              onChange={handleChange}
              rows="4"
              cols="30"
            />
          </label>
        </div>

        <button type="submit">Invia</button>
      </form>
    </div>
  );
}

export default ModuloContatti;
