import React from 'react'
import piatti from './Piatti'

function MenuRistorante() {
    return (
        <div>
            <h2> Menu del Ristorante</h2>
            <ul>
                {piatti.map((piatto) => (
                    <li key= {piatto.id}>
                        {piatto.nome} - €{piatto.prezzo}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default MenuRistorante;