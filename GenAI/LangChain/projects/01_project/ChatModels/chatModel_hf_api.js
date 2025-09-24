import 'dotenv/config';
import { HuggingFaceInference } from '@langchain/community/llms/hf';

console.log('api key', process.env.HUGGINGFACEHUB_API_KEY);

const model = new HuggingFaceInference({
  model: 'baidu/ERNIE-4.5-0.3B-PT', 
  apiKey: process.env.HUGGINGFACEHUB_API_KEY,  
  task: 'text-generation', 
  provider: 'novita',                  
});

async function main() {
  const res = await model.invoke('What is the capital of India');
  console.log(res); // This prints the full response object
}

main();
