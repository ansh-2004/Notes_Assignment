import { ChatOpenAI } from "@langchain/openai";  // now you don't take just openai from @langchain/openai , you take chatopenai , it is only basic difference from LLM model 
import { HumanMessage } from "@langchain/core/messages";
import dotenv from "dotenv";

dotenv.config();

const model = new ChatOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  modelName: "gpt-4",
});

const response = await model.invoke([
  new HumanMessage("Write a 5 line poem on cricket")
]);

console.log("OpenAI Response:", response.content);


