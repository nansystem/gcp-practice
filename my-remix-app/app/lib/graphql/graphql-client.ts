import { GraphQLClient } from 'graphql-request';
import { getSdk } from './operations';

const client = new GraphQLClient('http://localhost:8000/api/graphql');
export const sdk = getSdk(client);
