import { json } from "@remix-run/node";
import type { LoaderFunction, ActionFunction } from "@remix-run/node";
import { UserList } from "~/components/UserList";
import { sdk } from "~/lib/graphql/graphql-client";

export const loader: LoaderFunction = async () => {
  const { users } = await sdk.GetUsers()
  return json({ users });
};

export const action: ActionFunction = async ({ request }) => {
  const formData = await request.formData();
  const action = formData.get("_action");

  switch (action) {
    case "create":
      await sdk.CreateUser({
        name: formData.get("name") as string,
        email: formData.get("email") as string,
      });
      break;

    case "delete":
      await sdk.DeleteUser({
        id: Number(formData.get("id")),
      });
      break;
  }

  return json({ ok: true });
};

export default function GraphQLPage() {
  return <UserList />;
}
