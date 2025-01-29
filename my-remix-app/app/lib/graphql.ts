const GRAPHQL_ENDPOINT = "http://localhost:8000/api/graphql";

interface GraphQLResponse<T> {
  data?: T;
  errors?: Array<{ message: string }>;
}

interface GraphQLVariables {
  [key: string]: string | number | boolean | null;
}

export const graphqlClient = {
  async request<T>(
    query: string,
    variables?: GraphQLVariables
  ): Promise<GraphQLResponse<T>> {
    const response = await fetch(GRAPHQL_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, variables }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    return response.json();
  },
};
