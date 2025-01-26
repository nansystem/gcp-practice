import { type LoaderFunction } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";

type LoaderData = {
  message: string;
};

export const loader: LoaderFunction = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/hello');
    const data = await response.json();
    
    return new Response(JSON.stringify(data), {
      headers: {
        'Content-Type': 'application/json',
      },
    });
  } catch (error) {
    console.error('APIエラー:', error);
    return new Response(
      JSON.stringify({ message: 'エラーが発生しました' }), 
      {
        status: 500,
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
  }
};

export default function Index() {
  const { message } = useLoaderData<LoaderData>();

  return (
    <div className="p-4">
      <h1>FastAPIからのメッセージ</h1>
      <p className="mt-4">{message}</p>
    </div>
  );
}