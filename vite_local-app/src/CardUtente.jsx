import React from "react";
function CardUtente(props) {
    return (
        <div>
            <img src={props.imgUrl} alt="Avatar utente" />
            <h2>{props.nome}</h2>
            <p>{props.email}</p>
        </div>
    );
}

export default CardUtente;