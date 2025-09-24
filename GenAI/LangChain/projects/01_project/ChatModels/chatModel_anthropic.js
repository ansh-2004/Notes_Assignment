
import { ChatAnthropic } from '@langchain/anthropic';


const model = new ChatAnthropic({
  modelName: 'claude-3-5-sonnet-20241022',
  apiKey: process.env.ANTHROPIC_API_KEY,
});

async function main() {
  const response = await model.invoke('What is the capital of India');
  console.log(response.content);
}

main();
