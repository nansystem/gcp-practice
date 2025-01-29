import { gql } from 'graphql-request';

export const GET_USERS = gql`
  query GetUsers {
    users {
      id
      name
      email
      createdAt
    }
  }
`;

export const GET_USER = gql`
  query GetUser($id: Int!) {
    user(id: $id) {
      id
      name
      email
      createdAt
    }
  }
`;
