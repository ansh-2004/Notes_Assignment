import dotenv from 'dotenv'
dotenv.config()


import { ChatGoogleGenerativeAI } from '@langchain/google-genai';


import path from "path";
import { fileURLToPath } from 'url';

// Get __dirname equivalent in ES6
const __filename = fileURLToPath(import.meta.url); // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\ChatModels\chatModel_google.js
const __dirname = path.dirname(__filename); // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\ChatModels
const customEnvPath = path.resolve(__dirname, "../.env") // C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\GenAI\LangChain\projects\01_project\.env

// dotenv.config({ path: customEnvPath })

console.log('api key', process.env.GOOGLE_API_KEY);

const model = new ChatGoogleGenerativeAI({
    model: 'gemini-2.5-pro',
    apiKey: process.env.GOOGLE_API_KEY,
});

async function main() {
    const response = await model.invoke('What is the capital of India');
    console.log("response is ", response);

    /*
      response is  AIMessage {
    "content": "The capital of India is **New Delhi**.\n",
    "additional_kwargs": {
      "finishReason": "STOP",
      "avgLogprobs": -0.0008689493872225285
    },
    "response_metadata": {
      "tokenUsage": {
        "promptTokens": 6,
        "completionTokens": 10,
        "totalTokens": 16
      },
      "finishReason": "STOP",
      "avgLogprobs": -0.0008689493872225285
    },
    "tool_calls": [],
    "invalid_tool_calls": [],
    "usage_metadata": {
      "input_tokens": 6,
      "output_tokens": 10,
      "total_tokens": 16
    }
  }
  
    */

    console.log("content is ", response.content);

    /*
    content is  The capital of India is **New Delhi**.
    */
}

main();
