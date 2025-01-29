import * as Types from './types';

import { GraphQLClient, RequestOptions } from 'graphql-request';
import gql from 'graphql-tag';
type GraphQLClientRequestHeaders = RequestOptions['requestHeaders'];
export type CreateUserMutationVariables = Types.Exact<{
  name: Types.Scalars['String']['input'];
  email: Types.Scalars['String']['input'];
}>;


export type CreateUserMutation = { __typename?: 'Mutation', createUser: { __typename?: 'User', id: number, name: string, email: string, createdAt: any } };

export type UpdateUserMutationVariables = Types.Exact<{
  id: Types.Scalars['Int']['input'];
  name: Types.Scalars['String']['input'];
  email: Types.Scalars['String']['input'];
}>;


export type UpdateUserMutation = { __typename?: 'Mutation', updateUser?: { __typename?: 'User', id: number, name: string, email: string, createdAt: any } | null };

export type DeleteUserMutationVariables = Types.Exact<{
  id: Types.Scalars['Int']['input'];
}>;


export type DeleteUserMutation = { __typename?: 'Mutation', deleteUser: boolean };

export type GetUsersQueryVariables = Types.Exact<{ [key: string]: never; }>;


export type GetUsersQuery = { __typename?: 'Query', users: Array<{ __typename?: 'User', id: number, name: string, email: string, createdAt: any }> };

export type GetUserQueryVariables = Types.Exact<{
  id: Types.Scalars['Int']['input'];
}>;


export type GetUserQuery = { __typename?: 'Query', user?: { __typename?: 'User', id: number, name: string, email: string, createdAt: any } | null };


export const CreateUserDocument = gql`
    mutation CreateUser($name: String!, $email: String!) {
  createUser(name: $name, email: $email) {
    id
    name
    email
    createdAt
  }
}
    `;
export const UpdateUserDocument = gql`
    mutation UpdateUser($id: Int!, $name: String!, $email: String!) {
  updateUser(id: $id, name: $name, email: $email) {
    id
    name
    email
    createdAt
  }
}
    `;
export const DeleteUserDocument = gql`
    mutation DeleteUser($id: Int!) {
  deleteUser(id: $id)
}
    `;
export const GetUsersDocument = gql`
    query GetUsers {
  users {
    id
    name
    email
    createdAt
  }
}
    `;
export const GetUserDocument = gql`
    query GetUser($id: Int!) {
  user(id: $id) {
    id
    name
    email
    createdAt
  }
}
    `;

export type SdkFunctionWrapper = <T>(action: (requestHeaders?:Record<string, string>) => Promise<T>, operationName: string, operationType?: string, variables?: any) => Promise<T>;


const defaultWrapper: SdkFunctionWrapper = (action, _operationName, _operationType, _variables) => action();

export function getSdk(client: GraphQLClient, withWrapper: SdkFunctionWrapper = defaultWrapper) {
  return {
    CreateUser(variables: Types.CreateUserMutationVariables, requestHeaders?: GraphQLClientRequestHeaders): Promise<Types.CreateUserMutation> {
      return withWrapper((wrappedRequestHeaders) => client.request<Types.CreateUserMutation>(CreateUserDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'CreateUser', 'mutation', variables);
    },
    UpdateUser(variables: Types.UpdateUserMutationVariables, requestHeaders?: GraphQLClientRequestHeaders): Promise<Types.UpdateUserMutation> {
      return withWrapper((wrappedRequestHeaders) => client.request<Types.UpdateUserMutation>(UpdateUserDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'UpdateUser', 'mutation', variables);
    },
    DeleteUser(variables: Types.DeleteUserMutationVariables, requestHeaders?: GraphQLClientRequestHeaders): Promise<Types.DeleteUserMutation> {
      return withWrapper((wrappedRequestHeaders) => client.request<Types.DeleteUserMutation>(DeleteUserDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'DeleteUser', 'mutation', variables);
    },
    GetUsers(variables?: Types.GetUsersQueryVariables, requestHeaders?: GraphQLClientRequestHeaders): Promise<Types.GetUsersQuery> {
      return withWrapper((wrappedRequestHeaders) => client.request<Types.GetUsersQuery>(GetUsersDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'GetUsers', 'query', variables);
    },
    GetUser(variables: Types.GetUserQueryVariables, requestHeaders?: GraphQLClientRequestHeaders): Promise<Types.GetUserQuery> {
      return withWrapper((wrappedRequestHeaders) => client.request<Types.GetUserQuery>(GetUserDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'GetUser', 'query', variables);
    }
  };
}
export type Sdk = ReturnType<typeof getSdk>;
