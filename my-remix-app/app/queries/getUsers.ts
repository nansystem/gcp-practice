import { graphqlClient } from "~/lib/graphql";

export const GET_USERS = `
  query {
    users {
      id
      name
      email
      createdAt
    }
  }
`;

export async function getUsers() {
  const response = await graphqlClient.request(GET_USERS);

  if (!response.data) {
    throw new Error("Failed to fetch users");
  }

  return response.data.users;
}
