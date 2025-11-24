import React, { useCallback, useState } from 'react'

const ProvaRouter = () => {
const[link,setLink]=useState("Home")
const handleRender=()=>{
    if(link==="Home"){
        return <Home></Home>
    }
    if(link==="About"){
        return <About></About>
    }
    if(link==="Profiles"){
        return <Profiles></Profiles>
    }
}

  return (
    <div>
        <nav className='navbar'>
            <button className="btn btn-link nav-link" onClick={()=>setLink("Home")}>Home</button>
            <button className="btn btn-link nav-link" onClick={()=>setLink("About")}>About</button>
            <button className="btn btn-link nav-link" onClick={()=>setLink("Profiles")}>Profiles</button>
        </nav>
        <div>
            {handleRender()}
        </div>
    </div>
  )
}

export default ProvaRouter;