export function Stats({initialItems}){

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