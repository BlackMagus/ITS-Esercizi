const cambianome = ()=>{
    const [nome,setNome] = useStates ("Roberto");
    const cambia=()=>{
        /* if(nome=="Roberto"){
            setNome("Mario")
        }else{
            setNome("Roberto")
        }
    } */

        setNome(current=>{
            if (current==="Roberto")
                return "Mario"
            return "Roberto";
        })
    return (<div> 
        {nome}
        <div>
            <button class= "btn btn-dark" onClick={cambia}>Cambia</button>
        </div>
    </div>)
}
export default cambianome;