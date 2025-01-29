import { Form, useLoaderData, useSubmit } from "@remix-run/react";
import type { User } from "~/types";

export function UserList() {
  const { users } = useLoaderData<{ users: User[] }>();
  const submit = useSubmit();

  const handleDelete = (
    e: React.MouseEvent<HTMLButtonElement>,
    userId: number
  ) => {
    e.preventDefault();

    if (confirm("本当に削除しますか？")) {
      const formData = new FormData();
      formData.set("_action", "delete");
      formData.set("id", userId.toString());
      submit(formData, { method: "post" });
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">ユーザー管理（GraphQL）</h2>

      <Form method="post" className="mb-4">
        <div className="flex gap-2">
          <input
            type="text"
            name="name"
            placeholder="名前"
            className="border p-2 rounded"
          />
          <input
            type="email"
            name="email"
            placeholder="メールアドレス"
            className="border p-2 rounded"
          />
          <button
            type="submit"
            name="_action"
            value="create"
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            追加
          </button>
        </div>
      </Form>

      {/* ユーザー一覧 */}
      <div className="space-y-2">
        {users.map((user) => (
          <div
            key={user.id}
            className="flex justify-between items-center border p-2 rounded"
          >
            <div>
              <p className="font-bold">{user.name}</p>
              <p className="text-sm text-gray-600">{user.email}</p>
            </div>
            <Form method="post">
              <input type="hidden" name="id" value={user.id} />
              <button
                type="submit"
                name="_action"
                value="delete"
                className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                onClick={(e) => handleDelete(e, user.id)}
              >
                削除
              </button>
            </Form>
          </div>
        ))}
      </div>
    </div>
  );
}
