import { graphqlClient } from "~/lib/graphql-no-lib-client";

export const DELETE_USER = `
  mutation($id: Int!) {
    deleteUser(id: $id)
  }
`;

export async function deleteUser(id: number) {
  const response = await graphqlClient.request(DELETE_USER, { id });

  if (!response.data) {
    throw new Error("Failed to delete user");
  }

  return response.data.deleteUser;
}
