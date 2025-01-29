import { type LoaderFunction } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";

type User = {
  id: number;
  name: string;
  email: string;
};

type LoaderData = {
  users: User[];
};

export const loader: LoaderFunction = async () => {
  try {
    const backendUrl = process.env.BACKEND_URL || "http://localhost:8000";
    const response = await fetch(`${backendUrl}/api/v1/users`);
    const data = await response.json();

    return { users: data };
  } catch (error) {
    console.error("APIエラー:", error);
    return {
      users: [],
    };
  }
};

export default function Index() {
  const { users } = useLoaderData<LoaderData>();

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">ユーザー一覧</h1>

      <div>
        {users.map((user) => (
          <div key={user.id} className="p-2">
            <p>
              {user.name}/{user.email}
            </p>
          </div>
        ))}
      </div>

      {users.length === 0 && <p>ユーザーがRest APIで見つかりません</p>}
    </div>
  );
}
