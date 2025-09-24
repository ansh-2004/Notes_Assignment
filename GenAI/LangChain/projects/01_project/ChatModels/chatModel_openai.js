import { ChatOpenAI } from "@langchain/openai";  // now you don't take just openai from @langchain/openai , you take chatopenai , it is only basic difference from LLM model 
import { HumanMessage } from "@langchain/core/messages";
import dotenv from "dotenv";

dotenv.config();

const model = new ChatOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  model: "gpt-4",
  // temperature: 0.9,
  // maxTokens: 1000,
});

const response = await model.invoke([
  new HumanMessage("Write a 5 line poem on cricket")
]);

console.log("OpenAI Response:", response.content);


// temperature :   it is use to make the response more creative , if you want more creative response then you can set temperature to 0.9 or 1.0 , if you want more precise response then you can set temperature to 0.0 or 0.1
// maxTokens : it is use to limit the number of tokens in the response , if you want more detailed response then you can set maxTokens to 1000 or 2000 , if you want more concise response then you can set maxTokens to 100 or 200


