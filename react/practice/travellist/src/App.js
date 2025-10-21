

const initialItems = [
  { id: 1, description: "Passports", quantity: 2, packed: false },
  { id: 2, description: "Socks", quantity: 12, packed: false },
];

export default function App() {
  return (
    <div className="app">
      <Logo/>
      <Form/>
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

function Form(){
  return(
    <div>
     
     <form className="add-form">
        <h3>What do you need for your trip</h3>

        <select>
         {

          Array.from({ length: 20 }, (_, i) => i+1).map((ele)=>(<option>{ele}</option>))
         }
        </select>

        <input placeholder="item..."  ></input>
        <button> ADD </button>
     </form>
      
    </div>
  )
}
function PackingList(){}
function Stats(){}