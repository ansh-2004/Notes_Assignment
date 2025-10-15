import { useState } from "react";
import "./App.css";


const questions = [
  {
    id: 3457,
    question: "What language is React based on?",
    answer: "JavaScript"
  },
  {
    id: 7336,
    question: "What are the building blocks of React apps?",
    answer: "Components"
  },
  {
    id: 8832,
    question: "What's the name of the syntax we use to describe a UI in React?",
    answer: "JSX"
  },
  {
    id: 1297,
    question: "How to pass data from parent to child components?",
    answer: "Props"
  },
  {
    id: 9103,
    question: "How to give components memory?",
    answer: "useState hook"
  },
  {
    id: 2002,
    question:
      "What do we call an input element that is completely synchronised with state?",
    answer: "Controlled element"
  }
];

export default function App() {
  return (
    <div className="App">
      <FlashCards />
    </div>
  );
}


function FlashCards() {


  const [selectedId,setSelectedId] = useState()
 

  function handleClick(obj){
    
    // console.log("obj id is ",obj.id)
    // console.log("selected id is",selectedId)

    if(selectedId === obj.id) {
      setSelectedId(null)
    }
    else {

      setSelectedId(obj.id)
    }
    
    //  we use this if else condition because we want  the selectedId to be set when a <div> is clicked, and cleared only when the user clicks again
    // so at first click , the selectedId and obj.id will not same as selectedId will be set only after when user click first Time , but if user clicks second time then selectedid and obj.id will be same so in that case, we need to again toggle the flashcard 
  }
  
  return (
    <div className="flashcards">
      {
        questions.map((obj)=>(

          <div 
          key={obj.id} 
          onClick={()=>handleClick(obj)} 
          className={obj.id === selectedId ? "selected" : ""}
          >

            {obj.id === selectedId ? obj.answer : obj.question}

          </div>

        ))
      }
      

    </div>
  )
}

