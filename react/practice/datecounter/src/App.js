
import { useState } from 'react';
import './App.css';

export default function App() {
  return (
    <div className="App">
      <Counter />
    </div>
  );
}

function Counter() {

  const [step, setStep] = useState(1)
  const [count, setCount] = useState(0)

  function handleStepIncrement() {
    setStep(() => step + 1)
  }

  function handleStepDecrement() {
    setStep(() => step - 1)
  }

  function handleCountIncrement() {
    setCount(() => count + step)
  }

  function handleCountDecrement() {
    setCount(() => count - step)
  }


  const date = new Date()
  date.setDate(date.getDate() + count)

  return (
    <>

      <div>
        <button onClick={handleStepDecrement}> - </button>
        <span> Step:  {step} </span>
        <button onClick={handleStepIncrement}> + </button>
      </div>

      <div>
        <button onClick={handleCountDecrement}> - </button>
        <span> Count:  {count}</span>
        <button onClick={handleCountIncrement}> + </button>
      </div>

      <div>
       {
        count === 0 
        ? `Today is ${date.toDateString()}` 
        : count < 0 
        ?  `${Math.abs(count)} days ago was  ${date.toDateString()}` 
        : `${count} days from Today is ${date.toDateString()} `
       }
      </div>

    </>
  )
}