import { graphqlClient } from "~/lib/graphql";

export const CREATE_USER = `
  mutation($name: String!, $email: String!) {
    createUser(name: $name, email: $email) {
      id
      name
      email
      createdAt
    }
  }
`;

export async function createUser(name: string, email: string) {
  const { data } = await graphqlClient.request(CREATE_USER, { name, email });
  return data.createUser;
}
