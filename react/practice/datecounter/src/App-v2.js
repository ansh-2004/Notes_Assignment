import { useState } from 'react'
import './App.css'

export default function App2(){
    return (
        <div className='App'>
            <Counter />
        </div>
        
    )
}


function Counter(){

    const [step,setStep] = useState(1)
    const [count,setCount] = useState(0)

    const date = new Date()
    date.setDate(date.getDate() + count)

    function handleReset(){
        setCount(0)
        setStep(1)
    }

    return(
        <>
            <div>
                <input type='range' min={0} max={10} value={step} onChange={(e)=>setStep(Number(e.target.value))} ></input>
                <span> step :{step} </span>
            </div>

            <div>
                <button onClick={()=>setCount(()=>count - step)}> - </button>
                <input type='number' value={count} onChange={(e)=>setCount(Number(e.target.value))}></input>
                <button onClick={()=>setCount(()=>count + step)}> + </button>
            </div>

            <div>
                <p>
                    <span>
                    {
                        count === 0 
                        ? `Today is ` 
                        : count < 0 
                        ?  `${Math.abs(count)} days ago was ` 
                        : `${count} days from Today is `
                    }
                    </span>
            
                    <span>{date.toDateString()}</span>
            

                </p>
            </div>

            {
            count !==0 || step !== 1 
            ? <button onClick={handleReset}>Reset</button> 
            : null
            }
            
        </>
    )
}