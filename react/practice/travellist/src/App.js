
// Ah, now I see exactly what you're asking — and it's a subtle but important distinction in how **React state** and **JavaScript references** behave.

// ---

// ### 🧩 The Key Difference

// Let’s compare the two scenarios:

// #### ✅ **When you define `initialItems` inside the `App` component:**

// ```jsx
// export default function App() {
//   const initialItems = [...]; // defined inside App
//   const [items, setItems] = useState(initialItems);
// }
// ```

// Here, `initialItems` is **re-created every time `App` re-renders**. So when you call `setItems(initialItems)`, you're passing a **fresh reference**, and React sees it as a change → it re-renders.

// ---

// #### ❌ **When you define `initialItems` globally (outside the component):**

// ```jsx
// let initialItems = [...]; // defined outside App

// export default function App() {
//   const [items, setItems] = useState(initialItems);
// }
// ```

// Now, `initialItems` is a **single global reference**. When you mutate it (e.g., `.push()`), you're modifying the same array in memory. Then when you call `setItems(initialItems)`, you're passing the **same reference** again — React sees no change → no re-render.

// ---

// ### 🧠 Why React Cares About References

// React uses **shallow comparison** to detect changes. If you pass the same object or array reference to `setState`, React assumes nothing changed — even if the contents did.

// ---

// ### ✅ Best Practice

// Always treat state as **immutable**. Instead of mutating arrays or objects, create new ones:

// ```js
// setItems((prevItems) => [...prevItems, newItem]); // triggers re-render
// ```

// And avoid relying on global mutable variables like `initialItems`.

// ---

// ### 🔍 TL;DR

// | Location of `initialItems` | Behavior |
// |----------------------------|----------|
// | Inside `App` component     | Fresh reference on each render → React re-renders ✅ |
// | Outside `App` (global)     | Same reference reused → React skips re-render ❌ |

// ---

// Would you like help refactoring your app to follow best practices throughout?


/* 
const initialItems = [
  { id: 1, description: "Passports", quantity: 2, packed: false },
  { id: 2, description: "Socks", quantity: 12, packed: false },
];
*/ // don't use this gloabl initialitems

import { Logo } from "./Components/Logo";
import { Form } from "./Components/Form";
import { PackingList } from "./Components/PackingList";
import { Stats } from "./Components/Stats";
import { useState } from "react";

export default function App() {

let initialItems = []

const [items,setItems] = useState(initialItems)



  function addItem(newItem){
    /*
    // initialItems.push(newItem)
    // setItems(initialItems)
    // console.log("updated Items in app.js",initialItems)

    don't do this because In React, immutability means not changing (mutating) the original data directly, but instead creating a new copy of the data with the changes you want.

React relies on reference comparison to detect changes. If you mutate the original state (like using .push() or .splice()), the reference stays the same — so React doesn’t know anything changed, and it won’t re-render your component.React’s rendering engine checks if the state has changed by comparing the old and new references. If they’re the same (as with mutation), it assumes nothing changed. If they’re different (as with immutable updates), it re-renders the component.

    */

    console.log("new item is",newItem)
    setItems(()=>([...items,newItem])) 
  }


  function updatePackedStatus(e,item){
   const restItems = items.filter((obj)=>(
    obj.id !== item.id
   ))

   console.log("rest items are ",restItems)

   console.log({
        id : item.id,
        description : item.description,
        quantity : item.quantity,
        packed : !item.packed 
      })

   
   setItems(()=>([...restItems,{
        id : item.id,
        description : item.description,
        quantity : item.quantity,
        packed : !item.packed
      }
    ]))
    
  }

  function handleClearList(){
    alert("Are you sure you want to delete all items ")
    setItems([])
  }


  function handleDeleteItems(item){
    const updatedItem = items.filter((obj)=>(obj.id !== item.id))
    console.log("After delete updated items",updatedItem)
    setItems(()=>updatedItem)
  }
  

  return (
    <div className="app">
      <Logo/>
      <Form initialItems = {items} addItem = {addItem}/>
      <PackingList initialItems = {items} updatePackedStatus = {updatePackedStatus} handleDeleteItems = {handleDeleteItems} handleClearList = {handleClearList}/>
      <Stats initialItems = {items}/>
    </div>
  );
}









