import { useState } from "react"

export function PackingList({initialItems,updatePackedStatus,handleDeleteItems,handleClearList}){



  return (
    <div className="list">
      <ul>
        {initialItems.map((item) => (
          <li key={item.id}>
            <input type="checkbox" checked = {item.packed} onChange={(e)=>updatePackedStatus(e,item)} ></input>
            <span style = {{textDecoration : item.packed ? "line-through" : "none"}}>{item.quantity} {item.description}</span>
            <button onClick={()=>handleDeleteItems(item)}>❌</button>
          </li>
        ))}
      </ul>
      <div className="actions">
        <select>
              <option>Sort By Input Order</option>
              <option>Sort By Description</option>
              <option>Sort By Packed Status</option>
        </select>

        <button onClick={()=>handleClearList()} > Clear List </button>
      </div>
    </div>
  )
}
