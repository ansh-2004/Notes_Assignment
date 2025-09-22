import {ChatGoogleGenerativeAI} from '@langchain/google-genai'
import { HumanMessage } from "@langchain/core/messages";
import dotenv from 'dotenv'


import path from "path"; 
import { fileURLToPath } from 'url';

// Get __dirname equivalent in ES6
const __filename = fileURLToPath(import.meta.url); // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\LLMs\index.js
const __dirname = path.dirname(__filename); // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\LLMs


const customEnvPath = path.resolve(__dirname, "../.env") // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\.env

dotenv.config({ path: customEnvPath })


console.log('GOOGLE_API_KEY : ', process.env.GOOGLE_API_KEY);

const model = new ChatGoogleGenerativeAI({
    apiKey: process.env.GOOGLE_API_KEY,
    model: 'gemini-1.5-flash',

})

async function init(){
    try {
    // const respone = await model.invoke([
    // new HumanMessage(' who is india prime minister . ')

    const respone = await model.invoke('why modi is best prime minister of india ?')

    
    console.log('Gemini Response : ', respone.content)
        
    } catch (error) {
        console.log('Error while invoking the model: ', error);
        
    }
}
 
init()