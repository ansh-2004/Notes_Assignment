import { useState } from "react";


const initialItems = [
  { id: 1, description: "Passports", quantity: 2, packed: true },
  { id: 2, description: "Socks", quantity: 12, packed: false },
  { id: 3, description: "ticket", quantity: 2, packed: false },
];

export default function App() {
  return (
    <div className="app">
      <Logo/>
      <Form initialItems = {initialItems}/>
      <PackingList/>
      <Stats/>
    </div>
  );
}


function Logo(){
  return (
    <h1>
      🌴Far Away💼
    </h1>
  )
}


function Form({initialItems}){

  const [item,setItem] = useState("")
  const [quantity,setQuantity] = useState(1)

  function handleSubmit(e){
    e.preventDefault();
    initialItems.push(
      {
        id : initialItems.length + 1,
        description : item,
        quantity : quantity,
        packed : false
      }
    )

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


function PackingList(){

  function handleSubmit(){

    alert("Are you sure you want to delete all Items? ")

    console.log("before",JSON.stringify(initialItems))
    initialItems.splice(0,initialItems.length)
    console.log("after",JSON.stringify(initialItems))
  }



  return (
    <div className="list">
      <ul>
        {initialItems.map((item) => (
          <li key={item.id}>
            <input type="checkbox" ></input>
            <span style = {{textDecoration : item.packed ? "line-through" : "none"}}>{item.quantity} {item.description}</span>
            <button>❌</button>
          </li>
        ))}
      </ul>
      <div className="actions">
        <select>
              <option>Sort By Input Order</option>
              <option>Sort By Description</option>
              <option>Sort By Packed Status</option>
        </select>

        <button onClick={handleSubmit}> Clear List </button>
      </div>
    </div>
  )
}


function Stats(){

  const packedItems = initialItems.reduce((count,obj)=> (obj.packed === true ? count + 1 : count) ,0)

  const packedItemsPercentage = Math.round((packedItems / initialItems.length) * 100)
  

  return(
    <div className="stats">

      {
        initialItems.length === 0 
        ? (<p>Start adding some items to your packing list 🚀</p>)
        : packedItems !== initialItems.length 
        ? (<p>You have {initialItems.length} items on your list, and you already packed {packedItems} ({packedItemsPercentage}%) </p>)
        : (<p>You got everything! Ready to go ✈️</p>)
      }

      
    </div>
  )
}