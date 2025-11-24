import React from 'react'
import {useparams} from 'react-router-dom'

const SingleProfile = () => {
    const params=useparams();
    console.log(params)
  return (
    <div>SingleProfile con id {params.id}</div>
  )
}

export default SingleProfile