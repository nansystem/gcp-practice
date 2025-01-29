import { json } from "@remix-run/node";
import type { LoaderFunction, ActionFunction } from "@remix-run/node";
import { UserList } from "~/components/UserList";
import { getUsers } from "~/queries/getUsers";
import { createUser } from "~/mutations/createUser";
import { deleteUser } from "~/mutations/deleteUser";

export const loader: LoaderFunction = async () => {
  const users = await getUsers();
  return json({ users });
};

export const action: ActionFunction = async ({ request }) => {
  const formData = await request.formData();
  const action = formData.get("_action");

  switch (action) {
    case "create":
      await createUser(
        formData.get("name") as string,
        formData.get("email") as string
      );
      break;

    case "delete":
      await deleteUser(Number(formData.get("id")));
      break;
  }

  return json({ ok: true });
};

export default function GraphQLPage() {
  return <UserList />;
}
