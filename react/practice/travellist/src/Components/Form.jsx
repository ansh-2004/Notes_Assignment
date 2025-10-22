import { useState } from "react";

export function Form({initialItems,addItem}){

  const [item,setItem] = useState("")
  const [quantity,setQuantity] = useState(1)

  function handleSubmit(e){
    e.preventDefault();
    const newItem = 
      {
        id : Date.now(),
        description : item,
        quantity : quantity,
        packed : false
      }
    

  
    addItem(newItem)

  }



  return(
    <div>
     
     <form className="add-form" onSubmit={(e)=>handleSubmit(e)}>
        <h3>What do you need for your 😍 trip?</h3>

        <select value={quantity} onChange={(e)=>(setQuantity(e.target.value))}>
         {
          
          Array.from({ length: 20 }, (_, i) => i+1).map((ele)=>(<option key={ele}>{ele} </option>))
         }
        </select>
        <input placeholder="item..." value={item} onChange={(e)=>(setItem(e.target.value))} ></input>
        <button> ADD </button>
     </form>
      
    </div>
  )
}