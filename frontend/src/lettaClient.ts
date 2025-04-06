import { LettaClient } from '@letta-ai/letta-client';

const client = new LettaClient({
  baseUrl: 'https://app.letta.com',
  token: 'MDgwNjQxY2YtMTI0NC00NDZmLThiM2YtMTVhNTIzOTJjMDhiOjhkNTg1ZTg1LTk1ODItNGRmYi1iZjY4LTBiOTRmZTAwYmVlNQ==', // Replace with your actual Letta API key
});

async function createAgentAndReturnId(name: string) {
    const response = await client.templates.createAgents('default-project', 'cruel-blush-turkey:latest', {
      agentName: "My Agent", // Replace 'name' with a valid property from TemplatesCreateAgentsRequest
    });
  
    // this template creates a single agent
    return response.agents[0].id;
  }

export default client;